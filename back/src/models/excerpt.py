from sqlalchemy import Column, Integer, String
from src.config.db_settings import Base


class Excerpt(Base):
    __tablename__ = "excerpts"

    id = Column(String, primary_key=True, index=True)
    text = Column(String)
    category = Column(Integer)
    test_or_train = Column(String, default="real-life")
