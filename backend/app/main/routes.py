from flask import Blueprint, request, jsonify
from ..models import Car, Employee
from typing import List

main_bp = Blueprint("main", __name__)


@main_bp.route("/search", methods=["GET"])
def search_cars():
    # Example: /search?brand=Toyota&model=Corolla
    search_fields = {
        "brand": Car.Brand,
        "model": Car.Model,
        "color": Car.Color,
        "mileage": Car.Mileage,
        "price": Car.Price,
        "condition_ID": Car.Condition_ID,
        "dealer_ID": Car.Dealer_ID,
    }

    query = Car.query

    for arg in request.args:
        if arg not in search_fields:  # security check
            continue
        value = request.args[arg]
        query = query.filter(search_fields[arg].ilike(f"%{value}%"))

    cars: List[Car] = query.all()

    return jsonify(
        [
            {
                "id": car.Car_ID,
                "brand": car.Brand,
                "model": car.Model,
                "price": car.Price,
            }
            for car in cars
        ]
    )


@main_bp.route("/employees", methods=["GET"])
def manage_employees():
    if request.method == "GET":
        employees: List[Employee] = Employee.query.all()
        return jsonify(
            [
                {
                    "id": employee.Employee_ID,
                    "name": f"{employee.Name} {employee.Surname}",
                }
                for employee in employees
            ]
        )


@main_bp.route("/", methods=["GET"])
def main_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Button with Script</title>
    </head>
    <body>
        <button onclick="sendLoginRequest('admin')">LoginAdmin</button>
        <button onclick="sendLoginRequest('worker1')">Login</button>

        <script>
            function sendLoginRequest(login_) {
                fetch('http://127.0.0.1:5000/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'  // Ensure the correct content type
                    },
                    body: JSON.stringify({
                        login: login_,
                        password: 'temp'
                    })
                })
                .then(response => {
                    if (response.redirected) {
                        window.location.href = response.url;  // This will redirect the browser to the new URL
                    } else {
                        return response.json();  // Handle the case where no redirect occurs
                    }
                })
                .then(data => {
                    console.log(data);  // This will handle any JSON data you may want to log
                })
                .catch(error => console.error('Error:', error));
            }
        </script>
    </body>
    </html>
    """
