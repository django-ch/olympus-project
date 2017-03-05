from flask_restful import Resource, marshal_with

from marshmallow_jsonapi import Schema, fields
from marshmallow import validate


from server.models.race import Race
from server import db


race_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'running_race_type': fields.Integer,
    'distance': fields.Float,
    'city': fields.String,
    'country': fields.String,
    'url': fields.String,
}

class RaceSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    running_race_type = fields.Integer()
    distance = fields.Decimal()
    city = fields.String()
    country = fields.String()
    url = fields.String()

    class Meta:
        type_ = 'race'


race_schema = RaceSchema()

def race_serializer(instance):
    return race_schema.dump(instance).data

def race_deserializer(data):
    return race_schema.load(data).data

class RaceAPI(Resource):

    def get(self):
        races = db.session.query(Race).all()
        results = race_schema.dump(races, many=True).data
        return results