from RoutineHub.extensions import db


exercise_workout = db.Table('exercise_workout',
    db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True),
    db.PrimaryKeyConstraint('workout_id', 'exercise_id')
)