from flask import request, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_current_user

from RoutineHub.models import Workout
from RoutineHub.extensions import ma, db
from RoutineHub.commons.pagination import paginate
from RoutineHub.commons.enum import EnumField

from RoutineHub.domain.training import get_workouts, get_workout

from .exercise import ExerciseSchema

class WorkoutSchema(ma.Schema):

    id = ma.Int(dump_only=True)
    title = ma.String()
    description = ma.String()
    exercises = ma.List(ma.Nested(ExerciseSchema()))

class ScheduleSchema(ma.Schema):

    id = ma.Int(dump_only=True)
    start_date = ma.DateTime()
    end_date = ma.DateTime()
    workout = ma.Nested(WorkoutSchema())

class WorkoutResource(Resource):

    method_decorators = [jwt_required]

    def get(self, workout_id):
        schema = WorkoutSchema()
        current_user = get_current_user()
        workout = get_workout(workout_id, current_user)
        if workout is None:
            abort(404)
        return {'workout': schema.dump(workout)}


class WorkoutList(Resource):

    method_decorators = [jwt_required]

    def get(self):
        schema = ScheduleSchema(many=True)
        current_user = get_current_user()
        workouts = get_workouts(request, current_user)
        return paginate(workouts, schema)
