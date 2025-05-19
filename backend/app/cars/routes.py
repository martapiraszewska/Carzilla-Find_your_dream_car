from flask import request, jsonify, Blueprint
from flask_login import login_required
from .cars import CarService

cars_bp = Blueprint("cars", __name__)


@cars_bp.route("/", methods=["POST"])
def add_car():
    required_fields = [
        "Brand",
        "Model",
        "Color",
        "Mileage",
        "Price",
        "Car_condition_ID",
        "Car_dealer_ID",
    ]
    ans = CarService.add(request.get_json(), required_fields)
    return jsonify(ans[0]), ans[1]


@cars_bp.route("/<int:car_id>", methods=["DELETE"])
@login_required
def delete_car(car_id):
    ans = CarService.add(car_id)
    return jsonify(ans[0]), ans[1]


@cars_bp.route("/<int:car_id>", methods=["PUT"])
@login_required
def update_car(car_id):
    updatable_fields = [
        "Brand",
        "Model",
        "Color",
        "Mileage",
        "Price",
        "Car_condition_ID",
        "Car_dealer_ID",
    ]
    ans = CarService.update(car_id, request.get_json(), updatable_fields)
    return jsonify(ans[0]), ans[1]


@cars_bp.route("/", methods=["GET"])
def search_car():
    # Example: /cars?brand=Toyota&model=Corolla
    search_fields = [
        "Brand",
        "Model",
        "Color",
        "Mileage",
        "Price",
        "Car_condition_ID",
        "Car_dealer_ID",
    ]

    criteria = request.args
    ans = CarService.search(criteria, search_fields)
    return jsonify(ans)
