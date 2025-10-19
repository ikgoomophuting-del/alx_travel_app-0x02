This project extends the previous alx_travel_app_0x01 by integrating secure online payments using the Chapa API, background email notifications via Celery, and booking management through Django + GraphQL.

---
Project Overview

ALX Travel App 0x02 is a full-stack backend system that allows users to:

Browse and book travel listings

Make secure payments through Chapa

Automatically verify and update payment statuses

Receive email confirmations via Celery background tasks

Query and mutate data through a GraphQL API

---
🧩 Tech Stack
Component	Technology
Framework	Django 5.x
API Layer	Graphene-Django (GraphQL)
Payment Gateway	Chapa API
Background Tasks	Celery + Django-Celery-Results
Database	Django SQLite backend
Environment Management	python-dotenv
Testing	Django Test Framework

---
📁 Project Structure

alx_travel_app/

├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   ├── schema.py
│   ├── asgi.py
│   └── wsgi.py

├── listings/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── schema.py
│   ├── tasks.py
│   ├── tests/
│   │   ├── test_models.py
│   │   ├── test_payments.py
│   │   └── test_graphql.py
│   └── utils/
│       ├── payment_gateway.py
│       └── serializers.py
│

├── manage.py
├── requirements.txt
├── .env
└── README.md

---
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/ikgopoleng-del/alx_travel_app_0x02.git
cd alx_travel_app_0x02

2️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file in the project root (see below).

5️⃣ Run database migrations
python manage.py migrate

6️⃣ Run the server
python manage.py runserver

7️⃣ Start Celery worker
celery -A alx_travel_app worker --loglevel=info --pool=solo

---
🔐 Environment Variables

Create a .env file with the following content:

SECRET_KEY=your_django_secret_key
DEBUG=True
CHAPA_SECRET_KEY=CHAPA_TEST_SECRET
EMAIL_HOST_USER=noreply@alxtravelapp.com
EMAIL_HOST_PASSWORD=your_email_password

---
💳 Payment Flow (Chapa Integration)

User books a listing
→ Backend generates a payment request with a unique booking reference.

Initialize Payment
→ App sends POST request to Chapa API via /utils/payment_gateway.py.

Chapa returns a payment link
→ Returned to user in GraphQL mutation or REST API response.

User completes payment
→ Chapa calls back to /listings/verify/.

Verify Payment
→ The verify_payment_view() checks payment status with Chapa’s verification endpoint.

Status updated + Email sent
→ The payment’s status changes to Completed or Failed.
→ Celery asynchronously sends confirmation email.

---
🧠 GraphQL API Overview

Example mutation to initialize a payment:

mutation {
  createPayment(
    bookingReference: "BOOK123"
    amount: 2000
    email: "user@example.com"
  ) {
    payment {
      id
      bookingReference
      status
    }
    paymentUrl
  }
}


Example query to retrieve payments:

{
  payments {
    id
    bookingReference
    amount
    status
  }
}

---
📦 Celery Background Email

Celery runs asynchronously to avoid blocking the main thread when sending confirmation emails.

Example log output:

[Celery Worker] Email sent to user@example.com — Payment Completed

---
🧪 Testing
Run unit tests
python manage.py test

Example test output
Creating test database...
System check OK.
....
Ran 4 tests in 0.032s

OK

---
🌐 Deployment Readiness

✅ Secure environment variables

✅ Production-ready settings.py (DEBUG=False)

✅ Tested in Django sandbox and Chapa sandbox

---
📚 API Documentation
Endpoint	Method	Description
/graphql/	POST	GraphQL endpoint for all queries/mutations
/listings/verify/	GET	Verify payment via Chapa callback
/admin/	GET	Django admin dashboard
🏁 Acknowledgments

Special thanks to:

ALX Africa for backend development curriculum

Chapa API for providing a developer-friendly payment gateway

Django & Graphene-Django open-source communities

---
👨🏽‍💻 Author

Ikgopoleng Mophuting
Backend Developer | ALX Backend Python Track
GitHub: @ikgoomophuting-del
