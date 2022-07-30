'''
Python Containers: can contain multiple element
    - Containers
       1.List[] //can change data
       2.Tuple() //can't change data
       3.Dictionary {key:value} //key is unique
        - key map to value, no duplicate key, no order
       4.Set{key}
        - dictionary without value, no duplicate, no order
    - Using List
    -Using Tuple
'''
'''
#List[]
list = list()
list2 = [1,2,3,4]
print(type(list))
print(type(list2))
print(list)
print(list2)

#tuple cannot be alter
tuple = tuple()
print(type(tuple))
print(tuple)
tuple = (1,2,3,4) #or tuple = 1,2,3,4
print(tuple)
'''
'''
# Dictionary
#create dictionary
data = dict() #or data={}
print(type(data))
print(data) #outp'key2'ut: {} --> dictionary
data = {'key1':1,'key2':2}
print(data)
#Set
data = set()
data = {1,2,3} #data cannot duplicate
print(type(data))
print(data)
data = {1,2,3,3}
print(data)
'''
'''# List example
brands = []
print(brands)
brands = list()
print(brands)
brands = ['Google','Apple']
print(brands)
brands = ['Google','Apple',1,2.0,[True,False]]
print(brands)'''
'''# convert other data type to a list
message = "Have a nice day"
myTuple = (0,1,2) # cannot be alter, so we have to change to list
messageList = list(message) #make every char in a list
print(messageList)
tupleList = list(myTuple)
print(tupleList)
tupleList[0] = 100
print(tupleList)'''
'''# access elements in list
brands = ['sorry','LG','Google']
print(brands[0])
brands[0] = 'sony'
print(brands)'''
'''#SLICE operation [start:end:step]
brands = ['sony','LG','Google']
print(brands[0:1])
print(brands[0])
print(brands[:]) #copy list
print(brands[2::-1])
print(brands[2:])'''
'''
#List of a list
googleProduct = ['Youtube', 'Google Calendar'] #list 1
appleProduct = ['iPhone','iPad'] #list2
allProducts = [googleProduct,appleProduct] # a list contain 2 list
print(allProducts)'''
'''# add elements to list
brands = ['Sony','LG','Google']
brands.append('Amazone')
print(brands)
mylist = [0,1,2]
brands.append(mylist) #append a list
print(brands)
#joining lists
brands = ['Sony','LG','Google']
otherBrands = ['Microsoft','Amazon']
brands.extend(otherBrands) #not extend a list
brands += otherBrands
print(brands)'''
'''# Insert an element
brands = ['Sony','LG','Google']
brands.insert(0,'Microsoft') #append is at rear
print(brands)
brands.insert(1,'K6')
#remove an element
del brands[0]
print(brands)

#pop and remove an element (attract the rearest element)
elementPopped = brands.pop() #default at index -1
print(elementPopped)
print(brands)
elementPopped = brands.pop(0) #the 1st index
print(elementPopped)'''
'''# check if an element exists
brands = ['Sony','LG','Google']
bFound = 'Google' in brands
bNotFound = 'Apple' in brands
print(bFound)
print(bNotFound)'''
'''#sort a list
brands = ['Sony','LG','google']
#method 1: Will modify the list
brands.sort()
print(brands)
#method 2: will not modify the list
newBrands = sorted(brands)
print(newBrands)'''
'''#create copy of a list
brands = ['Sony','LG','Google']
copy1 = brands.copy()
copy2 = list(brands)
copy3 = brands[:]
print(copy1)
print(copy2)
print(copy3)'''
'''#Tuple (cannot be alter)
brands = ()
brands = tuple()
brands = ('Sony',) #must add ,
brands = 'Sony','LG','Google'
brands = ('Sony','LG','Google')
#brands[0] = 'Apple' #illegal
brands = ('Apple','LG','Google') #ok
print(brands)'''
'''# swap variables (want to exchange these two variable)
value1 = 1
value2 = 2
#classic approach
temp = value2
value2 = value1
value1 = temp
print(value1)
print(value2)
#tuple approach
value1,value2 = value2,value1
print(value1)
print(value2)
'''
# Access elements of tuple
brands = ('Sony','LG','Google')
brands1,brands2,brands3 = brands
print(brands[0])
print(brands1)
print(brands2)
print(brands3)
print(brands[1:])
print(brands[:])








