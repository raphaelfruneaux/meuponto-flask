from flask import Blueprint
from flask_restful import Api, Resource

from datetime import datetime


app = Blueprint('api-healthcheck', __name__)
api = Api(app, prefix='/healthcheck')


class HealthCheck(Resource):
    def get(self):
        return {
            "status": True,
            "now": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


api.add_resource(HealthCheck, '')
