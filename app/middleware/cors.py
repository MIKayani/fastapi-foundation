from fastapi.middleware.cors import CORSMiddleware
from app.schemas.config_schema import settings

def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin.strip() for origin in settings.CORS_ALLOWED_ORIGINS.split(',')],
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=[method.strip() for method in settings.CORS_ALLOWED_METHODS.split(',')],
        allow_headers=[header.strip() for header in settings.CORS_ALLOWED_HEADERS.split(',')],
    )
