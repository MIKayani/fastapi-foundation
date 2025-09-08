from fastapi import FastAPI
from app.middleware.auth import AccessTokenAuthMiddleware, DocsAuthMiddleware
from app.middleware.cors import add_cors_middleware
from app.core.openapi import custom_openapi
from app.schemas.config_schema import settings
from app.db.init_db import initialize_database

from app.api.endpoints.routes import (
    server_info, 
)

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)

@app.on_event("startup")
async def startup_event():
    if settings.DATABASE_INIT:
        initialize_database()

# Add middlewares
add_cors_middleware(app)
app.add_middleware(DocsAuthMiddleware)
app.add_middleware(AccessTokenAuthMiddleware)

# Include routers
app.include_router(server_info.router)

# Set custom OpenAPI schema
app.openapi = lambda: custom_openapi(app)