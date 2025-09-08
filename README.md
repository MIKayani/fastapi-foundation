# FastAPI Foundation

⚡ FastAPI Foundation is a production-ready boilerplate for building scalable FastAPI applications. It comes with a clean modular architecture, PostgreSQL integration, centralized configuration, authentication middleware, logging, and other essentials—so you can focus on writing business logic instead of setup.

This project serves as a robust, production-ready skeleton for building FastAPI applications. It comes pre-configured with a modular structure, centralized configuration management, database integration, and essential middleware.

## Features

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs.
- **Pydantic**: Centralized, type-safe configuration management that fails fast.
- **PostgreSQL Integration**: Pre-configured for use with a PostgreSQL database.
- **Dependency Injection**: Leverages FastAPI's dependency injection system.
- **Modular Design**: Code is organized into logical modules (`core`, `middleware`, `schemas`, `db`, `api`).
- **Authentication**: Includes middleware for protecting API docs and a placeholder for token-based API authentication.
- **CORS**: Pre-configured CORS middleware.
- **Logging**: Centralized logging setup.

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL server

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your environment:**
    -   Create a `.env` file by copying the example:
        ```bash
        cp .env.example .env
        ```
    -   Open the `.env` file and edit the variables, especially the `DB_*` values, to match your local setup.

### Running the Application

-   **Development server with auto-reload:**
    ```bash
    uvicorn main:app --reload
    ```
-   The API will be available at `http://127.0.0.1:8000`.
-   The interactive API documentation (Swagger UI) will be at `http://127.0.0.1:8000/docs`.

## Project Structure

```
.
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       ├── dependencies.py
│   │       └── routes/
│   │           └── server_info.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── openapi.py
│   ├── db/
│   │   ├── auth.py           # <-- TODO: Implement your auth logic here
│   │   ├── DataBase.sql
│   │   └── init_db.py
│   ├── middleware/
│   │   ├── auth.py
│   │   └── cors.py
│   └── schemas/
│       └── config_schema.py
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Authentication

The `AccessTokenAuthMiddleware` is set up to protect your API endpoints. However, the actual token validation logic is just a placeholder.

To implement your own authentication:
1.  Go to `app/db/auth.py`.
2.  Modify the `get_user_id_from_token` function to contain your real logic for validating a token and returning a user ID. This might involve querying the database, decoding a JWT, or calling an external service.

```python
# app/db/auth.py

def get_user_id_from_token(token: str) -> str | None:
    """
    This is a placeholder for the actual token validation logic.
    - Validate the token.
    - Return the user ID if the token is valid.
    - Return None if the token is invalid.
    """
    # TODO: Replace this with your actual authentication logic
    if token == "valid_token_xyz789":
        return "user_123"
    return None
```