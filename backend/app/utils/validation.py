import re
from datetime import datetime
from .other import str_to_class, convert_case
import math


class Valid:
    def __init__(self):
        self._error_msg = ""
        self._is_valid = True

    def check_validity(self):
        return self._is_valid

    def get_error_msg(self):
        return self._error_msg

    def valid_presence(self, data: dict, required_fields: list):
        missing = [field for field in required_fields if field not in data]
        if missing:
            self._add_error(f"Missing fields: {', '.join(missing)}. ")

    def valid_phone_number(self, number):
        phone_pattern = r"^\+?\d[\d\s\-]{5,20}$"
        if not re.fullmatch(phone_pattern, number):
            self._add_error("Invalid phone number format. ")

    def valid_email(self, email):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.fullmatch(email_pattern, email):
            self._add_error("Invalid email format. ")

    def valid_date(self, date, format="%Y-%m-%d"):
        try:
            datetime.strptime(date, format).date()
        except ValueError:
            self._add_error("Invalid Date_of_birth format. ")

    def valid_salary(self, salary, lower_bound=0, upper_bound=math.inf):
        try:
            salary = int(salary)
        except ValueError:
            self._add_error("Salary must be an integer. ")
            return
        
        if salary < lower_bound:
            self._add_error("Salary too low. ")
        if salary > upper_bound:
            self._add_error("Salary too high. ")

    def valid_number_positive(self, number):
        try:
            number = int(number)
            if number < 0:
                self._add_error("Number should not be negative. ")
        except ValueError:
            self._add_error("Number is not an integer. ")

    def valid_foreign_keys(self, data: dict):
        for field in data:
            if not field.endswith("_ID"):
                continue
            
            try:
                data[field] = int(data[field])
            except Exception:
                continue

            if not isinstance(data[field], int):
                self._add_error(f"{field} must be an integer. ")
                continue

            try:
                model_class_name = str_to_class(convert_case(field[:-3]))
            except Exception:
                self._add_error(f"{field} does not refer to any table. ")
                continue

            id_found = False
            for entry in model_class_name.query.all():
                if getattr(entry, field) == data[field]:
                    id_found = True

            if not id_found:
                self._add_error(
                    f"{model_class_name} does not contain ID={data[field]}. "
                )

    def _add_error(self, msg):
        self._is_valid = False
        self._error_msg += msg
