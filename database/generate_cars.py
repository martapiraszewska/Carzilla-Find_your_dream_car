import random

cars = {
    'Audi': ['A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q3', 'Q5', 'Q7', 'Q8', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8',
             'SQ3', 'SQ5', 'SQ8', 'RS3', 'RS4', 'RS5', 'RS6', 'RS7', 'RSQ3', 'RSQ5', 'RSQ7', 'RSQ8'],
    'BMW': ['118i', '320i', '335i', '340i', '420i', '435i', '440i', '520i', '535i', '540i', 'X1', 'X3', 'X4', 'X5', 'X6', 'X7', 'M3', 'M4', 'M5', 'M8', 'Z4'],
    'Toyota': ['Corolla', 'Camry', 'Yaris', 'RAV4', 'Land Cruiser', 'Highlander', 'Prius', 'C-HR', 'Supra'],
    'Mercedes': ['A-Class', 'C-Class', 'E-Class', 'S-Class', 'CLA', 'GLA', 'GLC', 'GLE', 'GLS', 'AMG GT'],
    'Ford': ['Fiesta', 'Focus', 'Mondeo', 'Mustang', 'Puma', 'Kuga', 'Explorer', 'Edge', 'Ranger', 'F-150'],
    'Volkswagen': ['Golf', 'Passat', 'Polo', 'Tiguan', 'Touareg', 'Arteon', 'T-Cross', 'ID.3', 'ID.4', 'ID.Buzz'],
    'Hyundai': ['i10', 'i20', 'i30', 'Kona', 'Tucson', 'Santa Fe', 'Ioniq 5', 'Ioniq 6'],
    'Kia': ['Picanto', 'Rio', 'Ceed', 'Sportage', 'Sorento', 'Stinger', 'EV6'],
    'Nissan': ['Micra', 'Qashqai', 'Juke', 'X-Trail', 'Leaf', 'Navara', 'Ariya'],
}

colors = ["White", "Black", "Blue", "Red", "Silver", "Grey", "Green", "Yellow", "Orange"]
conditions = [1, 2, 3, 4, 5]
car_dealer_ids = range(1, 16)
car_data_realistic = []

car_id = 1
for car_id in range(501):
    brand = random.choice(list(cars.keys()))
    model = random.choice(cars[brand])
    color = random.choice(colors)
    mileage = random.randint(0, 200000)
    price = round(random.uniform(5000,100000), 2)
    condition_id = random.choice(conditions)
    car_dealer_id = random.choice(car_dealer_ids)
    car_data_realistic.append(
        f"({car_id}, '{brand}', '{model}', '{color}', {mileage}, {price}, {condition_id}, {car_dealer_id}),\n"
    )
    car_id += 1

with open('cars.txt', 'w') as fh:
    for car in car_data_realistic:
        fh.write(car)
