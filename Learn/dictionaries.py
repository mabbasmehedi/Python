thisdict = {"brand": "Ford",
            "model":"Mustang", 
            "year": 1964}
print(thisdict)

print(thisdict["brand"])

thisdict = {"brand": "Ford",
            "model":"Mustang", 
            "year": 1964,
            "year": 2201}
print(thisdict)

print(len(thisdict))

thisdict = {"brand": "Ford",
            "electronic": False,
            "year": 1964,
            "colors": ["red", "while", "blue"]
            }
print(thisdict)

thisdict = {"brand": "Ford",
            "model":"Mustang", 
            "year": 1964}
print(type(thisdict))

thisdict = dict(name = "John", age = 35, country = "Norway")
print(thisdict)

"""Accessing Items"""
print("\nAccessing Items:")

thisdict = {"brand": "Ford",
            "model":"Mustang", 
            "year": 1964}
x  = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)
car["color"] = "White"
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

car["color"] = "red"
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

car["color"] = "red"
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in car:
    print("yes")
    

