# 1) List []
# 2) Tuple ()
# 3) Dictionary {key:value}
#   - key map to value, no duplicate key, no order
# 4) Set set()
#   -dictionary without value, no duplicate, no order
'''# list can be alter
data = list()
data = [1,2,3]
data[0] =2'''

'''#Tuple cannot be alter (no insert,append,del)
data = tuple()
data = (1,2,3)'''
'''# Dictionary
data = dict()
data = {'key1':1,'key2':2}
#Set
data = set()
data = {1,2,3}'''

'''# Define a dictionary
data = dict()
data = {}
data = {'key1':1,'key2':2}
data = {'key1':1,'key1':2} #2 will replace 1
data = {'key1':1, 9999:1000} #key type can be mixed, key => immutable
print(data)
data = {'key1': 1,'key2':[0,1,2],'key3':(0,1,2)} #value can be any datatype
data = {('a','b'):(1,2),('c','d'):(3,4),():(5,6)} #key must be immutable, tuple as key => OK
print(data)
#data = {['a','b']:(1,2)} #list cannot be key'''

'''# Dictionary conversion (key:value)
data = ['12','34'] #string to dictionary
data = [[1,2],[3,4]] #list to dictionary
data = [(1,2),(3,4)] #tuple to dictionary
data = ((1,2),(3,4))#tuple to dictionary
data = ((1,2),(3,4))
newData = dict(data)
print(newData)'''

'''# Update an element
data = {'key1':1,'key2':2}
print(data['key1'])
data['key1'] = 999
print(data)
data['key1']= (1,2,3)
print(data)
data[0] = 1234 #0 is not index here, it is a key
print(data)'''

'''#Merge to dictionary
data1 = {'key1':1,'key2':2}
data2 = {'key3':3, 'key4':4}
data1.update(data2)  #data1+data2 (merge)
print(data1)
print(data2)'''

'''# Remove an element
data = {'key1':1, 'key2':2}
del data ['key1']
print(data)

# Clear all element
data.clear() #method 1
# data = {} #method 2
print(data)'''

'''# Check if KEY exists
data = {'key1':1,'key2':2}
dataFound = 'key2' in data
dataFound2 = 'key3' in data
print(dataFound)
print(dataFound2)'''

'''#Access an element: [key] vs get*()
data = {'key1':1,'key2':2}
print(data['key1']) #valid
#print(data['key999']) #key error
print(data.get('key999')) #none, because here is no ket999
print(data.get('key1',999)) #get with default value (not useful because key1 exisit.)
print(data.get('key999',999)) #return 999 because key999 not exits (return default value)'''

'''#Get all keys
data = {'key1':1,'key2':2}
keys = data.keys() #return all keys
keys = list(keys) #create a list contain data.keys
print(keys)
#Get all values
data = {'key1':1,'key2':2}
values = data.values()
values = list(values)
print(values)'''

'''# Get all items
data = {'key1':1,'key2':2}
items = data.items() #return tuple
items = list(items)
print(items)
# same as:
itemsDict = dict(items) #turn tuple to dictionary
print(itemsDict)'''

'''# Copy a dictionary
data = {'key1':1,'key2':2}
newDict = data.copy()
print(newDict)'''

'''#define a set (only key)
data = set()
data = {1,2,3} #no duplicate
# Set conversion
#data = set('testing')  #trun string to set
data = set([1,2,3]) #turn a list to set
data = set((1,2,3)) #trun tuple to set
data = set({'key1':1,'key2':2}) #turn dictionary to set.(key only)
print(data)
#Check if item in set
data = {1,2,3}
bFound = 1 in data
print(bFound)'''

#Set function:
#   1:Intersection
#   2:Union
#   3:Difference
'''#Intersection
data1 = {1,2}
data2 = {2,3}
intersect_1 = data1 & data2
intersect_2 = data1.intersection(data2)
print(intersect_1)
print(intersect_2)'''

'''#Union
data1 = {1,2}
data2 = {2,3}
union_1 = data1 | data2
union_2 = data1.union(data2)
print(union_1)
print(union_2)'''

'''#differece
data_1 = {1,2}
data_2 = {2,3}
difference = data_1 - data_2
difference = data_1.difference(data_2)
print(difference)'''









