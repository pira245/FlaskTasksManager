from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base




# Create the engine to connect to the SQLite database
#engine = create_engine('sqlite:///database/tareas.sqlite3', connect_args={'check_same_thread': False})
engine = create_engine('sqlite:///core_package/database/tareas.sqlite3', connect_args={'check_same_thread': False})

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create a base class for our classes definitions
Base = declarative_base()

def init_db():
    """
    Initialize the database by creating all tables.
    """
    import models
    Base.metadata.create_all(engine)


