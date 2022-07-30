'''1. Iterable
    -Requirement: class must implement __iter__(), which return an iterator object
    -Usage: For each item loop

    2. Iterator
        -Requirement: class must implement__iter__() AND __next__()
        -Usgae: Call next() to load next item in the collection

    3. Iterable can be convert to lterator using iter()
    '''

# 1. Iterable - object with __iter__() -> For each item Loop, can call iter() to get an iterator
# 2. Iterator - object with __iter__() + __next__() -> can call next (iterator) to get next item

'''#without for each item Loop
list = [1,2,3]
for i in range (0,3):
    print(list[i])'''
'''# With for each item Loop #Iterable object
list = [1,2,3]
for item in list:
     print(item)
for i in list:
    print(i)'''
# Iterator AND next()
# Create an iterator using iter()
'''# list example # List, Dictionary, tuple are Iterable
list = [1,2,3,4]
iterator = iter(list) #change interable to Iterator

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    pass'''
'''# set example
numbers = {1,2,3}
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))'''
'''# char example
str = 'abcdef'
iterator = iter(str)
print(next(iterator))
print(next(iterator))
print(next(iterator))
list = [1,2,3,4]
iterator = iter(list)

for item in iterator:
    print(item)

for item in list:
    print(item)

for i in list:
    print(i)'''

class Square ():
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >=self.end:
            raise StopIteration
        current = self.start * self.start
        self.start = self.start +1
        return current

square = Square(1,10)

for item in square: #iterable
     print(item)

#print(next(square)) #iterator


























