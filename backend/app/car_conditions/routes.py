from flask import jsonify, Blueprint
from ..models import CarCondition
from typing import List

car_conditions_bp = Blueprint("car_conditions", __name__)


@car_conditions_bp.route("/", methods=["GET"])
def get_all():
    query = CarCondition.query
    conditions: List[CarCondition] = query.all()

    return jsonify(
        [
            {
                "Car_condition_ID": condition.Car_condition_ID,
                "Condition": condition.Condition,
            }
            for condition in conditions
        ]
    )
