from flask_restx import Api


class SwaggerConfig:
    name_space = None

    @classmethod
    def initialize(cls, app):
        api = Api(app)
        cls.name_space = api.namespace('Test Swagger', description='Test Swagger')