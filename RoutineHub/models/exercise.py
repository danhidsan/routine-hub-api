from RoutineHub.extensions import db
from RoutineHub.commons.model import CommonModel


class Exercise(CommonModel, db.Model):
    """ Exercise model
    """

    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(280), nullable=False)
    image_url = db.Column(db.String(500))
    sets = db.Column(db.Integer)
    reps = db.Column(db.PickleType) # pickle python array with reps
    cadence = db.Column(db.Integer)
    set_seconds = db.Column(db.Integer)
    rest_seconds = db.Column(db.Integer)
    min_reps_interval = db.Column(db.Integer)
    max_reps_interval = db.Column(db.Integer)

    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, **kwargs):
        super(Exercise, self).__init__(**kwargs)

    def __repr__(self):
        return "<Exercise %s>" % self.title

