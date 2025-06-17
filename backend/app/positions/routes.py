from flask import jsonify, Blueprint
from ..models import Position
from typing import List

positions_bp = Blueprint("positions", __name__)


@positions_bp.route("/", methods=["GET"])
def get_all():
    query = Position.query
    positions: List[Position] = query.all()

    return jsonify(
        [
            {
                "Position_ID": position.Position_ID,
                "Position_name": position.Name,
            }
            for position in positions
        ]
    )
