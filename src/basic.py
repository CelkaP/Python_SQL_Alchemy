from sqlalchemy import text
from db.core.initializer import create_connection


def run_db_select_statement():
    """Creates a self closing connection to the database after outputting 'Hello World'"""
    try:
        with create_connection() as conn:
            result = conn.execute(text("select 'Hello World'"))
            data = result.all()
            print(f"Query Result: {data}")  # Print the result explicitly
    except Exception as e:
        print(f"Database query failed: {e}")