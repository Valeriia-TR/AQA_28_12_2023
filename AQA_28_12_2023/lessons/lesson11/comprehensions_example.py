'''some_list = [1,2,3,4,5]
new_list = []

for item in some_list:
    if item>3:
        new_list.append(item)

print(new_list)

new_list2 = [item for item in some_list if item > 3]
print(new_list2)

new_list = [item**2 for item in range(100000000)]
print(new_list)

names = ['Jhoanna', 'Maria', 'Alexis','Anna']
new_dict = {index:name for index, name in enumerate(names)}
print(new_dict)

list_to_filter = [1,2,2,2,3,4,6,11,36,71,17,17,17]
new_set = {item for item in list_to_filter if item>5}
print(new_set)
new_set2 = set(list_to_filter)
print(new_set2)
'''
new_gen = (*(item for item in range(10000000)),)
print(new_gen)