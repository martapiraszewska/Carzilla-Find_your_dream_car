from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, current_user
from ..models import Employee, LoginCredentials
from werkzeug.security import check_password_hash, generate_password_hash
from ..db import db


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    print(data)
    creds:LoginCredentials = LoginCredentials.query.filter_by(Login=data.get("login")).first()
    if creds and check_password_hash(creds.Password, data.get("password")):
    # if creds and creds.Password == data.get("password"):  # temporary!!
        user:Employee = Employee.query.filter_by(Login_credentials_ID=creds.Login_credentials_ID).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard.dashboard'))
            return jsonify({"message": "Logged in", "Name": user.Name})
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})