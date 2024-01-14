"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
fruits.clear()
print(fruits)
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
fruits = ['apple', 'banana', 'cherry', 'orange', 'cherry']
x = fruits.count("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
x = cars.index("BMW")
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
fruits.pop(0)
print(fruits)
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

