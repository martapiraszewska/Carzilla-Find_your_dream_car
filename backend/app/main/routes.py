from flask import Blueprint, request, jsonify
from ..models import Car
from typing import List

main_bp = Blueprint("main", __name__)

@main_bp.route("/search", methods=["GET"])
def search_cars():
    # Example: /search?brand=Toyota
    filters = {}

    print(request.args)
    if "brand" in request.args:
        filters["Brand"] = request.args["brand"]
    cars:List[Car] = Car.query.filter_by(**filters).all()
    print(cars)
    return jsonify([{
        "id": car.Car_ID,
        "brand": car.Brand,
        "model": car.Model,
        "price": car.Price
    } for car in cars])

@main_bp.route("/status", methods=["GET"])
def main_page():
    return jsonify("PING PONG")
