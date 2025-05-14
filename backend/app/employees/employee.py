from typing import Dict
from utils.validation import Valid
from utils.date import get_date_or_today
from models import db, Employee, Position, PositionHistory


class Employee_service:
    def create(data) -> Dict:
        required_fields = [
            "Name",
            "Surname",
            "Gender",
            "Date_of_birth",
            "Employee_status_ID",
            "Car_dealer_ID",
            "Login_credentials_ID",
        ]

        valid = Valid()
        valid.valid_presence(data, required_fields)
        valid.valid_date(data["Date_of_birth"])

        phone = data.get("Phone_number")
        if phone:
            valid.valid_phone_number(phone)

        salary = data.get("Salary")
        if salary:
            position = Position.query.get(data["Position_ID"])
            if not position:
                return {"error": "Invalid Position_ID"}, 400

            valid.valid_salary(salary, position.Min_salary, position.Max_salary)

        if not valid.check_validity():
            return {"error": valid.get_error_msg()}, 400

        # Tworzenie pracownika
        try:
            emp_id = Employee_service._add_employee_to_db(data, db.session)
            return {"message": "Employee created", "id": emp_id}, 201

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    def _add_employee_to_db(data, db_session):
        employee = Employee(
            Name=data["Name"],
            Surname=data["Surname"],
            Gender=data["Gender"],
            Salary=data.get("Salary"),
            Date_of_birth=data["Date_of_birth"],
            Phone_number=data.get("Phone_number"),
            Employee_status_ID=data["Employee_status_ID"],
            Car_dealer_ID=data["Car_dealer_ID"],
            Login_credentials_ID=data["Login_credentials_ID"],
        )
        db_session.add(employee)
        db_session.flush()  # potrzebne do uzyskania ID

        date_start = get_date_or_today(data.get("Date_start"))

        emp_id = employee.Employee_id

        history = PositionHistory(
            Date_start=date_start,
            Date_end=None,
            Position_ID=data["Position_ID"],
            Employee_ID=employee.Employee_ID,
        )
        db_session.add(history)
        db_session.commit()

        return emp_id
