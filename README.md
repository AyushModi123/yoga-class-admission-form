# yoga-class-admission-form
Streamlined yoga class enrollment system using FastAPI for a robust backend and Streamlit for a user-friendly frontend. Seamlessly manage monthly payments and flexible batch selections for a stress-free yoga experience.

Requirements for the admission form are:
- Only people within the age limit of 18-65 can enroll for the monthly classes and they will
be paying the fees on a month on month basis. I.e. an individual will have to pay the fees
every month and he can pay it any time of the month.
- They can enroll any day but they will have to pay for the entire month. The monthly fee is
500/- Rs INR.
- There are a total of 4 batches a day namely 6-7AM, 7-8AM, 8-9AM and 5-6PM. The
participants can choose any batch in a month and can move to any other batch next
month. I.e. participants can shift from one batch to another in different months but in the
same month they need to be in the same batch.

Implementation Details

- Accepts the user data, does basic validations.
- Store the data in database.
- Assumes a mock function named CompletePayment() which accepts the
details of user and payment and does the payment for you.
- Return the response to front-end depending on the payment response from
CompletePayment() function.

FastAPI backend and ReactJs Frontend is containerized using Docker.

ER Diagram-

![image](https://github.com/AyushModi123/yoga-class-admission-form/assets/99743679/a6e6544f-5009-4d05-9d56-1b64db38ce42)

Webpage created on streamlit-

![image](https://github.com/AyushModi123/yoga-class-admission-form/assets/99743679/2e57995e-dc00-4648-b00e-84459619b016)

