from src.config.db_settings import Base
from sqlalchemy import Column, String


class Login(Base):
    __tablename__ = "logins"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)