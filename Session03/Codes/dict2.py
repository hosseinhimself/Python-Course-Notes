car = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ['red', 'white', 'blue']
}

print(car.keys())
print(car.items())

car['doors'] = 4

print(car)

car.pop('brand')
print(car)

print(car.get('colors'))

car.clear()
print(car)

