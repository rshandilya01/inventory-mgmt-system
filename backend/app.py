from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app)

# Secret key for JWT
app.config["SECRET_KEY"] = "your_secret_key"

# Dummy user database
users = {
    "owner1": {"password": "password1", "role": "owner"},
    "user1": {"password": "password2", "role": "reader"},
}

# Dummy server inventory data
servers = [
    {
        "id": 1,
        "server_name": "Server A",
        "ip": "192.168.1.1",
        "owner": "owner1",
        "license_expiry": "2025-12-31",
        "application": "App1",
        "database": "DB1",
        "purpose": "Web Server",
        "environment": "Production",
    },
    {
        "id": 2,
        "server_name": "Server B",
        "ip": "192.168.1.2",
        "owner": "owner1",
        "license_expiry": "2026-01-15",
        "application": "App2",
        "database": "DB2",
        "purpose": "Database Server",
        "environment": "Development",
    },
]

def token_required(f):
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = data["username"]
            role = data["role"]
        except Exception as e:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(current_user, role, *args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated

@app.route("/api/login", methods=["POST"])
def login():
    auth = request.get_json()
    username = auth.get("username")
    password = auth.get("password")
    user = users.get(username)
    if not user or user["password"] != password:
        return jsonify({"message": "Invalid credentials"}), 401
    token = jwt.encode({
        "username": username,
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config["SECRET_KEY"])
    return jsonify({"token": token})

@app.route("/api/servers", methods=["GET"])
@token_required
def get_servers(current_user, role):
    query = request.args.get("query", "").lower()
    results = []
    for s in servers:
        searchable_values = f"{s['server_name']} {s['ip']} {s['owner']} {s['application']} {s['database']} {s['purpose']} {s['environment']}".lower()
        if query in searchable_values:
            results.append(s)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
