"""Unpack Tuples"""
print("Unpack Tuples:")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

"""Loop Tuples"""
print("\nLoop Tuples:")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
#Print all items by referring to their index number:
print()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
print()
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1
"""Join Tuples"""
print("\nJoin Tuples:")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#multiply
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

"""Tuple Methods"""
print("\nTuple Methods:")
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

x = thistuple.index(8)
print(x)