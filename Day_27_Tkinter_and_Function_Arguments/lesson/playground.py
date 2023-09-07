def add(*args):
    num = 0
    for n in args:
        num += n
    return num

result = add(1,3,6,10,101,50)
print(result)


def calculate(n, **kwargs):
    #print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        #using the [key] method to get a key value will fail if the class isn't passed all the argments.  Use .get() instead. 
        #It will not error if the kw argument isn't passed into the function
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
