from flask import Blueprint, request, jsonify
from flask_login import login_required
from ..models import Employee
from .employee import EmployeeService

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/", methods=["POST"])
@login_required
def create_employee():
    required_fields = [
        "Name",
        "Surname",
        "Gender",
        "Date_of_birth",
        "Employee_status_ID",
        "Car_dealer_ID",
        "Login_credentials_ID",
    ]  # there are also other non-obligatory fields that you can add
    ans = EmployeeService.create(request.get_json(), required_fields)
    return jsonify(ans[0]), ans[1]


@employees_bp.route("/<int:employee_id>", methods=["PUT"])
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


@employees_bp.route("/<int:employee_id>", methods=["DELETE"])
@login_required
def delete_employee(employee_id):
    ans = EmployeeService.delete(employee_id)
    return jsonify(ans[0]), ans[1]


@employees_bp.route("/", methods=["GET"])
@login_required
def search_employees():
    search_fields = {
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
    return jsonify(ans)
