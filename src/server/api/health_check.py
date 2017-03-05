from flask_restful import Resource


class HealthCheckAPI(Resource):

    def get(self):
        return {"status": "healthy"}, 200