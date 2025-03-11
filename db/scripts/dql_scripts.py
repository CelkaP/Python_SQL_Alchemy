from db.core.initializer import create_connection, engine
from db.models.test_data import TestData
from sqlalchemy.orm import sessionmaker

# Create a session factory
Session = sessionmaker(bind=engine)

class DQL:
    """Encapsulates database query language (DML)"""

    @staticmethod
    def retrieve_all_items():
        """
        Retrieves all data entries and corresponding columns from Item table.
        """
        with Session() as session:
            return session.query(TestData).all()

    @staticmethod
    def retrieve_all_items_as_dict():
        """
        Retrieves all data entries and corresponding columns from the test_data table.
        :return: list of dictionaries
        """
        with Session() as session:
            items = session.query(TestData).all()
            return [{key: value for key, value in item.__dict__.items() if key != "_sa_instance_state"} for item in items]
