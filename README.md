# Carzilla - find your dream car
Jakub Bagiński, Michał Bloch, Bartosz Mączka, Aleksander Paliwoda, Marta Piraszewska

## About the Project
Carzilla is a web application designed to manage a car dealership network. It supports employee management, invoice processing, vehicle searching, and business analytics such as sales statistics, employee performance, and revenue tracking.

## Features
- Public car search without authentication
- Employee and manager roles
- Invoice creation and management
- Employee hiring and dismissal (manager only)
- Vehicle database management
- Business statistics and reporting
- CRUD operations for dealership data

## Running the Application
The project uses Docker and Docker Compose for easy deployment.

Start the application with:  
`docker-compose up`

To run it in the background:  
`docker-compose up -d`

## Technologies
- **Docker & Docker Compose** – containerization and deployment
- **PostgreSQL** – containerization and deployment
- **Python Flask** – backend REST API
- **React** – frontend
