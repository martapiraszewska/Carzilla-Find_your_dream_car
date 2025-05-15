from utils.validation import Valid
from utils.other import get_date_or_now
from models import db, Employee, Position, PositionHistory


class EmployeeService:
    def create(data, required_fields):
        valid = Valid()
        valid.valid_presence(data, required_fields)
        valid.valid_date(data["Date_of_birth"])
        valid.valid_foreign_keys(required_fields)

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
            emp_id = EmployeeService._add_employee_to_db(data, db.session)
            return {"message": "Employee created", "id": emp_id}, 201

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    def update(employee_id, data, updatable_fields):
        employee = Employee.query.get(employee_id)
        if not employee:
            return {"error": "Employee not found"}, 404

        update_data = {key: data[key] for key in updatable_fields if key in data}

        if not update_data:
            return {"error": "No valid fields to update"}, 400

        valid = Valid()
        if "Date_of_birth" in update_data:
            valid.valid_date(data["Date_of_birth"])

        phone = data.get("Phone_number")
        if phone:
            valid.valid_phone_number(phone)

        valid.valid_foreign_keys(update_data)

        # Walidacja i aktualizacja pensji
        if "Salary" in update_data or "Position_ID" in data:
            try:
                position = EmployeeService._get_position_of_employee(employee_id, data)
                if not position:
                    return {"error": "Invalid Position_ID"}, 400
            except Exception:
                return {"error": "No active position found for employee"}, 400

            salary = update_data.get("Salary", employee.Salary)
            valid.valid_salary(salary, position.Min_salary, position.Max_salary)

        if not valid.check_validity():
            return {"error": valid.get_error_msg()}, 400

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
                old_history.Date_end = get_date_or_now()

            # dodajemy nowy wpis
            date_start = get_date_or_now(data.get("Date_start"))
            new_history = PositionHistory(
                Date_start=date_start,
                Date_end=None,
                Position_ID=data["Position_ID"],
                Employee_ID=employee_id,
            )
            db.session.add(new_history)

        try:
            db.session.commit()
            return {"message": "Employee updated"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    def search(args, search_fields):
        query = Employee.query

        for arg in args:
            if arg not in search_fields:  # security check
                continue
            value = args[arg]

            # Dopasowanie do kolumny w modelu, z użyciem 'ilike' dla tekstowych pól
            if isinstance(search_fields[arg].type, db.String):  # Dla tekstowych kolumn
                query = query.filter(search_fields[arg].ilike(f"%{value}%"))
            else:  # Dla innych pól (np. liczbowych, datowych)
                query = query.filter(search_fields[arg] == value)

        # employees: List[Employee] = query.all()
        employees = query.all()

        return [
            {
                "Employee_ID": emp.Employee_ID,
                "Name": emp.Name,
                "Surname": emp.Surname,
                "Gender": emp.Gender,
                "Salary": emp.Salary,
                "Date_of_birth": emp.Date_of_birth.strftime("%Y-%m-%d"),
                "Phone_number": emp.Phone_number,
                "Employee_status_ID": emp.Employee_status_ID,
                "Car_dealer_ID": emp.Car_dealer_ID,
                "Login_credentials_ID": emp.Login_credentials_ID,
            }
            for emp in employees
        ]

    def delete(employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return {"error": "Employee not found"}, 404

        try:
            # Ustawienie daty końca na pozycji
            history = PositionHistory.query.filter_by(
                Employee_ID=employee_id, Date_end=None
            ).first()
            if history:
                history.Date_end = get_date_or_now()

            db.session.delete(employee)
            db.session.commit()
            return {"message": "Employee deleted"}, 200
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

        date_start = get_date_or_now(data.get("Date_start"))

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

    def _get_position_of_employee(employee_id, data):
        # Pobieramy aktualne stanowisko jeśli nie podano nowego
        current_history = PositionHistory.query.filter_by(
            Employee_ID=employee_id, Date_end=None
        ).first()
        if not current_history:
            raise Exception("No active position found for employee")

        position_id = data.get("Position_ID", current_history.Position_ID)

        return Position.query.get(position_id)
