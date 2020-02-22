from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from RoutineHub.models import Routine
from RoutineHub.extensions import ma, db
from RoutineHub.commons.pagination import paginate
from RoutineHub.commons.enum import EnumField

class RoutineSchema(ma.ModelSchema):

    id = ma.Int(dump_only=True)
    level = EnumField(attribute="level")
    gender = EnumField(attribute="gender")
    duration_type = EnumField(attribute="duration_type")

    class Meta:
        model = Routine
        sqla_session = db.session

class RoutineResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: routine_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: RoutineSchema
        404:
          description: routine does not exists
    put:
      tags:
        - api
      parameters:
        - in: path
          name: routine_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              RoutineSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: routine updated
                  user: RoutineSchema
        404:
          description: routine does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: routine deleted
        404:
          description: routine does not exists
    """


    method_decorators = [jwt_required]

    def get(self, routine_id):
        schema = RoutineSchema()
        routine = Routine.query.get_or_404(routine_id)
        return {"routine": schema.dump(routine)}

    def put(self, routine_id):
        schema = RoutineSchema(partial=True)
        routine = Routine.query.get_or_404(routine_id)
        routine = schema.load(request.json, instance=routine)

        db.session.commit()

        return {"msg": "routine updated", "routine": schema.dump(routine)}

    def delete(self, routine_id):
        routine = Routine.query.get_or_404(routine_id)
        db.session.delete(routine)
        db.session.commit()

        return {"msg": "routine deleted"}, 204

class RoutineList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/RoutineSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              RoutineSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: routine created
                  user: RoutineSchema
    """

    method_decorators = [jwt_required]

    def get(self):
        schema = RoutineSchema(many=True)
        routine = Routine.query
        return paginate(routine, schema)

    def post(self):
        schema = RoutineSchema()
        routine = schema.load(request.json)

        db.session.add(routine)
        db.session.commit()

        return {"msg": "routine created", "routine": schema.dump(routine)}, 201

