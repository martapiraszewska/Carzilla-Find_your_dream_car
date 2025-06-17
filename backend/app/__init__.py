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
    from .car_conditions import car_conditions_bp
    from .car_dealers import car_dealers_bp
    from .employees import employees_bp
    from .employee_status import employee_status_bp
    from .clients import clients_bp
    from .profile import profile_bp
    from .positions import positions_bp
    from .stats import stats_bp
    from .invoices import invoices_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(cars_bp, url_prefix="/cars")
    app.register_blueprint(car_conditions_bp, url_prefix="/car_conditions")
    app.register_blueprint(car_dealers_bp, url_prefix="/car_dealers")
    app.register_blueprint(employees_bp, url_prefix="/employees")
    app.register_blueprint(employee_status_bp, url_prefix="/employee_status")
    app.register_blueprint(clients_bp, url_prefix="/clients")
    app.register_blueprint(profile_bp, url_prefix="/profile")
    app.register_blueprint(positions_bp, url_prefix="/positions")
    app.register_blueprint(stats_bp, url_prefix="/stats")
    app.register_blueprint(invoices_bp, url_prefix="/invoices")

    return app


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))
