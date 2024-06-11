thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple= ("apple") #not tuple
print(type(thistuple))
thistuple= ("apple",)
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

"""Access Tuple Items"""
print("\nAccess Tuple Items:")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])#start at index 2 (included) and end at index 5 (not included).
print(thistuple[:5])
print(thistuple[2:])
print(thistuple[-4:-1]) #-4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("YES")

"""Update Tuples"""
print("\nUpdate Tuples:")
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#add
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("kiwi")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple +=y
print(thistuple)

#remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#delete
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple)