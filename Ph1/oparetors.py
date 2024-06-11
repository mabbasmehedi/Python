"""Arithmatic"""
print(5+3)
print(5-2)
print(5*2)
print(6/2)
print(5%2) #Modulus
print(5 ** 2) #Exponentiation
print(15//2) #Floor division

"""Assignment"""
print("\nAssignment Oparetor:")
x = 5
print(x)
x +=3 #x = x+3
print(x)
x=5
x -=3 #x = x-3
print(x)
x=5
x -= 3	#x = x - 3
print(x)
x=5
x *= 3	#x = x * 3
print(x)
x=5
x /= 3	#x = x / 3
print(x)
x=5
x %= 3	#x = x % 3
print(x)
x=5
x //= 3	#x = x // 3
print(x)
x=5
x **= 3	#x = x ** 3
print(x)
x=5
x &= 3	#x = x & 3
print(x)
x=5
x |= 3	#x = x | 3
print(x)
x=5
x ^= 3	#x = x ^ 3
print(x)
x=5
x >>= 3	#x = x >> 3
print(x)
x=5
x <<= 3	#x = x << 3
print(x)

"""Comparisn"""
print("Comparison:")
x = 7
y = 5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

"""Logical"""
print("\nLogical:")
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))

"""Identity"""
print("\nIdentity:")
print(x is y)
print(x is not y)

"""Membership"""
print("\nMembership:")
a = ["Apple", "Banana"]
print("Apple" in a)
print("Litchi" in a)

"""Bitwise"""
print("\nBitwise")
x = 6
y = 3
print(x & y)
print(x | y)
print(x ^ y)
print (~x)
print (x << 2)
print (x >> 2)

"""Precedence"""
print("\nPrecedence")
print((x +y)*(x - y))
print(100-3**3)
print (100 + ~3)
