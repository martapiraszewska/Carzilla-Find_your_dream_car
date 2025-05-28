from typing import List
from ..utils.validation import Valid
from ..models import db, Client


class ClientService:
    def add(data, required_fields):
        valid = Valid()
        valid.valid_presence(data, required_fields)
        valid.valid_phone_number(data["Phone"])
        valid.valid_email(data["Mail"])
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

    def search_clients(data, search_fields):
        query = Client.query

        for arg in data:
            if arg not in search_fields:  # security check
                continue
            value = data[arg]
            if isinstance(
                getattr(Client, arg).type, db.String
            ):  # Dla tekstowych kolumn
                query = query.filter(getattr(Client, arg).ilike(f"%{value}%"))
            else:  # Dla innych pól (np. liczbowych, datowych)
                query = query.filter(getattr(Client, arg) == value)

        clients: List[Client] = query.all()

        return [
            {
                "Client_ID": client.Client_ID,
                "Name": client.Name,
                "Surname": client.Surname,
                "Gender": client.Gender,
                "Phone": client.Phone,
                "Mail": client.Mail,
            }
            for client in clients
        ]

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
