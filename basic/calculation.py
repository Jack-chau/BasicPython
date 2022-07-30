''' Operator
a = 2
b = 4
#a = a*b
a*=b #= a = a*b
print(a)
a = 2
c = a/b #output floating point
print(c)
c = a//b #output integer
print(c)

print("a: ", a)

#2/4
d = a%b #a/b modulus
print(d)
#4/2
d = b%a # b/a
print(d)
'''
'''
# Type conversion
a = int("123") + 1 # "123" is a string, change to integer for cauculation
print(a)
# a = int("123.1") +1 #wrong: int cannot apply to float
a = float("123.1") +1 # use float conversion
print(a)
a = float(88) #88 is integer, change to 88.1
print(a)
a = bool(100) #true != 0 , false = 0
print(a)
a = bool(0)
print(a)

a = str(0) #change to string datatype
print(type(a))
'''
'''
# string concatenation
a = "test" + "ing"
print(a)
a = "test" "ing"
print(a)
a = "Testing\n" * 10 #print Testing 10 times
print(a)
'''
'''
# use index to get a character in a string
a = "0123456789" #python is 0 base
print(a[0]) #first character
print(a[-1]) #last character
#print(a[100]) #out of range
#a[0] = "2" #incorrect, string is immutable (cannot be alter)
# Slicing [start:end:step]
print(a[0:]) #from start to the end
print(a[0:5]) #from 0 to 4
print(a[0::2]) #start from 0 char and skip 1
print(a[1::2]) #start from 2nd char and skip 1 char
print(a[9::-1]) #print inverse string
# change string
a = "T" + a[1:] # T + string from 1st char to the end
#string cannot to alter, it have assign another variable
print(a)
'''
'''# String function
# Len, startswith, endswith, find(indexOf), count, replace
a = "0123456789"
print(len(a)) #length of the string
print(a.startswith("a")) # start from a? No
print(a.startswith("01")) #start from 01? Yes
print(a.endswith("789"))
print(a.find("789")) #find the posintion in a string
print(a.count("1")) #How many 1 in a string
b = "11111"
print(b.count("1"))
print(a.replace("1","x")) #replace 1 to x (but not changing the variable)
print(a)
c = a.replace("1","x")
print(c)'''
# triple quote
message = "Testing"
message = 'Testing'
message = '''Testing'''
#print(message)
message ='''
I am Jack Chau
Remember me!!!
'''
#print(message)
print(message.strip())