'''String Mathods'''
print("SL-1:")
print("hello".capitalize()) #Converts the first character to upper case
print("SL-2:")
print("SUIIII".casefold()) #Converts string into lower case
print("SL-3:")
print("Hello".center(20)) #Returns a centered string
print("SL-4:")
print("Deluluuu".count("u")) #Returns the number of times a specified value occurs in a string
print("SL-5:")
print("chatgpt".encode("utf-8")) #Returns an encoded version of the string
print("SL-6:")
print("Hello World".endswith("World")) #Returns True if the string ends with the specified value
print("SL-7:")
print("Ikram\tBhai".expandtabs(20)) #Sets the tab size of the string
print("SL-8:")
print("Khuj the search".find("search")) #earches the string for a specified value and returns the position of where it was found
print("SL-9:")
print("Hello, {}!".format("Peter")) #Formats specified values in a string
print("SL-10:")
print("Hello, {name}".format_map({"name":"Parkar"})) #Formats specified values in a string using a mapping
print("SL-11:")
print("Help Mee".index("Mee")) #Searches the string for a specified value and returns the position of where it was found, raising an exception if not found
print("SL-12:")
print("Suiiii007".isalnum()) #Returns True if all characters in the string are alphanumeric
print("SL-13:")
print("Leo".isalpha()) #Returns True if all characters in the string are in the alphabet
print("SL-14:")
print("iShowSpeed".isascii()) #Returns True if all characters in the string are ASCII characters
print("SL-15:")
print("123".isdecimal()) #Returns True if all characters in the string are decimals
print("SL-16:")
print("123".isdigit()) #Returns True if all characters in the string are digits
print("SL-17:")
print("Joy_Bangla".isidentifier()) #Returns True if the string is a valid identifier
print("SL-18:")
print("hello".islower()) #Returns True if all characters in the string are lower case
print("SL-19:")
print("12345".isnumeric()) #Returns True if all characters in the string are numeric (includes digits, decimals, and other numeric characters)
print("SL-20:")
print("Is printable?".isprintable()) #Returns True if all characters in the string are printable
print("SL-21:")
print(" ".isspace()) #Returns True if all characters in the string are whitespaces
print("SL-22:")
print("Not A Title".istitle()) #Returns True if the string follows the rules of a title
print("SL-23:")
print("LOWER".isupper()) #Returns True if all characters in the string are upper case
print("SL-24:")
print("-".join(["Can't", "Join"])) #Returns True if all characters in the string are upper case
print("SL-25:")
print("Lorem".ljust(10)) #Returns a left justified version of the string
print("SL-26:")
print("UPPER".lower()) #Converts a string into lower case
print("SL-27:")
print("     Bam pash faka".lstrip()) #Returns a left trim version of the string
print("SL-28:")
mytable=str.maketrans("B", "V")
print(mytable)
print("Rubber Bird".translate(mytable))     #Returns a translation table to be used in translations
print("SL-29:")
print("Tube Light".partition(" ")) #Returns a tuple where the string is parted into three parts
print("SL-30:")
print("Lorem".replace("o","*"))
print("SL-31:")
print("Hello world".find("o")) #Searches the string for a specified value and returns the first position of where it was found
print("SL-32:")
print("Hello World".rindex("o")) #Searches the string for a specified value and returns the last position of where it was found
print("SL-33:")
print("Retake".rjust(10)) #Returns a right justified version of the string
print("SL-34:")
print("Adolf Hitler".rpartition(" ")) #Returns a tuple where the string is parted into three parts
print("SL-35:")
print("Hello, How are you?".rsplit(",")) #Splits the string at the specified separator, and returns a list
print("SL-36:")
print("  Dan bamer space nai  ".strip()) #Returns a right trim version of the string
print("SL-37:")
print("Live\nfrom\ncontrol\nroom".splitlines()) #Splits the string at line breaks and returns a list
print("SL-38:")
print("Taka naii".startswith("Taka")) #Returns true if the string starts with the specified value
print("SL-39:")
print("PenalDo PesSi".swapcase()) #Swaps cases, lower case becomes upper case and vice versa
print("SL-40:")
print("maybe title".title()) #Converts the first character of each word to upper case
print("SL-41:")
print("Rubber Bird".translate({66: 86}))
print("SL-42:")
print("lower".upper()) #Converts a string into upper case
print("SL-43:")
print("Sesh".zfill(10)) #Fills the string with a specified number of 0 values at the beginning