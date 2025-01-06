from src.database.db import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)