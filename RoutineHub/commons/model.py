import datetime

from RoutineHub.extensions import db


class CommonModel():

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    deleted = db.Column(db.Boolean, default=False)
