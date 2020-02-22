from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from RoutineHub.extensions import apispec
from RoutineHub.api.trainning.resources.routine import RoutineResource, RoutineList, RoutineSchema


blueprint = Blueprint("training", __name__, url_prefix="/api/training")
training = Api(blueprint)

# Routine
training.add_resource(RoutineResource, "/routine/<int:routine_id>")
training.add_resource(RoutineList, "/routine")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("RoutineSchema", schema=RoutineSchema)
    apispec.spec.path(view=RoutineResource, app=current_app)
    apispec.spec.path(view=RoutineList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400