x = 1  
y = 2.8  
z = 1j   
print(type(x))
print(type(y))
print(type(z))
#Float can also be scientific numbers with an "e" to indicate the power of 10.
t = 35e3 #35*10^3
print(t)
print(type(t))

u = 5j
print(type(u))
print('hehe')
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

#convert from float to complex:
d = complex(y)

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

import random
print(random.randrange(1, 10))