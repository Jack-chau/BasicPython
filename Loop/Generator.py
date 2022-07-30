# Generator function
# 1. function with yield keyword
# 2. yield may return value & pause execution and keep states
# 3. use next(generator) to resume execution of the function, with previous state
# 4. yield can use multiple times in a function
# 5. can use together with return

def generator_func():
    counter = 0
    for i in range (1,3):
        counter = counter +1
        yield counter


genereator = generator_func()
print(next(genereator))
print(next(genereator))
print(next(genereator))











