from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from RoutineHub.extensions import apispec
from RoutineHub.api.user.resources import UserResource, UserList
from RoutineHub.api.user.resources.user import UserSchema


blueprint = Blueprint("api", __name__, url_prefix="/api/user")
user = Api(blueprint)


# User
user.add_resource(UserResource, "/<int:user_id>")
user.add_resource(UserList, "/")

# Routine



@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
