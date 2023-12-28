print(10>9)
print(10 == 10)
print(10<9)
print(bool("Hello"))
print(bool(["apple", "Cherry"]))
print(bool(10))
print(bool(0))
print(bool(""))
print(bool(False))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))

print()
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))


def myFunction():
    return True
print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print(isinstance(200, int))