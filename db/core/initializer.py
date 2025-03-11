from sqlalchemy import create_engine
from conf.settings.base import DATABASE

# Create database engine
engine = create_engine(
    "mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4".format(
        db_username=DATABASE['USERNAME'],
        db_password=DATABASE['PASSWORD'],
        db_host=DATABASE['HOST'],
        db_port=DATABASE['PORT'],
        db_name=DATABASE['NAME']
    ),
    echo=True
)

def create_connection():
    print("Connecting to a database.")
    return engine.connect()