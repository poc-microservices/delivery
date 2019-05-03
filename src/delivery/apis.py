from flask_restful import Resource
from core import api


class DeliveryResource(Resource):
    """
    Delivery root API
    """
    def get(self):
        return "Delivery Service - Hello world."
    
    def post(self):
        return "Delivery Service - Hello Knative Eventing."

api.add_resource(DeliveryResource, '/')
