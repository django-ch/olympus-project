import datetime
from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from server import db
from .base import CRUD


class RunningRaceType(Enum):
    road = 0
    trail = 1
    track = 2
    xc = 3


class MeasurementPreference(Enum):
    meters = 1
    feet = 2


class Race(db.Model, CRUD):
    __tablename__ = 'races'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    name = db.Column(db.String(500))
    running_race_type = db.Column(db.Enum(RunningRaceType))
    distance = db.Column(db.Numeric(precision=3))
    start_date_local = db.Column(db.DateTime)
    city = db.Column(db.String(256))
    country = db.Column(db.String(256))
    measurement_preference = db.Column(db.Enum(MeasurementPreference))
    url = db.Column(db.String(256))
    website_url = db.Column(db.String(255))

    start_point = db.Column(Geometry('POINT'))

    routes = relationship('Route')
    race_follows = relationship('RaceFollow')

    def __repr__(self):
        return f"<Race {self.id}:{self.name!r}>"


class RaceFollow(db.Model):
    __tablename__ = 'race_follows'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    race_id = db.Column(db.Integer, ForeignKey('races.id'))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)