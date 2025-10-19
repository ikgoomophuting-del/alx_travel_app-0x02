
from django.test import TestCase
from listings.models import Payment

class PaymentModelTest(TestCase):
    def test_create_payment(self):
        payment = Payment.objects.create(
            booking_reference="TEST123",
            amount=200.00,
        )
        self.assertEqual(payment.status, "Pending")
