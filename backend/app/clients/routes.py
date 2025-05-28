from flask import Blueprint, request, jsonify
from flask_login import login_required
from models import db, Client
from typing import List
from .clients import ClientService
import re

clients_bp = Blueprint("clients", __name__)


@clients_bp.route("/clients", methods=["POST"])
# @login_required
def create_client():
    required_fields = ["Name", "Surname", "Gender", "Mail", "Phone"]

    ans = ClientService.add(request.get_json(), required_fields)
    return jsonify(ans[0]), ans[1]


# @clients_bp.route("/clients", methods=["GET"])
# @login_required
# def search_clients():
#     search_fields = {
#         "name": Client.Name,
#         "surname": Client.Surname,
#         "gender": Client.Gender,
#         "mail": Client.Mail,
#         "phone": Client.Phone,
#     }

#     query = Client.query

#     for arg in request.args:
#         if arg not in search_fields:
#             continue
#         value = request.args[arg]

#         if isinstance(search_fields[arg].type, db.String):
#             query = query.filter(search_fields[arg].ilike(f"%{value}%"))
#         else:
#             query = query.filter(search_fields[arg] == value)

#     clients: List[Client] = query.all()

#     return jsonify(
#         [
#             {
#                 "id": client.Client_ID,
#                 "name": client.Name,
#                 "surname": client.Surname,
#                 "gender": client.Gender,
#                 "mail": client.Mail,
#                 "phone": client.Phone,
#             }
#             for client in clients
#         ]
#     )
