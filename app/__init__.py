from flask import Flask
from app.routes.auth import auth_bp
from app.routes.groups import groups_bp
from app.routes.tasks import tasks_bp
from app.services.database import initialize_db

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'your-mongodb-uri'
    initialize_db(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(groups_bp, url_prefix='/groups')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    return app
