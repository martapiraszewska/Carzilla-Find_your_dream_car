from flask import Blueprint, request, jsonify
from flask_login import login_required
from sqlalchemy import text
from ..models import db
from datetime import datetime

invoices_bp = Blueprint("invoices", __name__)

@invoices_bp.route("/search", methods=["GET"])
def get_best_employee():
    query = text('''SELECT "Transaction"."Invoice_ID", "Transaction"."Value", CAST("Transaction"."Date" AS DATE) AS "Date", "Employee"."Name", "Employee"."Surname" FROM "Transaction"
                 JOIN "Employee"
                 ON "Employee"."Employee_ID" = "Transaction"."Employee_ID"
                 JOIN "Invoice"
                 ON "Invoice"."Invoice_ID" = "Transaction"."Invoice_ID"
                ''')
    result = db.session.execute(query)
    retv = [dict(row._mapping) for row in result]
    for emp in retv:
        emp["Name"] += ' ' + emp.pop("Surname")
        emp["Date"] = emp["Date"].strftime('%Y-%m-%d')


    if retv is None:
        return jsonify({"message": "No data for current time period"}), 204

    return jsonify(retv)

# @invoices_bp.route("/add", methods=["POST"])
# def add_invoice():
#     query = text('''
#                  ''')