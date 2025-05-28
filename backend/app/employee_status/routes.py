from flask import jsonify, Blueprint
from ..models import EmployeeStatus
from typing import List

employee_status_bp = Blueprint("employee_status", __name__)


@employee_status_bp.route("/", methods=["GET"])
def get_all():
    query = EmployeeStatus.query
    statuses: List[EmployeeStatus] = query.all()

    return jsonify(
        [
            {
                "Employee_status_ID": status.Employee_status_ID,
                "Status_name": status.Status_name,
            }
            for status in statuses
        ]
    )
