from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
# from models.index import Base

engine = create_engine("mysql+pymysql://root@localhost:3306/test")


SessionLocal = sessionmaker(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# @event.listens_for(engine, "connect")
# def create_tables(*args, **kwargs):
#     Base.metadata.create_all(bind=engine)


