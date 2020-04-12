from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_current_user

from RoutineHub.models import Workout
from RoutineHub.extensions import ma, db
from RoutineHub.commons.pagination import paginate
from RoutineHub.commons.enum import EnumField

from RoutineHub.domain.training import get_workouts

class WorkoutSchema(ma.Schema):

    id = ma.Int(dump_only=True)
    title = ma.String()
    description = ma.String()

class ScheduleSchema(ma.Schema):

    id = ma.Int(dump_only=True)
    start_date = ma.DateTime()
    end_date = ma.DateTime()
    workout = ma.Nested(WorkoutSchema())

class WorkoutList(Resource):

    method_decorators = [jwt_required]

    def get(self):
        schema = ScheduleSchema(many=True)
        current_user = get_current_user()
        routine = get_workouts(request, current_user)
        return paginate(routine, schema)
