from server import db
from sqlalchemy import ForeignKey

from geoalchemy2 import Geometry


class Route(db.Model):
    __tablename__ = 'routes'
    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, ForeignKey('races.id'))

    name = db.Column(db.String(500))
    description = db.Column(db.String)
    elevation_gain = db.Column(db.Numeric(precision=3))
    geom = db.Column(Geometry('GEOMETRY'))
