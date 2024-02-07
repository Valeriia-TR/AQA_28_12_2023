 # Exercise 1

def func_name(func):
    def wrapper(*args, **kwargs):
        print(f'The name of called function: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper



@func_name
def summation(a, b):
    return a + b


@func_name
def multiplication(a, b):
    return a * b


print(summation(2342, 8798))
print(multiplication(232, 9))


 #  Exercise 2

from random import randint

random_numbers = [randint(1, 10) for i in range(100)]

count_of_numbers = {item: random_numbers.count(item) for item in set(random_numbers)}

for item, count in count_of_numbers.items():
    print(f"Element {item}: {count}")
