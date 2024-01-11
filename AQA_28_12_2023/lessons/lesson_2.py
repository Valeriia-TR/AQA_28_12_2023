food = 'Pizza'
cost = 10
print("Your food is %s dollars" % (cost))
print(f"Your food is {cost} dollars")


import math
import random


simple_int = 1    #int
b = 2.5  #float
c = True #bool
person_name = 'John'  #str
second_int = 2
print(simple_int+second_int)
third_int = simple_int+second_int
print(third_int)
print(second_int-1)
print(second_int*4)
print(second_int/2)
print(8//4)
print(11%4)
print(3**3)
print(2+3*4)
print((2+3)*4)
'''
1. **
2.*, /,//, %
3.+,-
'''
new_value = 2 + 2.0
print(type(new_value))
small_number = 0.1
smaller_number = 0.000000001
print(0.2 + 0.1)
first_float = 2.3543745905
print(round(first_float, 4))
print(dir(math))
print(math.pi)
print(math.cos(0))
print(dir(random))
print(random.randint(20,30))
print(random.randrange(15))
print(random.choice(['black', 'white', 'grey']))
neqw_string = 'adsghsfj'
new_string = "I'm i don`t know\" dude"
another_new_string = 'this is called "wednesday"'
print(dir('a'))
message = 'i`m a sMall message'
print(message.capitalize())
print(message.title())
print(message.upper())
print(message.lower())
first_name = 'Oleh'
last_name = 'Vershynin'
full_name = '\t'+first_name+' '+last_name
print(full_name)
print('students:\nOlha \nVolodymyr')
print('python       '.rstrip())
print('     Python'.lstrip())
print('    Python      '.strip())
py_string_example = 'python is a very bad bad bad language'
print(py_string_example.replace('bad', 'good',2))
print('good' in py_string_example)
print(type(py_string_example))
print(py_string_example.islower())
print(py_string_example.isupper())
print(py_string_example.startswith('python'))
print(py_string_example.endswith('lang'))
print(first_name.isalpha())
one = '1'
print(one.isdigit())
special_symbols = '\n\t   '
print(special_symbols.isspace())
print(special_symbols.isprintable())
print(py_string_example.islower(), py_string_example.isspace())
print(py_string_example.capitalize().startswith('Python'))
print(py_string_example.count('bad'))
print(py_string_example.index('bad'))
print(py_string_example.find('bat'))
print(len(py_string_example))
splitted_string = py_string_example.split('very')
print(splitted_string)
lines_example = 'a\n b\nc'
print(lines_example.splitlines())
print(py_string_example[20])
print(py_string_example[10:20])
food = 'Pizza'
cost = 150
str_cost =str(cost)
print('your'+food+'cost'+str(cost))
print('Your % costs % hryvnias' % (cost, cost))
print('thanks for this{}, here`s your {}'.format(food, cost))
print(f'Happily, I went home with my {food}, and without my {cost} hryvnias')