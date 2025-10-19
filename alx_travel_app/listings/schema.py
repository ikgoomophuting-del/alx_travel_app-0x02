import graphene
from graphene_django import DjangoObjectType
from .models import Payment
from .utils.payment_gateway import initialize_payment

class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment

class CreatePayment(graphene.Mutation):
    class Arguments:
        booking_reference = graphene.String(required=True)
        amount = graphene.Float(required=True)
        email = graphene.String(required=True)

    payment = graphene.Field(PaymentType)
    payment_url = graphene.String()

    def mutate(self, info, booking_reference, amount, email):
        payment = Payment.objects.create(
            booking_reference=booking_reference,
            amount=amount,
        )
        response = initialize_payment(booking_reference, amount, email)
        url = response.get("data", {}).get("checkout_url")
        return CreatePayment(payment=payment, payment_url=url)

class ListingQuery(graphene.ObjectType):
    payments = graphene.List(PaymentType)

    def resolve_payments(self, info):
        return Payment.objects.all()

class PaymentMutation(graphene.ObjectType):
    create_payment = CreatePayment.Field()
      
