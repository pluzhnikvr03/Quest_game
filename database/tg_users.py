from database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func



class TelegramUser(Base):
    __tablename__ = 'telegramusers'
    telegram_id = Column(
        Integer,
        primary_key=True,
        unique=True
    )
    username = Column(
        String(),
        nullable=True
    )
    first_name = Column(
        String(),
        nullable=True
    )
    time_add = Column(
        DateTime,
        server_default=func.now()
    )