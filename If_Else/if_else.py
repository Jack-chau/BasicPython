'''#User input
name = input("what is your name? ")
print("Hello " + name.capitalize()+"!")'''
'''# Compare values: >,>=,<,<=,==,!=
age = input("What is your age? ") #input will be string
age = int(age)
print(age >= 60)'''
'''#if-else
#if <bool>:<...> else: <...>
age = input("What is your age? ")
age = int(age)
if age >= 18:
    print("you are adult")
    print("you can drink wine")
else:
    print("you are young")
    print("you can't drink wine")'''
'''age = input("What is your age")
age = int(age)

if age >= 60:
    print("you are very old")
    print("Time to go to bed now")
elif age >= 18:
    print("you are old")
    print("you can drink wine")
else:
    print("you are young")
    print("you can drink milk")'''
'''#while loop
#while <bool>:
#break to terminate loop
while True:
    name = input("What is your name? [q to quit]")

    if name =='':
        continue
    if name == 'q':
        break
    print("Hello " + name.capitalize()+"!")'''
'''# for loop
words = "testing"
for character in words:
    print(character)'''
'''brands = ['Sony','LG','Google'] #for each element inside the list, print that out
for brand in brands:
    print(brand)'''
'''brands = {'Sony','LG','Google'} #print every element in SET
for brand in brands:
    print(brand)'''
'''brands = {'key1':"Sony",'key2':"LG",'key3':"Google"}
for brand in brands:
    print(brand)
for brand in brands.values():
    print(brand)
for brand in brands.items(): #turn to tuple 
    print(brand)

for key, value in brands.items():
    print("key: "+key,"value: "+value)'''
'''brands = {'key1':1,'key2':2,'key3':3}
for key, value in brands.items():
    print("key: " + key + " value: " + str(value)) #number can't concatenate to string, so it have to convert string'''
# for-in-range
#range(start,end,step)
'''for i in range(0,10): #from 0 to 9
        print(i)
for i in range (10,0,-2):
    print(i)
data = list(range(10,0,-2)) #make a list
print(data)
data = list(range(100,0,-2))
print(data)'''
'''#Comprehensions
#method 1
data = []
data.append(1)
data.append(2)
data.append(3)
print(data)
#method 2
data = [1,2,3]
print(data)
#method 3
data = list(range(1,4))
print(data)'''
'''#List comprehensions
data = [x for x in range(0,4)]
print(data)
data2 = [x for x in range(0,4) if x > 1]
print(data2)
data2 = [x*x for x in range(0,4) if x > 1]
print(data2)'''

'''# dictionary comprehension
'#{key_expression: value_expression for item in iterable}
data = {x:x for x in range(1,4)} #x as key and value
print(data)
data = {x:x+1 for x in range(1,4)}
print(data)''''




































