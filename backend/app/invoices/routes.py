from flask import Blueprint, request, jsonify
from flask_login import login_required
from sqlalchemy import text
from ..models import db, Invoice, Transaction
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

@invoices_bp.route("/add", methods=["POST"])
def add_invoice():
    
    data = request.get_json()
    emp_id = data.get("employee")
    client_id = data.get("client")
    value = data.get("amount")
    nip = data.get("nip")

    new_invoice = Invoice(
        Status='Issued',
        Issue_date=datetime.now(),
        NIP=nip)
    
    db.session.add(new_invoice)
    db.session.commit()
    invoice_id = new_invoice.Invoice_ID

    new_transaction = Transaction(
        Date=datetime.now(),
        Value=value,
        Client_ID=client_id,
        Employee_ID=emp_id,
        Transaction_type_ID=1,
        Invoice_ID=invoice_id
    )

    db.session.add(new_transaction)
    db.session.commit()
    transaction_id = new_transaction.Transaction_ID

    return jsonify({"message": "Added Transaction + Invoice Succesfuly"}), 200

    # query = text('''INSERT INTO "Invoice" ("Status", "Issue_date", "NIP")
    #                 VALUES ('Issued', ':date', :nip);
    #              ''')
    
    # result = db.session.execute(query, {"date": datetime.now(), "nip": nip})
    # db.session.commit()    

    # query = text('''INSERT INTO "Transaction" ("Date", "Value", "Client_ID", "Employee_ID", "Transaction_type_ID", "Invoice_ID")
    #                 VALUES (:date, :value, :client_id, :emp_id, 1, :invoice_id);
    #              ''')