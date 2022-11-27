import pandas as pd
from flask import Blueprint, jsonify, render_template, request

from app.models.models import User
from swagger_stack.swagger_initialize import SwaggerConfig
from flask_restx import Resource

api_bp = Blueprint('api_bp', __name__, url_prefix='/v1')
name_space = SwaggerConfig.name_space


@api_bp.route('/test_hello_world')
def hello_world():
    return 'hello world'


@api_bp.route('/upload_option', methods=['GET'])
def upload_option():
    return render_template('uploader.html')


@api_bp.route('/uploader', methods=['POST'])
def upload_link():
    file = request.files['file']
    df = pd.read_excel(file)
    for idx, rows in df.iterrows():
        name = rows.get('name')
        if len(User.by_name(name)) == 0:
            user = User()
            user.name = name
            user.save_me()
        else:
            continue
    return 'uploaded and saved'


@api_bp.route('/get_in_table', methods=['GET'])
def get_all():
    response = User.get_all()
    json_data = [{'id': x.id, 'nameeeee':x.name} for x in response]
    print(json_data)
    return render_template('table.html', items=json_data)




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
