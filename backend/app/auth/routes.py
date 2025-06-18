from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from ..models import Employee, LoginCredentials
from werkzeug.security import check_password_hash, generate_password_hash
from ..db import db


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    creds:LoginCredentials = LoginCredentials.query.filter_by(Login=data.get("username")).first()
    if creds and check_password_hash(creds.Password, data.get("password")):
        user:Employee = Employee.query.filter_by(Login_credentials_ID=creds.Login_credentials_ID).first()
        if user:
            login_user(user)
            return jsonify({"message": "Logged in", "user": user.Name}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/status', methods=['GET'])
def auth_status():
    if current_user.is_authenticated:
        return jsonify({ "authenticated": True, "user": current_user.Name }), 200
    return jsonify({ "authenticated": False }), 200

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})