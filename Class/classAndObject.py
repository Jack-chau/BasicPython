#Class and Object
class person():
    propulation = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        person.propulation += 1 # class method

    def sleeping(self):
        print(self.name + ' is sleeping')

    def talking(self):
        print(self.name + ' is sleeping')

    def walking(self):
        print(self.name + ' is walking')

    @classmethod
    def print_population(cls):
        print("Population: " + str(cls.propulation))

    @staticmethod
    def watch_tv():
        print("watch tv")

class Programming(person):
    def __init__(self,name,age,language):
        super().__init__(name,age)
        self.language = language

    def program(self):
        print(self.name+' and ' + self.language)
jack = person('Jack',23)
jack.sleeping() #instance method
person.print_population() #only in one class
person.watch_tv() #static method






