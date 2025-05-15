from datetime import datetime, timezone
import sys


def get_date_or_now(date=None, format="%Y-%m-%d"):
    return (
        datetime.strptime(date, format).date()
        if date
        else datetime.now(timezone.utc).date()
    )


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def convert_case(input_string):
    parts = input_string.split("_")
    return parts[0].capitalize() + parts[1].capitalize()
