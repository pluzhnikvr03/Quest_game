from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base_model import Base


engine = create_engine('sqlite:///name_db.db')
session = sessionmaker(bind=engine)


def init_db():
    print('База создается')
    Base.metadata.create_all(bind=engine)
    print('База создана')