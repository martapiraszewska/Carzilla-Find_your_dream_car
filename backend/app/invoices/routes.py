from flask import Blueprint, request, jsonify
from flask_login import login_required
from models import db, Invoice
from datetime import datetime, timezone

invoices_bp = Blueprint("invoices", __name__)


@invoices_bp.route("/invoices", methods=["POST"])
@login_required
def create_invoice():
    data = request.get_json()

    required_fields = ["Status", "NIP"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    issue_date = None
    if "Issue_date" in data:
        try:
            issue_date = datetime.strptime(data["Issue_date"], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Issue_date must be in YYYY-MM-DD format"}), 400
    else:
        issue_date = datetime.now(timezone.utc).date()

    try:
        invoice = Invoice(Status=data["Status"], NIP=data["NIP"], Issue_date=issue_date)
        db.session.add(invoice)
        db.session.commit()

        return jsonify({"message": "Invoice created", "id": invoice.Invoice_ID}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add invoice", "details": str(e)}), 500


@invoices_bp.route("/invoices", methods=["GET"])
@login_required
def search_invoices():
    search_fields = {
        "status": Invoice.Status,
        "issue_date": Invoice.Issue_date,
        "nip": Invoice.NIP,
    }

    query = Invoice.query

    for arg in request.args:
        if arg not in search_fields:
            continue
        value = request.args[arg]

        if isinstance(search_fields[arg].type, db.String):
            query = query.filter(search_fields[arg].ilike(f"%{value}%"))
        else:
            query = query.filter(search_fields[arg] == value)

    invoices = query.all()

    return jsonify(
        [
            {
                "id": inv.Invoice_ID,
                "status": inv.Status,
                "issue_date": (
                    inv.Issue_date.strftime("%Y-%m-%d") if inv.Issue_date else None
                ),
                "nip": inv.NIP,
            }
            for inv in invoices
        ]
    )


@invoices_bp.route("/invoices/<int:invoice_id>", methods=["PUT"])
@login_required
def update_invoice(invoice_id):
    data = request.get_json()
    updatable_fields = ["Status", "Issue_date", "NIP"]
    update_data = {k: data[k] for k in updatable_fields if k in data}

    if "Issue_date" in update_data:
        try:
            update_data["Issue_date"] = datetime.strptime(
                update_data["Issue_date"], "%Y-%m-%d"
            ).date()
        except ValueError:
            return jsonify({"error": "Issue_date must be in YYYY-MM-DD format"}), 400

    if "NIP" in update_data and not isinstance(update_data["NIP"], int):
        return jsonify({"error": "NIP must be an integer"}), 400

    try:
        result = Invoice.query.filter_by(Invoice_ID=invoice_id).update(update_data)
        if result == 0:
            return jsonify({"error": "Invoice not found"}), 404
        db.session.commit()
        return jsonify({"message": "Invoice updated"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@invoices_bp.route("/invoices/<int:invoice_id>", methods=["DELETE"])
@login_required
def delete_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    try:
        db.session.delete(invoice)
        db.session.commit()
        return jsonify({"message": "Invoice deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
