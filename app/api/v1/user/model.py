from sqlalchemy import Column, DateTime, Integer, Numeric, String, func,UUID
from app.core.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    price = Column(Numeric)
    last_sold = Column(DateTime)
    created_at = Column(DateTime, default=func.now())