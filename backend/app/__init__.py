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

    from .cars import cars_bp
    from .employees import employees_bp
    from .profile import profile_bp
    from .stats import stats_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(cars_bp, url_prefix="/cars")
    app.register_blueprint(employees_bp, url_prefix="/employees")
    app.register_blueprint(profile_bp, url_prefix="/profile")
    app.register_blueprint(stats_bp, url_prefix="/stats")

    return app


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))
