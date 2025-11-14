from database.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql import func


class TelegramUser(Base):
    __tablename__ = 'messages'
    id_message = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    text_message = Column(
        String(),
        nullable=True
    )
    author_telegram_id = Column(
        Integer,
        ForeignKey('telegramusers.telegram_id')
    )
