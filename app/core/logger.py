import logging
import sys
import warnings
from app.schemas.config_schema import settings

_logging_configured = False

def get_logger(name: str) -> logging.Logger:
    """
    Initializes and returns a logger with a specified name.
    The first time this is called, it will also configure the root logger
    with settings from the environment.
    """
    global _logging_configured
    if not _logging_configured:
        # Configure root logger
        root_logger = logging.getLogger()

        # Clear any existing handlers
        if root_logger.hasHandlers():
            root_logger.handlers.clear()

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

        # Set level from settings
        root_logger.setLevel(settings.LOGLEVEL.upper())

        # Ignore future warnings
        warnings.simplefilter(action="ignore", category=FutureWarning)

        _logging_configured = True

    return logging.getLogger(name)