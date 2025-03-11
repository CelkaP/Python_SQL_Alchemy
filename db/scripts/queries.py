from db.core.initializer import create_connection, engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

# Create a session factory
Session = sessionmaker(bind=engine)

def show_all_tables():
    """
    Show all available tables in the database.
    """
    with Session() as session:
        inspector = inspect(session.bind)
        tables = inspector.get_table_names()

    if not tables:
        print("No tables found in the database")
    else:
        for table in tables:
            print(f"{table} Table")
