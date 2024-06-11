a = "hello"
print(a)

b = """tesffhr djfklajfl dlfjla 
fjlajflajfal  faljfklajf lfjklfaja
jflajfaa; aflafajlfa; """
print(b)

a = "Hello World"
print(a[1])
print()
for x in "banana":
    print(x)

#langth
print(len(a))

#chk string
name = "Mahmud Abbas Mehedi"
print("Mehedi" in name)
if "Mehedi" in name:
    print("Yes, 'Mehedi' is present")
#if not
print("Mahi" not in name)
if "Mahi" not in name:
    print("NO, 'Mahi' is not present")

#sliking
    print(a[2:5])
#Slice from start
    print(a[:5])
#slice to end
    print(a[6:])
#Negative Indexing
    print(a[-5:-2])

#Upper Case
    print(a.upper())
#Lower Case
    print(a.lower())

#Remove Whitespace
a1 = " Hello, World "
print(a.strip())

#replace
print(a.replace("H", "J"))
#split
print(a1.split(","))

#String Concatenation
x = "Hello"
y = "World"
z = x + y
z1 = x + " " + y #add space
print(z)
print(z1)

"""Format"""
age = 21
txt = "I am Mehedi, I am {}"
print(txt.format(age))
quantity = 4
item = "Chips"
price = 40.0
txt2 = "I bought {} pack of item {} for {} taka"
print(txt2.format(quantity,item,price))
#can use index number for correct place start frm 0
txt2 = "I paid {2} taka for {0} pices of item {1}"
print(txt2.format(quantity,item,price))

'''Escape Characters'''
print('it\'s single qoute')
print("This insert one \\ backslash")
print("This is \nNew line")

print("ai paart koi\rCarriage Return")
print("aiyoo \t tab dekhi")
print("jodi \f dei taile ki Form Feed hoy?")

txt = "\110\145\154\154\157"  #\ooo	Octal value
print(txt) 

txt2 = "\x48\x65\x6c\x6c\x6f"  #\xhh	Hex value
print(txt2) 



