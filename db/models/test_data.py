import datetime
from sqlalchemy import Column, String, Integer, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base
from db.core.initializer import create_connection
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class TestData(Base):
    __tablename__ = "test_data"

    id = Column(Integer, Sequence("item_id"), primary_key=True)
    date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    title = Column(String(500), nullable=False)
    author = Column(String(500), nullable=False)


# Set up the engine and session
engine = create_connection()
Session = sessionmaker(bind=engine)


def create_test_data_table():
    # Create the table (if it does not exist already)
    Base.metadata.create_all(engine, checkfirst=True)


def drop_test_data():
    # Drop the table
    TestData.__table__.drop(engine)
