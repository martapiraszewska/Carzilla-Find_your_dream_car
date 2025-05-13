from flask import request, jsonify, Blueprint
from flask_login import login_required
from models import Car, db
from typing import Dict

cars_bp = Blueprint("cars", __name__)


@cars_bp.route("/cars", methods=["POST"])
@login_required
def add_car():
    data: Dict = request.get_json()

    required_fields = [
        "Brand",
        "Model",
        "Color",
        "Mileage",
        "Price",
        "Condition_ID",
        "Dealer_ID",
    ]
    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        new_car = Car(
            Brand=data["Brand"],
            Model=data["Model"],
            Color=data["Color"],
            Mileage=int(data["Mileage"]),
            Price=int(data["Price"]),
            Condition_ID=int(data["Condition_ID"]),
            Dealer_ID=int(data["Dealer_ID"]),
        )

        db.session.add(new_car)
        db.session.commit()

        return (
            jsonify({"message": "Car added successfully", "car_id": new_car.Car_ID}),
            201,
        )

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add car", "details": str(e)}), 500


@cars_bp.route("/cars/<int:car_id>", methods=["DELETE"])
@login_required
def delete_car(car_id):
    car = Car.query.get(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    try:
        db.session.delete(car)
        db.session.commit()
        return jsonify({"message": f"Car {car_id} deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to delete car", "details": str(e)}), 500


@cars_bp.route("/cars/<int:car_id>", methods=["PUT"])
@login_required
def update_car(car_id):
    data = request.get_json()
    updatable_fields = [
        "Brand",
        "Model",
        "Color",
        "Mileage",
        "Price",
        "Condition_ID",
        "Dealer_ID",
    ]
    update_data = {field: data[field] for field in updatable_fields if field in data}

    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    try:
        result = Car.query.filter_by(Car_ID=car_id).update(update_data)
        if result == 0:
            return jsonify({"error": "Car not found"}), 404

        db.session.commit()
        return jsonify({"message": f"Car {car_id} updated successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update car", "details": str(e)}), 500
