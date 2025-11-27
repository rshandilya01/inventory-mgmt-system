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
- The frontend sends authenticated requests to the backend API.

### Backend
- Install Python dependencies: `pip install flask flask-cors pyjwt`
- Run `python app.py` to start the Flask API server.
- Supports login and protected search endpoints.

## Future Enhancements
- Full CRUD operations to create, update, and delete server records.
- Real database integration for persistent storage.
- Audit trail and detailed role management.
- More advanced search features with Elasticsearch.
- Two-factor authentication for enhanced security.

