from flask import Blueprint, request, jsonify
from flask_login import login_required
from sqlalchemy import text
from ..models import db, Transaction

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/", methods=["GET"])
def get_profile():
    query = text('SELECT COUNT("Transaction"."Value") AS "carsSold", SUM("Transaction"."Value") AS "profit" FROM "Transaction";')
    result = db.session.execute(query)
    sold_profit = [dict(row._mapping) for row in result]
    query = text('SELECT COUNT(*) FROM "Car_dealer"')
    result = db.session.execute(query)
    dealers = [dict(row._mapping) for row in result]
    retv = {**sold_profit[0], **dealers[0]} #combine dicts
    retv_json = jsonify(retv)
    return retv_json