from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from uuid import UUID,uuid4
from app.core.db.database import Base


class User(Base):
    __tablename__ = "users"

    # Unique identifiers
    id:Mapped[UUID] = mapped_column(primary_key=True,default=uuid4)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(unique=True)

    password: Mapped[str] = mapped_column()

    # Activity log
    phone_verified: Mapped[bool] = mapped_column(default=False)
    phone_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    email_verified: Mapped[bool] = mapped_column(default=False)
    email_verified_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    last_logged_in_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    
    # Access Control
    disabled: Mapped[bool] = mapped_column(default=False)
    disabled_till: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True)) 

    

    # Housekeeping columns
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now()) 
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now()) 