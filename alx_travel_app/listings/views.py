from django.http import JsonResponse
from .models import Payment
from .tasks import send_payment_confirmation_email
from .utils.payment_gateway import verify_payment

def verify_payment_view(request):
    reference = request.GET.get("tx_ref")
    email = request.GET.get("email", "user@example.com")

    payment = Payment.objects.filter(booking_reference=reference).first()
    if not payment:
        return JsonResponse({"error": "Payment not found"}, status=404)

    response_data = verify_payment(reference)
    status = response_data.get("data", {}).get("status", "failed")

    payment.status = "Completed" if status == "success" else "Failed"
    payment.save()

    send_payment_confirmation_email.delay(email, reference, payment.amount, payment.status)
    return JsonResponse({"status": payment.status})
