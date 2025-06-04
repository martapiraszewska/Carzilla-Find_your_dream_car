from flask import Blueprint, request, jsonify
from flask_login import login_required
from sqlalchemy import text
from ..models import db
from datetime import datetime

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/employee_of_month/search", methods=["GET"])
def get_best_employee():
    current_month = 1 #datetime.now().month
    current_year = 2024 #datetime.now().year
    query = text('''SELECT "Employee"."Employee_ID", "Employee"."Name", "Employee"."Surname", "Position"."Name" "Position", "Employee_stats"."Sales_sum"
                    FROM "Employee"
                    JOIN "Employee_stats"
                    ON "Employee"."Employee_ID" = "Employee_stats"."Employee_ID"
                    JOIN "Position_history"
                    ON "Employee"."Employee_ID" = "Position_history"."Employee_ID"
                    JOIN "Position"
                    ON "Position_history"."Position_ID" = "Position"."Position_ID"
                    JOIN "Transaction"
                    ON "Employee"."Employee_ID" = "Transaction"."Employee_ID"
                    WHERE "Employee_stats"."Month" = :month
                    AND "Employee_stats"."Year" = :year
                    /*
                    AND EXTRACT(MONTH FROM "Transaction"."Date") = :month
                    AND EXTRACT(YEAR FROM "Transaction"."Date") = :year
                    GROUP BY "Employee"."Employee_ID", EXTRACT(MONTH FROM "Transaction"."Date"), EXTRACT(YEAR FROM "Transaction"."Date")
                    */
                    ORDER BY "Employee_stats"."Sales_sum" DESC, "Position_history"."Date_start" DESC
                    FETCH FIRST 1 ROWS ONLY
                ''')
    result = db.session.execute(query, {"month": 1, "year": 2024})  # TODO: use datetime.now().year and datetime.now().month, no data for current time period
    row = result.fetchone()  # Gets the first row as a Row object

    if row is None:
        return jsonify({"message": "No data for current time period"}), 204

    employee_data = {
        "Employee_ID": row.Employee_ID,
        "Name": row.Name,
        "Surname": row.Surname,
        "Position": row.Position,
        "Sales": row.Sales_sum
    }

    return jsonify(employee_data)