def dollar(func):
    def inner(*args, **kwargs):
        header, footer = "$" * 20, "$" * 20
        return f"{header}\n{func(*args, **kwargs)} \n{footer}"
    return inner

def star(func):
    def inner(*args, **kwargs):
        header, footer = "*" * 20, "*" * 20
        return f"{header}\n{func(*args, **kwargs)} \n{footer}"
    return inner

def add_footer_header(sign, quantity):
    def middle_dec(func):
        def inner(something):
            footer = sign*quantity
            header = sign*quantity
            return f'{header}{func(something)}{footer}'
        return inner
    return middle_dec


@add_footer_header("AAAAAA", 5)
@dollar
@star
def hi(msg):
    return "$$$\n***\n" + msg + "\n***\n$$$"

print(hi('Hello'))

primitive_loging_list = []

import datetime
def a_func(func):
    def inner(some):
        primitive_loging_list.append(some)
        a = datetime.datetime.now()
        result = func(some)
        b = datetime.datetime.now()
        print("diff = ", b-a)
        return result
    return inner

@a_func
def counter_func(num):
    total = sum([x for x in range(0, num ** 2)])
    return total

print(counter_func(500))
print(primitive_loging_list)