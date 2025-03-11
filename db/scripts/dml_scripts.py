from db.core.initializer import create_connection, engine
from db.models.test_data import TestData
import datetime
from sqlalchemy.orm import sessionmaker

# Create a session factory
Session = sessionmaker(bind=engine)


class DML:
    """Encapsulates database manipulation language (DML)"""

    @staticmethod
    def add_item(date: datetime, title: str, author: str):
        """Adds a single item to Item table"""
        with Session() as session:
            try:
                item = TestData(date=date, title=title, author=author)
                session.add(item)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred while adding an item: {e}")

    @staticmethod
    def add_items(items_data):
        with Session() as session:
            try:
                items = [TestData(**data) for data in items_data]
                session.add_all(items)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred while adding items: {e}")

    @staticmethod
    def remove_item(item_id: int):
        with Session() as session:
            try:
                item = session.query(TestData).filter_by(id=item_id).first()
                if item:
                    session.delete(item)
                    session.commit()
                    print(f"Item with id {item_id} has been successfully deleted.")
                else:
                    print(f"Item with id {item_id} not found.")
            except Exception as e:
                session.rollback()
                print(
                    f"Error occurred while trying to delete item with id: {item_id}. \nMessage: {e}"
                )
