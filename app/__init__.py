from flask import Flask
from config import Config
from flask_cors import CORS
from app.models import SQLAConfig
from swagger_stack.swagger_initialize import SwaggerConfig


class AppFactory:

    @classmethod
    def initialize(cls):
        try:
            app = Flask(__name__)
            config = Config()
            CORS(app)
            SwaggerConfig.initialize(app)

            from app.api.api import api_bp
            app.register_blueprint(api_bp)

            SQLAConfig.initialize()
            with app.app_context():
                pass

            return app

        except Exception as e:
            print(e)
