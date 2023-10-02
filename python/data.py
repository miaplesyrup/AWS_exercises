import csv
import copy

"""
Output:
[
    {
        "vin": "TMX20122",
        "make": "AnyCompany Motors",
        "model": "Coupe",
        "year": 2012,
        "range": 335,
        "topSpeed": 155,
        "zeroSixty": 4.1,
        "mileage": 50000
    },
    ...
]
"""

pattern = {
    "vin": "",
    "make": "",
    "model": "",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

cars = []

with open('car_fleet.csv') as file:
    reader = csv.reader(file, delimiter=',')
    
    for row in list(reader)[1:]:
        element = copy.deepcopy(pattern)
        element['vin'] = row[0]
        element['make'] = row[1]
        element['model'] = row[2]
        element['year'] = row[3]
        element['range'] = row[4]
        element['topSpeed'] = row[5]
        element['zeroSixty'] = row[6]
        element['mileage'] = row[7]
        cars.append(element)

print(cars)