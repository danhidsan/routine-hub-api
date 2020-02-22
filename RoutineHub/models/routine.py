import enum
import datetime

from RoutineHub.extensions import db

class LevelEnum(enum.Enum):
    easy = 1
    medium = 2
    hard = 3

class DurationTypeEnum(enum.Enum):
    days = 1
    weeks = 2
    months = 3
    years = 4

class GenderEnum(enum.Enum):
    male = 1
    female = 2
    both = 3

class Routine(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(180), nullable=False)

    goal = db.Column(db.String(180), nullable=False)

    level = db.Column(db.Enum(LevelEnum), nullable=False)

    duration = db.Column(db.Integer, nullable=False)

    duration_type = db.Column(db.Enum(DurationTypeEnum), nullable=False)

    gender = db.Column(db.Enum(GenderEnum), nullable=False)

    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, **kwargs):
        super(Routine, self).__init__(**kwargs)

    def __repr__(self):
        return "<Routine %s>" % self.title