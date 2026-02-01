# Inventory Management Flask Backend

This Flask backend implements user login and server data search.

- `/api/login`: Accepts username and password, returns JWT token with role.
- `/api/servers`: Search endpoint protected by JWT. Returns servers matching query.
- `token_required`: Decorator to check JWT validity and extract user info.
- Dummy data and users for demonstration.

Authentication ensures role-based access; currently supports reader and owner roles.
