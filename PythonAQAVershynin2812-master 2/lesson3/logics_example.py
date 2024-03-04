'''new_value = True
false_value = False
print(int(new_value))
print(int(false_value))
print(bool(1))
print(bool(0))
#a = 0
#b = bool(3)
#print(b)
new_string = 'fgsh'
empty_string = ''
print(bool(new_string))
print(bool(empty_string))

<
>
<=
>=
==
!=

a = 100
b = 200
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


int_value_to_read = int(input('hey dude print int immidiately'))

if type(int_value_to_read) == str:
    print(int(int_value_to_read))
else:
    print("it's defenitely not an integer")

# or and not
if int_value_to_read >30 or int_value_to_read<20:
    print('ha! ')

if int_value_to_read>200 and int_value_to_read % 20 == 0:
    print('oh no!')

if not empty_string:
    print('hell yeah')

str_input = input('go!')

if str_input.startswith('Hello'):
    print('Hello my dear')
elif str_input.isdigit() and not str_input.startswith('2'):
    print('oh I see you mr robot')
elif str_input.startswith('2'):
    print('Second!')
else:
    print('you typed invalid value')


eyes = int(input('how many eyes?'))
legs = int(input('how many legs?'))
if eyes >= 8:
    if legs == 8:
        print('spider')
    elif legs == 6:
        print('cockroach')
    else:
        print('undefined creature')
else:
    if eyes == 2 and legs == 4:
        print('definitely a cat')
    else:
        print('horror beyond our comprehension')
'''
cool_fruit = 'watermelon'
fruits = ['apple','banana',cool_fruit,'watermelon']
print(fruits)
print(type(fruits))
print(id(fruits))
print(len(fruits))
print(fruits[-1])
print(fruits.index('watermelon', 3))
fruits.append('lemon')
print(fruits)
fruits.pop(3)
print(fruits)
fruits.pop()
print(fruits)
del fruits[1]
print(fruits)
fruits.clear()
print(fruits)




