from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    if current_user.Employee_ID == 1:
        return jsonify({"dashboard": "admin data"})
    return jsonify({"dashboard": "worker data"})
