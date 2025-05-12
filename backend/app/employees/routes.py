from flask import Blueprint, request, jsonify
from flask_login import login_required
from models import db, Employee
from datetime import datetime
import re

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/employees", methods=["POST"])
@login_required
def create_employee():
    data = request.get_json()
    required_fields = [
        "Name",
        "Surname",
        "Gender",
        "Date_of_birth",
        "Employee_status_ID",
        "Car_dealer_ID",
        "Login_credentials_ID",
    ]

    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        employee = Employee(
            Name=data["Name"],
            Surname=data["Surname"],
            Gender=data["Gender"],
            Salary=data.get("Salary"),
            Date_of_birth=datetime.strptime(data["Date_of_birth"], "%Y-%m-%d"),
            Phone_number=data.get("Phone_number"),
            Employee_status_ID=data["Employee_status_ID"],
            Car_dealer_ID=data["Car_dealer_ID"],
            Login_credentials_ID=data["Login_credentials_ID"],
        )
        db.session.add(employee)
        db.session.commit()
        return jsonify({"message": "Employee created", "id": employee.Employee_ID}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@employees_bp.route("/employees/<int:employee_id>", methods=["PUT"])
@login_required
def update_employee(employee_id):
    data = request.get_json()
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

    update_data = {key: data[key] for key in updatable_fields if key in data}

    # Walidacja Salary
    if "Salary" in update_data:
        if not isinstance(update_data["Salary"], int) or update_data["Salary"] < 0:
            return jsonify({"error": "Salary must be a non-negative integer"}), 400

    # Walidacja Phone_number
    if "Phone_number" in update_data:
        phone = update_data["Phone_number"]
        phone_pattern = (
            r"^\+?\d[\d\s\-]{5,20}$"  # pozwala na: +48 123456789, 123-456-789, itp.
        )
        if not re.fullmatch(phone_pattern, phone):
            return jsonify({"error": "Invalid phone number format"}), 400

    # Walidacja pól kończących z kluczem obcym
    for field in update_data:
        if field.endswith("ID") and not isinstance(update_data[field], int):
            return jsonify({"error": f"{field} must be an integer"}), 400

    # Parsowanie daty
    if "Date_of_birth" in update_data:
        try:
            update_data["Date_of_birth"] = datetime.strptime(
                update_data["Date_of_birth"], "%Y-%m-%d"
            )
        except ValueError:
            return jsonify({"error": "Date_of_birth must be in YYYY-MM-DD format"}), 400

    try:
        result = Employee.query.filter_by(Employee_ID=employee_id).update(update_data)
        if result == 0:
            return jsonify({"error": "Employee not found"}), 404
        db.session.commit()
        return jsonify({"message": "Employee updated"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@employees_bp.route("/employees", methods=["GET"])
@login_required
def search_employees():
    search_fields = {
        "name": Employee.Name,
        "surname": Employee.Surname,
        "gender": Employee.Gender,
        "salary": Employee.Salary,
        "date_of_birth": Employee.Date_of_birth,
        "phone_number": Employee.Phone_number,
        "employee_status_id": Employee.Employee_status_ID,
        "car_dealer_id": Employee.Car_dealer_ID,
        "login_credentials_id": Employee.Login_credentials_ID,
    }

    query = Employee.query

    for arg in request.args:
        if arg not in search_fields:  # security check
            continue
        value = request.args[arg]

        # Dopasowanie do kolumny w modelu, z użyciem 'ilike' dla tekstowych pól
        if isinstance(search_fields[arg].type, db.String):  # Dla tekstowych kolumn
            query = query.filter(search_fields[arg].ilike(f"%{value}%"))
        else:  # Dla innych pól (np. liczbowych, datowych)
            query = query.filter(search_fields[arg] == value)

    # employees: List[Employee] = query.all()
    employees = query.all()

    return jsonify(
        [
            {
                "id": emp.Employee_ID,
                "name": emp.Name,
                "surname": emp.Surname,
                "gender": emp.Gender,
                "salary": emp.Salary,
                "date_of_birth": emp.Date_of_birth.strftime("%Y-%m-%d"),
                "phone_number": emp.Phone_number,
                "employee_status_id": emp.Employee_status_ID,
                "car_dealer_id": emp.Car_dealer_ID,
                "login_credentials_id": emp.Login_credentials_ID,
            }
            for emp in employees
        ]
    )


@employees_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
@login_required
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    try:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": "Employee deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
