import streamlit as st
import requests
from datetime import datetime, timedelta
import calendar
from dotenv import load_dotenv
load_dotenv()
import os

API_URL =  os.getenv('API_URL')

st.title("Yoga Class Admission Form")

name = st.text_input("Name:")
age = st.number_input("Age:", min_value=18, max_value=65)
email = st.text_input("Email:", placeholder="example@example.com")
contact_no = st.text_input("Contact Number:")
location = st.text_input("Location:")
batch = st.selectbox("Select Batch:", ["6-7AM", "7-8AM", "8-9AM", "5-6PM"])
amount = st.number_input("Amount:", min_value=500, step=500)


if amount % 500 != 0:
    st.warning("Amount must be a multiple of 500.")

months_valid = amount // 500
current_date = datetime.now().replace(day=1).date()
expiration_date = current_date + timedelta(days=30 * months_valid)
last_day_of_month = calendar.monthrange(expiration_date.year, expiration_date.month)[1]
expiration_date = datetime(expiration_date.year, expiration_date.month, last_day_of_month)

st.text(f"The subscription of {amount} INR will be valid until {expiration_date.date()}.")

if st.button("Enroll"):    
    user_data = {"name": name, "age": age, "batch": batch, "email": email, "contact_no": contact_no, "location": location, "amount": amount, "currency": "INR"}
    response = requests.post(f"{API_URL}/enroll", json=user_data)    
    if response.status_code == 200:        
        st.success(response.json()["detail"])

        # Add a payment button
        # if st.button("Make Payment"):            
        #     payment_data = {"email": email, "amount": amount}
        #     payment_response = requests.post(f"{API_URL}/payment", json=payment_data)
        #     if payment_response.status_code == 200:
        #         st.success("Payment successful!")
        #     else:
        #         st.error("Payment failed. Please try again.")
    else:
        st.error("Enrollment failed. Please check your details and try again.")