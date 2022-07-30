# Special methods
# __str__ print(self)
# __eq__ self == other
# __gt__ self > other
# __lt__ self < other
# __add__ self + other
# __sub__ self - other
'''# __str__ print(self)
class Ball():
    def __init__(self,num):
        self.num = num

    def __str__(self):
        return "Number: " + str(self.num)

ball1 = Ball(10)
print(ball1)'''
'''# __eq__ self == other
class Ball():
    def __init__(self,num):
        self.num = num

    def __eq__(self,other):
        return self.num == other.num
ball1 = Ball(10)
ball2 = Ball(10)
print(ball1==ball2)'''
'''# __add__ self + other
class Ball():
    def __init__(self,num):
        self.num = num
    def __eq__(self, other):
        return self.num == other.num
    def __str__(self):
        return "Number = " + str(self.num)
    def __add__(self, other):
        ball = Ball(self.num + other.num)
        return ball
ball_1 = Ball(10)
ball_2 = Ball(10)
print(ball_1)
print(ball_2 == ball_1)'''
# namedtuple like a simple class
from collections import namedtuple
Person = namedtuple('Person','name age')

class Programmer (Person):
    def programming(self):
        print(self.name + ": do programming")

p1 = Programmer('Jack',23)
p1.programming()