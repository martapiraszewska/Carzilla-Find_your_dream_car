import random
import string
import json
from werkzeug.security import generate_password_hash

cars_nb = 600
car_dealers_nb = 30
clients_nb = 100
employees_nb = 100

with open("./database/seed_data.json", "r") as fh:
    data = json.load(fh)

cars = data["cars"]
colors = data["colors"]
car_conditions = data["car_conditions"]
car_dealers = data["car_dealers"]
names = data["names"]
mail_domains = data["mail_domains"]
employee_status = data["employee_status"]
position_names = data["position_names"]
transaction_types = data["transaction_types"]
invoice_status = data["invoice_status"]
cities = data["cities"]
streets = data["streets"]

address_ids = list(range(1, car_dealers_nb + 1))
cities_list = [city for countries in cities.values() for city in countries]


def generate_cars():
    car_table = ""
    for car_id in range(1, cars_nb + 1):
        brand = random.choice(list(cars.keys()))
        model = random.choice(cars[brand])
        color = random.choice(colors)
        mileage = random.randint(0, 200000)
        price = round(random.uniform(5000, 100000), 2)
        condition_id = random.randint(1, len(car_conditions))
        car_dealer_id = random.randint(1, car_dealers_nb)
        car_table += (
            "INSERT INTO \"Car\" (\"Car_ID\", \"Brand\", \"Model\", \"Color\","
            " \"Mileage\", \"Price\", \"Car_condition_ID\", \"Car_dealer_ID\")"
            f" VALUES ({car_id}, '{brand}', '{model}', '{color}', {mileage}, "
            f"{price}, {condition_id}, {car_dealer_id});\n"
        )
    return car_table


def generate_car_conditions():
    car_condition_table = ""
    for id, condition in enumerate(car_conditions):
        car_condition_table += (
            "INSERT INTO \"Car_condition\" (\"Car_condition_ID\", "
            f"\"Condition\") VALUES ({id + 1}, '{condition}');\n"
        )
    return car_condition_table


def generate_car_dealers():
    car_dealer_table = ""
    for car_dealer_id in range(1, car_dealers_nb + 1):
        name = random.choice(car_dealers)
        car_dealers.remove(name)
        address_id = random.choice(address_ids)
        address_ids.remove(address_id)
        car_dealer_table += (
            "INSERT INTO \"Car_dealer\" (\"Car_dealer_ID\", \"Name\", "
            f"\"Address_ID\") VALUES ({car_dealer_id}, '{name}', "
            f"{address_id});\n"
        )
    return car_dealer_table


def generate_cities():
    city_table = ""
    id = 1
    for country, city_list in cities.items():
        for city in city_list:
            city_table += (
                "INSERT INTO \"City\" (\"City_ID\", \"Name\", \"Country\") "
                f"VALUES ({id}, '{city}', '{country}');\n"
            )
            id += 1
    return city_table


def generate_addressses():
    address_table = ""
    for address_id in range(1, car_dealers_nb + 1):
        postcode = random.choices(string.digits, k=5)
        postcode = ''.join(postcode)
        cities_keys = list(cities.keys())
        country = random.choice(cities_keys)
        city = random.choice(cities[country])
        street = random.choice(streets[city])
        street_nb = random.randint(1, 99)
        city_id = cities_list.index(city) + 1
        address_table += (
            "INSERT INTO \"Address\" (\"Address_ID\", \"Postcode\", \"Street\""
            f", \"Street_number\", \"City_ID\") VALUES ({address_id}, "
            f"'{postcode}', '{street}', {street_nb}, {city_id});\n"
        )
    return address_table


def generate_clients():
    client_table = ""
    for client_id in range(1, clients_nb + 1):
        gender = random.choice(["M", "F"])
        full_name = random.choice(names[gender])
        names[gender].remove(full_name)
        name, surname = full_name.split()
        domain = random.choice(mail_domains)
        mail = name + "." + surname + "@" + domain + ".com"
        phone = random.randint(100000000, 999999999)
        client_table += (
            "INSERT INTO \"Client\" (\"Client_ID\", \"Name\", \"Surname\", "
            f"\"Gender\", \"Mail\", \"Phone\") VALUES ({client_id}, '{name}', "
            f"'{surname}', '{gender}', '{mail}', '{phone}');\n"
        )
    return client_table


def generate_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    if month == 2:
        day = random.randint(1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)
    return (year, month, day)


def generate_tables():
    employee_table = ""
    transaction_table = ""
    invoice_table = ""
    position_history_table = ""
    login_credentials_table = ""
    curr_transaction_id = 1
    for employee_id in range(1, employees_nb + 1):
        employee_table += generate_employee(employee_id)
        year_start, month_start, day_start = generate_date(2013, 2023)
        date_start = (year_start, month_start, day_start)
        position_history_table += generate_pos_history(employee_id, date_start)
        login_credentials_table += generate_login_credentials(employee_id)
        transaction_nb = random.randint(1, 5)
        for id in range(transaction_nb):
            transaction_id = id + curr_transaction_id
            transaction, invoice = generate_transaction_and_invoice(
                transaction_id, employee_id, year_start)
            transaction_table += transaction
            invoice_table += invoice
        curr_transaction_id += transaction_nb
    return (employee_table, transaction_table, invoice_table,
            position_history_table, login_credentials_table)


def generate_employee(id):
    gender = random.choice(["M", "F"])
    full_name = random.choice(names[gender])
    names[gender].remove(full_name)
    name, surname = full_name.split()
    salary = "NULL"
    year, month, day = generate_date(1956, 2006)
    phone = random.randint(100000000, 999999999)
    status_id = random.randint(1, len(employee_status))
    car_dealer_id = random.randint(1, car_dealers_nb)
    employee = (
        "INSERT INTO \"Employee\" (\"Employee_ID\", \"Name\", \"Surname\", "
        "\"Gender\", \"Salary\", \"Date_of_birth\", \"Phone_number\", "
        "\"Employee_status_ID\", \"Car_dealer_ID\", \"Login_credentials_ID"
        f"\") VALUES ({id}, '{name}', '{surname}', '{gender}', {salary}, "
        f"'{year}-{month:02}-{day:02}', '{phone}', {status_id}, "
        f"{car_dealer_id}, {id});\n"
    )
    return employee


def generate_transaction_and_invoice(id, employee_id, year_start):
    year, month, day = generate_date(year_start + 1, 2024)
    value = round(random.uniform(5000, 100000), 2)
    client_id = random.randint(1, clients_nb)
    transaction_type_id = random.randint(1, len(transaction_types))
    transaction = (
        "INSERT INTO \"Transaction\" (\"Transaction_ID\", \"Date\", \""
        "Value\", \"Client_ID\", \"Employee_ID\", \"Transaction_type_ID\","
        f" \"Invoice_ID\") VALUES ({id}, '{year}-{month:02}-"
        f"{day:02}', {value}, {client_id}, {employee_id}, "
        f"{transaction_type_id}, {id});\n"
    )
    invoice = (generate_invoice(id, year, month, day))
    return transaction, invoice


def generate_invoice(id, year, month, day):
    status = random.choice(invoice_status)
    first_digit = random.choice(string.digits[1:])
    other_digits = random.choices(string.digits, k=9)
    nip = first_digit + ''.join(other_digits)
    invoice = "INSERT INTO \"Invoice\" (\"Invoice_ID\", \"Status\", "
    invoice += f"\"Issue_date\", \"NIP\") VALUES ({id}, '{status}', "
    invoice += f"'{year}-{month:02}-{day:02}', {nip});\n"
    return invoice


def generate_employee_status():
    employee_status_table = ""
    for id, status in enumerate(employee_status):
        employee_status_table += (
            "INSERT INTO \"Employee_status\" (\"Employee_status_ID\", "
            f"\"Status_name\") VALUES ({id + 1}, '{status}');\n"
        )
    return employee_status_table


def generate_positions():
    position_table = ""
    for id, name in enumerate(position_names):
        min_salary = random.randint(4000, 16000)
        max_salary = random.randint(min_salary, 20000)
        position_table += (
            "INSERT INTO \"Position\" (\"Position_ID\", \"Name\", "
            f"\"Min_salary\", \"Max_salary\") VALUES ({id + 1}, '{name}', "
            f"{min_salary}, {max_salary});\n"
        )
    return position_table


def generate_transaction_type():
    transaction_type_table = ""
    for id, type in enumerate(transaction_types):
        transaction_type_table += (
            "INSERT INTO \"Transaction_type\" (\"Transaction_type_ID\", "
            f"\"Name\") VALUES ({id + 1}, '{type}');\n"
        )
    return transaction_type_table


def generate_pos_history(id, date_start):
    year, month, day = date_start
    date_end = "NULL"
    position_id = random.randint(1, len(position_names))
    position_history = (
        "INSERT INTO \"Position_history\" (\"Position_history_ID\", "
        "\"Date_start\", \"Date_end\", \"Position_ID\", \"Employee_ID\") "
        f"VALUES ({id}, '{year}-{month:02}-{day:02}', {date_end}, "
        f"{position_id}, {id});\n"
    )
    return position_history


def generate_login_credentials(id):
    login_length = random.randint(5, 10)
    login = random.choices(string.ascii_letters, k=login_length)
    login = ''.join(login)
    password = generate_password_hash("password", method='scrypt',
                                      salt_length=16)
    login_credentials = (
        "INSERT INTO \"Login_credentials\" (\"Login_credentials_ID\","
        f" \"Login\", \"Password\") VALUES ({id}, '{login}', "
        f"'{password}');\n"
    )
    return login_credentials


if __name__ == "__main__":
    with open('./database/seed_data.sql', 'w') as fh:
        fh.write(generate_cities())
        fh.write(generate_addressses())
        fh.write(generate_car_conditions())
        fh.write(generate_car_dealers())
        fh.write(generate_employee_status())
        fh.write(generate_positions())
        tables = generate_tables()
        employees, transactions, invoices, pos_history, log_cred = tables
        fh.write(log_cred)
        fh.write(employees)
        fh.write(generate_clients())
        fh.write(generate_transaction_type())
        fh.write(invoices)
        fh.write(transactions)
        fh.write(generate_cars())
        fh.write(pos_history)
