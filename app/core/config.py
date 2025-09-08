from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.logger import get_logger, setup_logging
from app.schemas.config_schema import Settings

load_dotenv()

# 1. Create the configuration instance, which will read from the environment
config = Settings()

# 2. Set up logging based on the loaded configuration
setup_logging(config.LOGLEVEL)

# 3. Get a logger for this file, now that logging is configured
logger = get_logger(__name__)

postgres_connection = None

def get_postgres_connection():
    """
    Establishes and returns a PostgreSQL connection using psycopg2.
    If the global connection is not active, it attempts to reconnect.
    """
    global postgres_connection

    if postgres_connection and not postgres_connection.closed:
        try:
            with postgres_connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            logger.debug("Existing PostgreSQL connection is active.")
            return postgres_connection
        except psycopg2.Error as e:
            logger.warning(f"Existing PostgreSQL connection is stale or broken: {e}. Attempting to reconnect.")
            if postgres_connection:
                try:
                    postgres_connection.close()
                except psycopg2.Error as close_e:
                    logger.error(f"Error closing stale connection: {close_e}")
            postgres_connection = None

    try:
        postgres_connection = psycopg2.connect(
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
            cursor_factory=RealDictCursor
        )
        logger.info("PostgreSQL connection established successfully.")
        return postgres_connection
    except Exception as e:
        logger.error(f"Failed to connect to PostgreSQL: {e}")
        raise
