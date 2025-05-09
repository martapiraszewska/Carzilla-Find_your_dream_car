from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user
from ..models import Employee
from werkzeug.security import check_password_hash
from ..db import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = Employee.query.filter_by(username=data.get("username")).first()
    if user and check_password_hash(user.password, data.get("password")):
        login_user(user)
        return jsonify({"message": "Logged in", "role": user.role})
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})