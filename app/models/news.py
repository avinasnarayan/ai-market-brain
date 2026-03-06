from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database import Base
import datetime

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    source = Column(String)
    sentiment = Column(String)
    impact_score = Column(Float)
    sector = Column(String)
    hash = Column(String, unique=True)
    published_at = Column(DateTime)