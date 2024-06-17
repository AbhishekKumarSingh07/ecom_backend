from sqlalchemy.orm import Session, sessionmaker
from ecom_backend.settings import engine, SessionLocal, Base
from fastapi import HTTPException

Base.metadata.create_all(bind=engine)


def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    except Exception as exception:
        print(exception)
        raise
    finally:
        db.close()
