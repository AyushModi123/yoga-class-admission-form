from fastapi import HTTPException
from datetime import timedelta
from pydantic import BaseModel,  constr, ValidationError, validator, EmailStr
from typing import List, Dict, Optional

class EnrollSchema(BaseModel):
    name: constr(min_length=3, max_length=50)
    email: EmailStr  
    contact_no: constr(min_length=10, max_length=13)        
    age: int
    batch: constr(regex="^(6-7AM|7-8AM|8-9AM|5-6PM)$")
    amount: int    

    @validator('amount')
    def validate_amount(cls, value, values, **kwargs):
        if not value%500==0 or value==0:
            raise HTTPException(status_code=422, detail="Amount must be a multiple of 500")
        return value

    @validator('age')
    def validate_age(cls, value, values, **kwargs):
        if not 18 <= value <= 65:
            raise HTTPException(status_code=422, detail="Age must be between 18 and 65")
        return value

class BatchSchema(BaseModel):
    email: EmailStr
    batch: constr(regex="^(6-7AM|7-8AM|8-9AM|5-6PM)$")
    
class PaymentSchema(BaseModel):
    email: EmailStr
    amount: int

    @validator('amount')
    def validate_amount(cls, value, values, **kwargs):
        if not value%500==0 or value==0:
            raise HTTPException(status_code=422, detail="Amount must be a multiple of 500")
        return value