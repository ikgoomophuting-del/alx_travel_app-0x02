import requests
from django.conf import settings

CHAPA_SECRET = "CHAPA_TEST_SECRET"

def initialize_payment(reference, amount, email):
    response = requests.post(
        "https://api.chapa.co/v1/transaction/initialize",
        headers={"Authorization": f"Bearer {CHAPA_SECRET}"},
        data={
            "amount": amount,
            "currency": "ETB",
            "email": email,
            "tx_ref": reference,
            "callback_url": "http://127.0.0.1:8000/listings/verify/",
        },
    )
    return response.json()

def verify_payment(reference):
    response = requests.get(
        f"https://api.chapa.co/v1/transaction/verify/{reference}",
        headers={"Authorization": f"Bearer {CHAPA_SECRET}"},
    )
    return response.json()

