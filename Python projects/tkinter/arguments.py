def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n

    return sum


print(add(1, 2, 3, 4, 45, 5, 5, 5, 5, 5))


def calculate(**kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)


class Car:
    def __int__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']


my_car = Car()
