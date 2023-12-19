from datetime import datetime, timedelta
import calendar

def CompletePayment(amount: int, currency: str="INR") -> bool:
    return True

def calc_expiration_date(amount: int):
    months_valid = amount // 500
    current_date = datetime.now().replace(day=1).date()
    expiration_date = current_date + timedelta(days=30 * months_valid)
    last_day_of_month = calendar.monthrange(expiration_date.year, expiration_date.month)[1]
    expiration_date = datetime(expiration_date.year, expiration_date.month, last_day_of_month).date()
    return expiration_date

def calc_start_of_next_month():
    current_date = datetime.now().replace(day=1).date()
    next_month = current_date + timedelta(days=32)
    start_of_next_month = next_month.replace(day=1)
    return start_of_next_month
