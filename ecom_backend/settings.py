import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ========= Database Setting ====================
engine = create_engine("postgresql://akki_ecom:root@localhost:5433/ecom", echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

# ==========JWT=========================
# SECRET_KEY = os.getenv("secret_key")
# ALGORITHM = os.getenv("algorithm")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
