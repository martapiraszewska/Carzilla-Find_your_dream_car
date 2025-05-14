import re
from datetime import datetime
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
            self._is_valid = False
            self._error_msg += f"Missing fields: {', '.join(missing)}. "

    def valid_phone_number(self, number):
        phone_pattern = r"^\+?\d[\d\s\-]{5,20}$"
        if not re.fullmatch(phone_pattern, number):
            self._is_valid = False
            self._error_msg += "Invalid phone number format. "

    def valid_date(self, date, format="%Y-%m-%d"):
        try:
            datetime.strptime(date, format).date()
        except ValueError:
            self._is_valid = False
            self._error_msg += "Invalid Date_of_birth format. "

    def valid_salary(self, salary, lower_bound=0, upper_bound=math.inf):
        try:
            salary = int(salary)
        except ValueError:
            self._is_valid = False
            self._error_msg += "Salary must be an integer. "
            return

        if salary < lower_bound:
            self._is_valid = False
            self._error_msg += "Salary too low. "
        if salary > upper_bound:
            self._is_valid = False
            self._error_msg += "Salary too high. "

    def valid_foreign_keys(self, data: dict):
        for field in data:
            if field.upper().endswith("ID") and not isinstance(data[field], int):
                self._is_valid = False
                self._error_msg += f"{field} must be an integer. "
