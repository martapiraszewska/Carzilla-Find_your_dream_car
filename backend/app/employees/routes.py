from flask import Blueprint, request, jsonify
from flask_login import login_required
from ..models import Employee
from .employee import EmployeeService
from sqlalchemy import text
from ..models import db

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/add", methods=["POST"])
# @login_required
def create_employee():
    required_fields = [
        "Name",
        "Surname",
        "Gender",
        "Date_of_birth",
        "Employee_status_ID",
        "Car_dealer_ID",
    ]  # there are also other non-obligatory fields that you can add like salary
    # you can reference to ID fields also by giving name of desired field; it will autoconvert to ID
    print(request.get_json())
    ans = EmployeeService.create(request.get_json(), required_fields)
    return jsonify(ans[0]), ans[1]


@employees_bp.route("/update/<int:employee_id>", methods=["PUT"])
@login_required
def update_employee(employee_id):
    updatable_fields = [
        "Name",
        "Surname",
        "Gender",
        "Salary",
        "Date_of_birth",
        "Phone_number",
        "Employee_status_ID",
        "Car_dealer_ID",
        "Login_credentials_ID",
    ]
    ans = EmployeeService.update(employee_id, request.get_json(), updatable_fields)
    return jsonify(ans[0]), ans[1]


@employees_bp.route("/remove/<int:employee_id>", methods=["DELETE"])
# @login_required
def delete_employee(employee_id):
    # ans = EmployeeService.delete(employee_id)
    # return jsonify(ans[0]), ans[1]
    query = text('''UPDATE "Employee"
                    SET "Employee_status_ID" = 2
                    WHERE "Employee_ID" = :id
                ''')
    try:
        result = db.session.execute(query, {"id": employee_id})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"message": "ERROR while firing employee", "error": str(e)}, 400
    
    if result.rowcount == 0:
        return {"message": "Employee not found"}, 404

    return {"message": "Employee fired"}, 200


@employees_bp.route("/search", methods=["GET"])
# @login_required
def search_employees():
    search_fields = {
        "Employee_ID": Employee.Employee_ID,
        "Name": Employee.Name,
        "Surname": Employee.Surname,
        "Gender": Employee.Gender,
        "Salary": Employee.Salary,
        "Date_of_birth": Employee.Date_of_birth,
        "Phone_number": Employee.Phone_number,
        "Employee_status_id": Employee.Employee_status_ID,
        "Car_dealer_id": Employee.Car_dealer_ID,
        "Login_credentials_id": Employee.Login_credentials_ID,
    }
    ans = EmployeeService.search(request.args, search_fields)
    ans = [emp for emp in ans if emp.get("Status_name") == "Active"]
    return jsonify(ans)
    # query = text('''SELECT "Employee".* FROM "Employee"
    #                 JOIN "Employee_status"
    #                 ON "Employee"."Employee_status_ID" = "Employee_status"."Employee_status_ID"
    #                 JOIN "Pos
    #                 WHERE "Employee_status"."Status_name" = 'Active'
    #             ''')
    # result = db.session.execute(query)
    # rows = result.fetchall()
    # data = [dict(row._mapping) for row in rows]
    # return jsonify(data)
