from models.users import ParticipantModel, BatchModel, EnrollmentHistoryModel
from models.payments import PaymentHistoryModel
from utils.payment import CompletePayment, calc_expiration_date, calc_start_of_next_month
from fastapi.responses import JSONResponse, Response, RedirectResponse
from fastapi import HTTPException, Depends
from db import Session, get_db
from . import logging, logger
from schemas import EnrollSchema, BatchSchema
from fastapi import APIRouter, Depends
from . import logging, logger

router = APIRouter(prefix="", tags=["Enroll Customer"])

@router.post("/enroll")
async def enroll_user(user_data: EnrollSchema, db: Session = Depends(get_db)):    
    user_record = db.query(ParticipantModel).filter_by(email=user_data.email).first()
    if user_record:
        raise HTTPException(status_code=409, detail="Already Registered")
    user_record = ParticipantModel(
        name=user_data.name,
        email=user_data.email,
        contact_no=user_data.contact_no,
        age=user_data.age
    )
    try:
        db.add(user_record)
        db.flush()
        # batch_id = db.query(BatchModel).filter_by(batch_time=user_data.batch).first().batch_id
        batch_id=1
        expiration_date = calc_expiration_date(user_data.amount)
        db.add(EnrollmentHistoryModel(
            participant_id=user_record.participant_id,
            batch_id=batch_id,        
            expiry_date=expiration_date
        ))
        db.flush()
    except Exception as e:
        db.rollback()
        logging.exception("Exception occurred")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    response = CompletePayment(user_data.amount)
    if not response:
        raise HTTPException(status_code=400, detail="Payment failed")
    try:
        db.add(PaymentHistoryModel(
            amount=user_data.amount,
            participant_id=user_record.participant_id
        ))            
    except Exception as e:
        db.rollback()
        logging.exception("Exception occurred")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Successful"})
    
    

@router.put("/change-batch")
async def change_batch(user_data: BatchSchema, db: Session = Depends(get_db)):
    user_record = db.query(ParticipantModel).filter_by(email=user_data.email).first()
    if not user_record:
        raise HTTPException(status_code=404, detail="User Not Found")
    # batch_id = db.query(BatchModel).filter_by(batch_time=user_data.batch).first().batch_id
    batch_id=2
    enroll_record = db.query(EnrollmentHistoryModel).filter_by(participant_id=user_record.participant_id).order_by(EnrollmentHistoryModel.enrollment_date.desc()).first()
    db.add(EnrollmentHistoryModel(
        participant_id=user_record.participant_id,
        batch_id=batch_id,        
        enrollment_date=calc_start_of_next_month(),
        expiry_date=enroll_record.expiry_date
    ))
    db.commit()
    print(db.query(EnrollmentHistoryModel).filter_by(participant_id=user_record.participant_id).all())
    return JSONResponse(status_code=201, content={"message": "Batch changed successfully for next month"})
    