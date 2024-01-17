"""Sets"""
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #dupli not allow
#True and 1 or False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", True,False, 0, 1, 2}
print(thisset)
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
set1 = {"abc", 34, True, 40, "male"}
print(thisset)
thisset = {"apple", "banana", "cherry"}
print(type(thisset))
thisset = set(("apple", "banana", "cherry"))
print(thisset)

"""Access Set Items"""
print("\nAccess Set Items:")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

"""Add Set Items"""
print("\nAdd Set Items:")
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset )
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)
#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

"""Loop Items"""
print("\nLoop Items:")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

"""Join Sets"""
print("\nJoin Sets:")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = { 1, 2, 3}
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)