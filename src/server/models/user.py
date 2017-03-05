import datetime

import pytz
from sqlalchemy.orm import relationship

from server import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_login = db.Column(db.DateTime)
    timezone = db.Column(db.String(255))
    is_active = db.Column(db.Boolean())
    is_superuser = db.Column(db.Boolean())

    created_races = relationship('Race')
    race_follows = relationship('RaceFollow')
