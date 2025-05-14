from flask import Blueprint, request, jsonify
from flask_login import login_required
from models import db, Employee, Position, PositionHistory
from datetime import datetime, timezone
from employee import Employee_service
import re

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/employees", methods=["POST"])
@login_required
def create_employee():
    ans = Employee_service.create(request.get_json())
    return jsonify(ans[0]), ans[1]


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

    # Walidacja daty
    if "Date_of_birth" in update_data:
        try:
            update_data["Date_of_birth"] = datetime.strptime(
                update_data["Date_of_birth"], "%Y-%m-%d"
            ).date()
        except ValueError:
            return jsonify({"error": "Invalid Date_of_birth format"}), 400

    # Walidacja telefonu
    if "Phone_number" in update_data:
        phone_pattern = r"^\+?\d[\d\s\-]{5,20}$"
        if not re.fullmatch(phone_pattern, update_data["Phone_number"]):
            return jsonify({"error": "Invalid phone number format"}), 400

    # Walidacja ID
    for field in update_data:
        if field.endswith("ID") and not isinstance(update_data[field], int):
            return jsonify({"error": f"{field} must be an integer"}), 400

    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    # Walidacja i aktualizacja pensji
    if "Salary" in update_data or "Position_ID" in data:
        salary = update_data.get("Salary", employee.Salary)
        position_id = data.get("Position_ID")

        # Pobieramy aktualne stanowisko jeśli nie podano nowego
        current_history = PositionHistory.query.filter_by(
            Employee_ID=employee_id, Date_end=None
        ).first()
        if not current_history:
            return jsonify({"error": "No active position found for employee"}), 400
        if not position_id:
            position_id = current_history.Position_ID

        position = Position.query.get(position_id)
        if not position:
            return jsonify({"error": "Invalid Position_ID"}), 400

        if not (position.Min_salary <= salary <= position.Max_salary):
            return (
                jsonify(
                    {
                        "error": f"Salary {salary} not within range {position.Min_salary}–{position.Max_salary}"
                    }
                ),
                400,
            )

    # Aktualizacja pracownika
    for k, v in update_data.items():
        setattr(employee, k, v)

    # Zmiana stanowiska?
    if "Position_ID" in data:
        # kończymy poprzedni wpis
        old_history = PositionHistory.query.filter_by(
            Employee_ID=employee_id, Date_end=None
        ).first()
        if old_history:
            old_history.Date_end = datetime.now(timezone.utc).date()

        # dodajemy nowy wpis
        date_start = (
            datetime.strptime(data.get("Date_start"), "%Y-%m-%d").date()
            if "Date_start" in data
            else datetime.now(timezone.utc).date()
        )
        new_history = PositionHistory(
            Date_start=date_start,
            Date_end=None,
            Position_ID=data["Position_ID"],
            Employee_ID=employee_id,
        )
        db.session.add(new_history)

    try:
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
        # Ustawienie daty końca na pozycji
        history = PositionHistory.query.filter_by(
            Employee_ID=employee_id, Date_end=None
        ).first()
        if history:
            history.Date_end = datetime.now(timezone.utc).date()

        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": "Employee deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
