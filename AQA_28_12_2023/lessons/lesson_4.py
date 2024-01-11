#first_list = []
#second_list = list()
'''cool_fruit = 'watermelon'
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

first_list = [1,6,8,4,6,3,5,2]

print(sorted(first_list, reverse=True))
print(first_list[4:])
print(first_list[:4])
second_list = first_list[:4]
print(second_list)
print(first_list[2:5])
first_list.extend(second_list)
print(first_list)
third_list = []
for element in first_list:
    third_list.append(element*2)
fourth_list = first_list+second_list
print(fourth_list)
a =[1,2,3,4]
b = a
a.append(5)
b.append(6)
print(a)
print(b)
c = a.copy()
c.pop()
print(a)
print(c)
a = [1,2]
b = [3,4]
c = a + b
a.pop()
print(c)
a.extend(b)
b.pop()
print(a)
d = list(a)
print(d)
a.pop()
print(f'd:{d}')
print(id(a))
print(id(d))
d.append(1)
print(id(d))
e = 1231342534
print(id(e))
e +=134253267658743
print(id(e))
'''
first_list = [2,5,6,6,6,7,8,9]
print(first_list.count(6))
first_list.reverse()
print(first_list)
first_tuple = (4,5,6,7,8)
print(first_tuple[0])
elements_list = []
for element in first_list:
    if element>7:
        continue
print(elements_list)
counter = 0
while counter<10:
    print('help me im stuck in the infinite loop')
    counter+=1
for element in 'hello world':
    if element == 'o':
        continue
    print(element)
while counter <20:
    counter += 1
    if counter%2 ==1:
        continue
    print(counter)
while counter <30:
    counter += 1
    if counter%2 ==1:
        print('i`m about to break')
        break
    print(counter)

for i in 'hello_world':
    if i == 'o':
        print(f'this_string_have {i} letter, I`m about to  die')
        break
    else:
        print(i)
else:
    print('this_string_have_not any A letters')









