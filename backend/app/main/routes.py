from flask import Blueprint, request, jsonify
from ..models import Car

main_bp = Blueprint("main", __name__)

@main_bp.route("/search", methods=["GET"])
def search_cars():
    # Example: /search?make=Toyota&available=true
    filters = {}
    if "make" in request.args:
        filters["make"] = request.args["make"]
    if "available" in request.args:
        filters["available"] = request.args["available"].lower() == "true"
    cars = Car.query.filter_by(**filters).all()
    return jsonify([{
        "id": car.id,
        "make": car.make,
        "model": car.model,
        "year": car.year,
        "price": car.price
    } for car in cars])

@main_bp.route("/", methods=["GET"])
def main_page():
    return jsonify("HOME PAGE")
