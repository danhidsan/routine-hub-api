from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from RoutineHub.extensions import apispec
from RoutineHub.api.schedule.resources import ScheduleResource, ScheduleSchema


blueprint = Blueprint("schedule", __name__, url_prefix="/api/schedule")
schedule = Api(blueprint)

# schedule
schedule.add_resource(ScheduleResource, "/<int:schedule_id>")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("ScheduleSchema", schema=ScheduleSchema)
    apispec.spec.path(view=ScheduleResource, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400