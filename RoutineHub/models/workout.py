from RoutineHub.extensions import db
from RoutineHub.commons.model import CommonModel
from RoutineHub.models.relations import exercise_workout


class Workout(CommonModel, db.Model):
    """ Workout model
    """
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(280))

    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    schedules = db.relationship('Schedule', backref='workout', lazy=True)
    exercises = db.relationship('Exercise', secondary=exercise_workout, backref='workout')

    def __init__(self, **kwargs):
        super(Workout, self).__init__(**kwargs)

    def __repr__(self):
        return "<Workout %s>" % self.title
