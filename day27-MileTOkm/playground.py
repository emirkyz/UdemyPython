def add(*args):
    print(type(args))
    print(args[0])
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    #   for key, value in kwargs.items():
    #       print(key)
    #       print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan", model="GT-R", color = "Red")

