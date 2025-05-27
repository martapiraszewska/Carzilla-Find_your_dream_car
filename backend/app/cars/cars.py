from typing import List
from ..utils.validation import Valid
from ..models import db, Car, CarCondition, CarDealer


class CarService:
    def add(data, required_fields):
        valid = Valid()
        valid.valid_presence(data, required_fields)
        valid.valid_number_positive(data["Mileage"])
        valid.valid_number_positive(data["Price"])
        if isinstance(data["Car_dealer_ID"], str):
            data["Car_dealer_ID"] = get_car_dealer_id_by_name(data["Car_dealer_ID"])
        if isinstance(data["Car_condition_ID"], str):
            data["Car_condition_ID"] = get_car_condition_id_by_name(
                data["Car_condition_ID"]
            )
        valid.valid_foreign_keys(data)

        if not valid.check_validity():
            return {"error": valid.get_error_msg()}, 400

        try:
            car_id = CarService._add_car_to_db(data, db.session)

            return (
                {"message": "Car added successfully", "car_id": car_id},
                201,
            )

        except Exception as e:
            db.session.rollback()
            return {"error": "Failed to add car", "details": str(e)}, 500

    def remove(car_id):
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Car not found"}, 404

        try:
            db.session.delete(car)
            db.session.commit()
            return {"message": f"Car {car_id} deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": "Failed to delete car", "details": str(e)}, 500

    def update(car_id, data, updatable_fields):
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Employee not found"}, 404

        update_data = {
            field: data[field] for field in updatable_fields if field in data
        }

        if not update_data:
            return {"error": "No valid fields to update"}, 400

        valid = Valid()
        if data["Mileage"]:
            valid.valid_number_positive(data["Mileage"])
        if data["Price"]:
            valid.valid_number_positive(data["Price"])
        valid.valid_foreign_keys(data)

        if not valid.check_validity():
            return {"error": valid.get_error_msg()}, 400

        try:
            result = Car.query.filter_by(Car_ID=car_id).update(update_data)
            if result == 0:
                return {"error": "Car not found"}, 404

            db.session.commit()
            return {"message": f"Car {car_id} updated successfully"}, 200

        except Exception as e:
            db.session.rollback()
            return {"error": "Failed to update car", "details": str(e)}, 500

    def search(criteria, search_fields):
        query = Car.query

        for arg in criteria:
            # print(arg, criteria[arg])
            if arg not in search_fields:  # security check
                continue
            value = criteria[arg]
            if isinstance(getattr(Car, arg).type, db.String):  # Dla tekstowych kolumn
                query = query.filter(getattr(Car, arg).ilike(f"%{value}%"))
            else:  # Dla innych pól (np. liczbowych, datowych)
                query = query.filter(getattr(Car, arg) == value)

        cars: List[Car] = query.all()

        return [
            {
                "Car_ID": car.Car_ID,
                "Brand": car.Brand,
                "Model": car.Model,
                "Color": car.Color,
                "Mileage": car.Mileage,
                "Price": car.Price,
                "Car_condition_ID": car.Car_condition_ID,
                "Car_dealer_ID": car.Car_dealer_ID,
            }
            for car in cars
        ]

    def _add_car_to_db(data, db_session):
        new_car = Car(
            Brand=data["Brand"],
            Model=data["Model"],
            Color=data["Color"],
            Mileage=int(data["Mileage"]),
            Price=int(data["Price"]),
            Condition_ID=int(data["Condition_ID"]),
            Dealer_ID=int(data["Dealer_ID"]),
        )

        db_session.add(new_car)
        db_session.commit()

        return new_car.Car_ID


def get_car_dealer_id_by_name(name):
    dealer_entry = CarDealer.query.filter_by(Name=name).first()
    if not dealer_entry:
        raise Exception("Car dealer name does not correspond to any car dealer entry")

    return dealer_entry.Car_dealer_ID


def get_car_condition_id_by_name(name):
    condition_entry = CarCondition.query.filter_by(Condition=name).first()
    if not condition_entry:
        raise Exception(
            "Car condition name does not correspond to any car condition entry"
        )

    return condition_entry.Car_condition_ID
