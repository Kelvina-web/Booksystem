from sqlalchemy import create_engine
from lib.db.models import Base

engine = create_engine('sqlite:///bookbuddy.db')

def init_db():
    Base.metadata.create_all(engine)
    print("Database initialized.")

if __name__ == '__main__':
    init_db()
