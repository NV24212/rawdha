from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    with app.app_context():
        from . import routes
        from . import database
        database.init_app(app)

    return app
