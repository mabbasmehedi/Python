mylist = ["apple", "banana", "cherry", "apple"]
print(mylist)
print(len(mylist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["apple", 34, True]
print(list1)
print(list2)
print(list3)
print(list4)
print(type(list1))

thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(thislist)

"""Access List Item"""
print("\nAccess List Item:")
print(thislist[1]) #first item has index 0
print(thislist[-1]) #Negative indexing means start from the end.
print(thislist[2:5]) #Return the third, fourth, and fifth item
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

"""Change List Items"""
print("\nChange List Items:")
thislist[1] = "bangi"
print(thislist)
thislist[2:5] = ["barry", "wtrmelon"]
print(thislist)
mylist.insert(2, "narikel")
print(mylist)

"""Add List Items"""
print("\nAdd List Items:")
addlist = ["apple", "banana", "cherry"]
addlist.append("orange")
print(addlist)
addlist.insert(1, "kola")
print(addlist)
#Add the elements of tropical to notlist:
notlist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
notlist.extend(tropical)
print(notlist)

"""Remove List Items"""
print("\nRemove List Items:")
alist = ["apple", "banana", "cherry"]
alist.remove("banana")
print(alist)
blist = ["apple", "banana", "cherry", "banana"]
blist.remove("banana")
print(blist)
blist.pop(1) #The pop() method removes the specified index.
print(blist)
blist.pop() #If you do not specify the index, the pop() method removes the last item.
print(blist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist

newlist = ["apple", "banana", "cherry"]
newlist.clear()
print(newlist)