from flask import Blueprint, jsonify

from app.models.models import User
from swagger_stack.swagger_initialize import SwaggerConfig
from flask_restx import Resource

api_bp = Blueprint('api_bp', __name__, url_prefix='/v1')
name_space = SwaggerConfig.name_space


@api_bp.route('/test_hello_world')
def hello_world():
    return 'hello world'


@name_space.route('/test_swagger')
class TestSwagger(Resource):
    def get(self):
        return 'hello world this is swagger'


@name_space.route('/status')
class InvalidTest(Resource):
    def post(self):
        try:
            id = 1
            ent = User.by_id(id)
            return {'name': ent.name}
        except Exception as e:
            return jsonify(e)

    def get(self):
        try:
            name = 'Charles Oneal'
            ents = User.by_name(name)
            ent = ents[0]
            return {'name': ent.name}
        except Exception as e:
            return jsonify(e)
