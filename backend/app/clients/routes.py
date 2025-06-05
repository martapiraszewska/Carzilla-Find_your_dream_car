from flask import Blueprint, request, jsonify
from flask_login import login_required
from .clients import ClientService

clients_bp = Blueprint("clients", __name__)


@clients_bp.route("/add", methods=["POST"])
@login_required
def create_client():
    required_fields = ["Name", "Surname", "Gender", "Mail", "Phone"]

    ans = ClientService.add(request.get_json(), required_fields)
    return jsonify(ans[0]), ans[1]


@clients_bp.route("/search", methods=["GET"])
# @login_required
def search_clients():
    search_fields = [
        "Client_ID",
        "Name",
        "Surname",
        "Gender",
        "Mail",
        "Phone",
    ]
    ans = ClientService.search(request.args, search_fields)
    return jsonify(ans)
