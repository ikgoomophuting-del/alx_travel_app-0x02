import graphene
from listings.schema import ListingQuery, PaymentMutation

class Query(ListingQuery, graphene.ObjectType):
    pass

class Mutation(PaymentMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

