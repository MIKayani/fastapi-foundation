import os
from app.core.config import get_postgres_connection
from app.core.logger import get_logger

logger = get_logger(__name__)

def initialize_database():
    """
    Initializes the database by running the DataBase.sql script.
    This is controlled by the DATABASE_INIT environment variable.
    """

    logger.info("Starting database initialization...")
    conn = None  # Initialize conn to None
    try:
        # The SQL file is in the same directory as this script.
        sql_file_path = os.path.join(os.path.dirname(__file__), 'DataBase.sql')

        with open(sql_file_path, 'r') as f:
            # Split statements by semicolon and filter out empty ones
            sql_statements = [statement.strip() for statement in f.read().split(';') if statement.strip()]

        if not sql_statements:
            logger.info("No SQL statements found in DataBase.sql. Nothing to execute.")
            return

        conn = get_postgres_connection()
        with conn.cursor() as cursor:
            for statement in sql_statements:
                logger.debug(f"Executing SQL: {statement[:100]}...") # Log snippet
                cursor.execute(statement)
        conn.commit()
        logger.info("Database initialization successful.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            logger.info("Database initialization routine finished. The global connection is left open.")
