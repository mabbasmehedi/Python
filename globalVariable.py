x = 'awesome'

def myfunc():
    print("Python is " +x)
myfunc()

def myfunc():
    x = "fantastic" #local variable
    print("Python is " +x)
myfunc()

print("Python is " +x)

def myfunc():
    global x  
    """global keyword create global
    variable inside function and/or
    change value of existing global variaible"""
    x = "fantastic"
myfunc()

print("Python is " +x)
