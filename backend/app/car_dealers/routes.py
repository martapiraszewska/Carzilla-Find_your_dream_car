from flask import jsonify, Blueprint
from ..models import CarDealer
from typing import List

car_dealers_bp = Blueprint("car_dealers", __name__)


@car_dealers_bp.route("/", methods=["GET"])
def get_all():
    query = CarDealer.query
    dealers: List[CarDealer] = query.all()

    return jsonify(
        [
            {
                "Car_dealer_ID": dealer.Car_dealer_ID,
                "Name": dealer.Name,
            }
            for dealer in dealers
        ]
    )
