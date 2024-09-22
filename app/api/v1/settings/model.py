from sqlalchemy import Column, DateTime, Integer, Numeric, String, func
from app.core.db.database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    price = Column(Numeric)
    last_sold = Column(DateTime)
    created_at = Column(DateTime, default=func.now())