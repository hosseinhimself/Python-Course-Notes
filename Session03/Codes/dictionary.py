a = dict()
a = {}

car = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ['red', 'white', 'blue']
}


print(car['brand'])
print(car["colors"])
print()
dic2 = car
dic2['brand'] = 'Benz'

print(dic2)
print(car)
print()
dic2 = car.copy()
dic2['brand'] = 'Ford'

print(dic2)
print(car)

