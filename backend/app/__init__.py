from flask import Flask
from .config import Config
from .db import db
from flask_login import LoginManager
from .models import Employee

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth_bp
    from .main import main_bp
    from .dashboard import dashboard_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

    return app

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))