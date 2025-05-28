from typing import List
from ..utils.validation import Valid
from ..models import db, Client


class ClientService:
    def add(data, required_fields):
        valid = Valid()
        valid.valid_presence(data, required_fields)
        valid.valid_phone_number(data["Phone"])
        valid.valid_email(data["Email"])
        valid.valid_foreign_keys(data)

        if not valid.check_validity():
            return {"error": valid.get_error_msg()}, 400

        try:
            client_id = ClientService._add_client_to_db(data, db.session)

            return (
                {"message": "Client added successfully", "client_id": client_id},
                201,
            )

        except Exception as e:
            db.session.rollback()
            return {"error": "Failed to add client", "details": str(e)}, 500

    def _add_client_to_db(data, db_session):
        new_client = Client(
            Name=data["Name"],
            Surname=data["Surname"],
            Gender=data["Gender"],
            Email=data["Email"],
            Phone=data["Phone"],
        )
        db_session.add(new_client)
        db_session.commit()
        return new_client.Client_ID
