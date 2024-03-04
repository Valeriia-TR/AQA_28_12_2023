'''numbers = [1,2,3,4,5]
numbers_iterator = iter(numbers)
print(numbers_iterator)
#for number in numbers_iterator:
#    print(number)
print(next(numbers_iterator))
print(next(numbers_iterator))
'''
a = []
def my_gen():
    counter=0
    while True:
        yield counter **2
        counter+=1

generator = my_gen()
for item in generator:
    print(item)
