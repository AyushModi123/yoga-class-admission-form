from models.users import ParticipantModel, EnrollmentHistoryModel
from models.payments import PaymentHistoryModel
from utils.payment import CompletePayment, calc_expiration_date
from fastapi.responses import JSONResponse, Response, RedirectResponse
from fastapi import HTTPException, Depends
from db import Session, get_db
from . import logging, logger
from fastapi import APIRouter, Depends
from schemas import PaymentSchema

router = APIRouter(prefix="/payment", tags=["Payments"])

@router.post("")
async def payment(payment_details: PaymentSchema, db: Session = Depends(get_db)):        
    user_record = db.query(ParticipantModel).filter_by(email=payment_details.email).first()
    if not user_record:
        raise HTTPException(status_code=404, detail="User Not Found")
    enroll_record = db.query(EnrollmentHistoryModel).filter_by(participant_id=user_record.participant_id).order_by(EnrollmentHistoryModel.enrollment_date.desc()).first()
    response = CompletePayment(payment_details.amount)
    if not response:
        raise HTTPException(status_code=400, detail="Payment failed")
    try:
        db.add(PaymentHistoryModel(
            amount=payment_details.amount,
            participant_id=user_record.participant_id
        ))
        expiration_date = calc_expiration_date(payment_details.amount)
        enroll_record.expiry_date = expiration_date
    except Exception as e:
        db.rollback()
        logging.exception("Exception occurred")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Payment Successful"})
