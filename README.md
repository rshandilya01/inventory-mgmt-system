# Inventory Management System

## Overview
This Inventory Management System is a web-based application designed to centrally manage and search IT server inventory metadata, including server names, IPs, project details, owners, service tags, license expiry dates, applications, databases, purposes, and environments. It supports user login and role-based access, ensuring that owners can update servers they own while other users have read-only access.

## Core Features
- **Centralized Search:** Unified search bar to fetch data using multiple fields like server name, IP address, owner, application, database, etc.
- **User Authentication:** Secure login with JWT-based token authentication.
- **Role-Based Access Control:** 
  - Owners can update server records.
  - Other authenticated users can only read data.
- **Multi-User Collaboration:** Multiple owners can update the same server concurrently.
- **Audit Logging (Planned):** Tracking changes by users for accountability.

## Technical Architecture
- **Frontend:** React.js for an interactive UI with components for login, searching, and displaying results.
- **Backend:** Python Flask REST API managing authentication, search queries, and user permissions.
- **Database:** Relational (e.g., PostgreSQL) to store structured inventory data and user records.
- **Authentication:** JWT tokens for session management and security.
- **Search Optimization:** Potential Elasticsearch integration for scalable and fast multi-field searching.
- **Hosting:** Cloud platform (AWS, GCP, or Azure) for scalability and security.

## Modular Components

### Frontend Modules
- `Login.js` — Handles user login and JWT token retrieval.
- `SearchBar.js` — Provides UI to enter search queries.
- `ServerList.js` — Displays server inventory search results.
- `App.js` — Main controller managing auth state and rendering components.

### Backend Modules
- `app.py` — Flask application exposing `/api/login` for authentication and `/api/servers` for search operations.
- `token_required` decorator — Secures API endpoints by validating JWT.
- Dummy data and user store for demonstration, extendable to real database integration.

## How to Run

### Frontend
- Run `npm install` to install dependencies.
- Use `npm start` to launch the React development server.
- The frontend communicates with the backend API using authenticated requests.

### Backend
- Install Python dependencies: `pip install flask flask-cors pyjwt`
- Run `python app.py` to start the Flask API server.
- Supports login and protected search endpoints.

## Testing Instructions

### Frontend Testing
1. Make sure the backend API is running and accessible.
2. Start the frontend app with `npm start`.
3. Open the web app in the browser (usually at `http://localhost:3000`).
4. Use the login page with sample credentials (e.g., username: `"owner1"`, password: `"password1"`).
5. After login, enter search queries in the search bar to fetch servers.
6. Confirm that results appear as expected and the UI updates correctly.
7. Test invalid login attempts to verify error handling.
8. Optional: Use React Testing Library or similar to write unit tests for components.

### Backend Testing
1. Ensure Python environment has required modules installed.
2. Run `python app.py` to start the Flask server.
3. Test authentication endpoint:
   - POST `/api/login` with JSON body `{ "username": "owner1", "password": "password1" }`.
   - Confirm you receive a JWT token on success.
4. Test search endpoint:
   - GET `/api/servers?query=server` with `Authorization: Bearer <token>` header.
   - Verify JSON response contains expected server data.
5. Test invalid token or missing token returns 401 Unauthorized.
6. Optional: Write unit tests using pytest or unittest covering authentication and API responses.

## Future Enhancements
- Full CRUD operations to create, update, and delete server records.
- Real database integration for persistent storage.
- Audit trail and detailed role management.
- More advanced search features with Elasticsearch.
- Two-factor authentication for enhanced security.
