from RoutineHub.extensions import db
from RoutineHub.commons.model import CommonModel

class Schedule(CommonModel, db.Model):

    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime, nullable=True)

    # Relationships
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Schedule {self.start_date}-{self.end_date}>"
