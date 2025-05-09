from flask import Blueprint, jsonify
from flask_login import login_required, current_user

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    if current_user.role == "manager":
        return jsonify({"dashboard": "manager data"})
    return jsonify({"dashboard": "employee data"})