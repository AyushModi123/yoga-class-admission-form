from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, ARRAY, Date, func
from sqlalchemy.types import Enum, UUID
from datetime import datetime
from . import Base

class ParticipantModel(Base):
    __tablename__ = 'participants'

    participant_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String, unique=True, nullable=False)
    contact_no = Column(String(15), nullable=False)
    age = Column(Integer, nullable=False)

class BatchModel(Base):
    __tablename__ = 'batches'

    batch_id = Column(Integer, primary_key=True)
    batch_time = Column(Enum('6-7AM', '7-8AM', '5-6PM', '8-9AM'), unique=True, nullable=False)

class EnrollmentHistoryModel(Base):
    __tablename__ = 'enrollment_history'

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    participant_id = Column(Integer, ForeignKey('participants.participant_id'), nullable=False)
    batch_id = Column(Integer, ForeignKey('batches.batch_id'), nullable=False)
    enrollment_date = Column(Date, default=datetime.now().date(), nullable=False)
    expiry_date = Column(Date, nullable=False)

