import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple hello world field")

    def resolve_hello(root, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)



import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple hello world field")

    def resolve_hello(root, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)


import graphene
from crm_module.schema import Query as CRMQuery  # adjust if your app is named differently

class Query(CRMQuery, graphene.ObjectType):
    # You can still add extra fields here if needed
    hello = graphene.String(description="A simple hello world field")

    def resolve_hello(root, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)


import graphene
from crm.schema import Query as CRMQuery

class Query(CRMQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
