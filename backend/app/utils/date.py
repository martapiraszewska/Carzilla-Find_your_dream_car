from datetime import datetime, timezone


def get_date_or_today(date, format="%Y-%m-%d"):
    return (
        datetime.strptime(date, format).date()
        if date
        else datetime.now(timezone.utc).date()
    )
