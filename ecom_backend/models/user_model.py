from ecom_backend.settings import Base
from sqlalchemy import Column, Integer, Boolean, Text, String


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String(30), unique=True)
    user_name = Column(String(27), unique=True)
    password = Column(Text, nullable=True)
    is_admin = Column(Boolean, default=False, nullable=True)
    is_active = Column(Boolean, default=True, nullable=True)

    def __repr__(self):
        return f"User: {self.user_name}"
