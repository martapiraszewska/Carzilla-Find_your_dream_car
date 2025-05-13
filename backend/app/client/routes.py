from flask import Blueprint, request, jsonify
from flask_login import login_required
from models import db, Client
from typing import List
import re

clients_bp = Blueprint("clients", __name__)


@clients_bp.route("/clients", methods=["POST"])
@login_required
def create_client():
    data = request.get_json()

    required_fields = ["Name", "Surname", "Gender", "Mail", "Phone"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Walidacja Mail
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.fullmatch(email_pattern, data["Mail"]):
        return jsonify({"error": "Invalid email format"}), 400

    # Walidacja Phone
    phone_pattern = r"^\+?\d[\d\s\-]{5,20}$"
    if not re.fullmatch(phone_pattern, data["Phone"]):
        return jsonify({"error": "Invalid phone number format"}), 400

    try:
        client = Client(
            Name=data["Name"],
            Surname=data["Surname"],
            Gender=data["Gender"],
            Mail=data["Mail"],
            Phone=data["Phone"],
        )
        db.session.add(client)
        db.session.commit()

        return jsonify({"message": "Client created", "id": client.Client_ID}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add client", "details": str(e)}), 500


@clients_bp.route("/clients", methods=["GET"])
@login_required
def search_clients():
    search_fields = {
        "name": Client.Name,
        "surname": Client.Surname,
        "gender": Client.Gender,
        "mail": Client.Mail,
        "phone": Client.Phone,
    }

    query = Client.query

    for arg in request.args:
        if arg not in search_fields:
            continue
        value = request.args[arg]

        if isinstance(search_fields[arg].type, db.String):
            query = query.filter(search_fields[arg].ilike(f"%{value}%"))
        else:
            query = query.filter(search_fields[arg] == value)

    clients: List[Client] = query.all()

    return jsonify(
        [
            {
                "id": client.Client_ID,
                "name": client.Name,
                "surname": client.Surname,
                "gender": client.Gender,
                "mail": client.Mail,
                "phone": client.Phone,
            }
            for client in clients
        ]
    )


@clients_bp.route("/clients/<int:client_id>", methods=["PUT"])
@login_required
def update_client(client_id):
    data = request.get_json()
    updatable_fields = ["Name", "Surname", "Gender", "Mail", "Phone"]
    update_data = {k: data[k] for k in updatable_fields if k in data}

    if "Mail" in update_data:
        email = update_data["Mail"]
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.fullmatch(email_pattern, email):
            return jsonify({"error": "Invalid email format"}), 400

    if "Phone" in update_data:
        phone = update_data["Phone"]
        phone_pattern = r"^\+?\d[\d\s\-]{5,20}$"
        if not re.fullmatch(phone_pattern, phone):
            return jsonify({"error": "Invalid phone number format"}), 400

    try:
        result = Client.query.filter_by(Client_ID=client_id).update(update_data)
        if result == 0:
            return jsonify({"error": "Client not found"}), 404
        db.session.commit()
        return jsonify({"message": "Client updated"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@clients_bp.route("/clients/<int:client_id>", methods=["DELETE"])
@login_required
def delete_client(client_id):
    client = Client.query.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404

    try:
        db.session.delete(client)
        db.session.commit()
        return jsonify({"message": "Client deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
