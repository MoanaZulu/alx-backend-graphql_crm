import graphene

class Query(graphene.ObjectType):
    dummy = graphene.String()

    def resolve_dummy(root, info):
        return "CRM dummy field"
