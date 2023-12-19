from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, ARRAY, Date, func
from sqlalchemy.types import Enum, UUID
from datetime import datetime
from . import Base

class PaymentHistoryModel(Base):
    __tablename__ = "payments_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)    
    payment_date = Column(Date, default=datetime.now().date(), nullable=False)
    participant_id = Column(Integer, ForeignKey('participants.participant_id'), nullable=False)