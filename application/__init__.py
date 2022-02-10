from flask import Flask
from application.routes import tasks

def create_app():
    app = Flask(__name__)

    app.register_blueprint(tasks)
    
    return app