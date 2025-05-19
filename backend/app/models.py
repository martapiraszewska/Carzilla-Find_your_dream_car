from .db import db
from flask_login import UserMixin


class CarCondition(db.Model):
    __tablename__ = "Car_condition"
    Car_condition_ID = db.Column(db.Integer, primary_key=True)
    Condition = db.Column(db.String, nullable=False)


class CarDealer(db.Model):
    __tablename__ = "Car_dealer"
    Car_dealer_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Address_ID = db.Column(
        db.Integer, db.ForeignKey("Address.Address_ID"), nullable=False
    )


class Address(db.Model):
    __tablename__ = "Address"
    Address_ID = db.Column(db.Integer, primary_key=True)
    Postcode = db.Column(db.String, nullable=False)
    Street = db.Column(db.String, nullable=False)
    Street_number = db.Column(db.Integer, nullable=False)
    City_ID = db.Column(db.Integer, db.ForeignKey("City.City_ID"), nullable=False)


class City(db.Model):
    __tablename__ = "City"
    City_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Country = db.Column(db.String, nullable=False)


class Car(db.Model):
    __tablename__ = "Car"
    Car_ID = db.Column(db.Integer, primary_key=True)
    Brand = db.Column(db.String, nullable=False)
    Model = db.Column(db.String, nullable=False)
    Color = db.Column(db.String, nullable=False)
    Mileage = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Car_condition_ID = db.Column(
        db.Integer, db.ForeignKey("Car_condition.Car_condition_ID"), nullable=False
    )
    Car_dealer_ID = db.Column(
        db.Integer, db.ForeignKey("Car_dealer.Car_dealer_ID"), nullable=False
    )


class Client(db.Model):
    __tablename__ = "Client"
    Client_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Surname = db.Column(db.String, nullable=False)
    Gender = db.Column(db.String, nullable=False)
    Mail = db.Column(db.String, nullable=False)
    Phone = db.Column(db.String, nullable=False)


class EmployeeStatus(db.Model):
    __tablename__ = "Employee_status"
    Employee_status_ID = db.Column(db.Integer, primary_key=True)
    Status_name = db.Column(db.String, nullable=False)


class LoginCredentials(db.Model):
    __tablename__ = "Login_credentials"
    Login_credentials_ID = db.Column(db.Integer, primary_key=True)
    Login = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)


class Employee(UserMixin, db.Model):
    __tablename__ = "Employee"
    Employee_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Surname = db.Column(db.String, nullable=False)
    Gender = db.Column(db.String, nullable=False)
    Salary = db.Column(db.Integer)
    Date_of_birth = db.Column(db.Date, nullable=False)
    Phone_number = db.Column(db.String)
    Employee_status_ID = db.Column(
        db.Integer, db.ForeignKey("Employee_status.Employee_status_ID"), nullable=False
    )
    Car_dealer_ID = db.Column(
        db.Integer, db.ForeignKey("Car_dealer.Car_dealer_ID"), nullable=False
    )
    Login_credentials_ID = db.Column(
        db.Integer,
        db.ForeignKey("Login_credentials.Login_credentials_ID"),
        nullable=False,
    )

    # flask_login
    def get_id(self):
        return int(self.Employee_ID)


class Position(db.Model):
    __tablename__ = "Position"
    Position_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Min_salary = db.Column(db.Integer)
    Max_salary = db.Column(db.Integer)


class PositionHistory(db.Model):
    __tablename__ = "Position_history"
    Position_history_ID = db.Column(db.Integer, primary_key=True)
    Date_start = db.Column(db.Date, nullable=False)
    Date_end = db.Column(db.Date)
    Position_ID = db.Column(
        db.Integer, db.ForeignKey("Position.Position_ID"), nullable=False
    )
    Employee_ID = db.Column(
        db.Integer, db.ForeignKey("Employee.Employee_ID"), nullable=False
    )


class TransactionType(db.Model):
    __tablename__ = "Transaction_type"
    Transaction_type_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)


class Invoice(db.Model):
    __tablename__ = "Invoice"
    Invoice_ID = db.Column(db.Integer, primary_key=True)
    Status = db.Column(db.String, nullable=False)
    Issue_date = db.Column(db.Date)
    NIP = db.Column(db.Integer, nullable=False)


class Transaction(db.Model):
    __tablename__ = "Transaction"
    Transaction_ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Value = db.Column(db.Integer, nullable=False)
    Client_ID = db.Column(db.Integer, db.ForeignKey("Client.Client_ID"), nullable=False)
    Employee_ID = db.Column(
        db.Integer, db.ForeignKey("Employee.Employee_ID"), nullable=False
    )
    Transaction_type_ID = db.Column(
        db.Integer,
        db.ForeignKey("Transaction_type.Transaction_type_ID"),
        nullable=False,
    )
    Invoice_ID = db.Column(db.Integer, db.ForeignKey("Invoice.Invoice_ID"), unique=True)


class EmployeeStats(db.Model):
    __tablename__ = "Employee_stats"
    Year = db.Column(db.Integer, primary_key=True)
    Month = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(
        db.Integer, db.ForeignKey("Employee.Employee_ID"), primary_key=True
    )
    Sales_sum = db.Column(db.Integer, nullable=False)
