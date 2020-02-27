from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from RoutineHub.models import Schedule
from RoutineHub.extensions import ma, db
from RoutineHub.commons.pagination import paginate
from RoutineHub.commons.enum import EnumField


class ScheduleSchema(ma.ModelSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Schedule
        sqla_session = db.session


class ScheduleResource(Resource):

    def put(self, schedule_id):
        schema = ScheduleSchema(partial=True)
        schedule = Schedule.query.get_or_404(schedule_id)
        schedule = schema.load(request.json, instance=schedule)

        db.session.commit()
        return {"msg": "schedule updated", "schedule": schema.dump(schedule)}

    def delete(self, schedule_id):
        schedule = Schedule.query.get_or_404(schedule_id)
        schedule.deleted = True
        db.session.commit()
        return {"msg": "schedule deleted"}
