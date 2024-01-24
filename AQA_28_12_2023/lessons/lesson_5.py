set_1 = {1,2,3,4,5}
set_2 = {5,6,7,8,1,2}
set_3 = {5,6,10}
set_4 = set_2.difference(set_3, set_1)
print(set_4)


dict_to_test = {1:2, 2:3, 3:4, 4:5, 5:6, 6:7}
dict_to_test_2 = {1:"two", 2:"three", 3:"four", 4:5, 5:6}

new_dict = dict_to_test_2.fromkeys(dict_to_test)
print(new_dict)

new_dict["new_key"] = "value"
print(new_dict)



# dictionary_examples

perfect_dict = {'one':1, 'two':2, 'banana':'yes', 14:6, 15:17}
'''lil_bit_less_perfect_dict = {
    1:2,
    'three':3
}
perfect_dict[14] = 15
print(perfect_dict[14])
print(len(perfect_dict))
print(perfect_dict['banana'].islower())
print(perfect_dict['one']>perfect_dict['two'])
del perfect_dict[14]
print(perfect_dict)
print('one' in perfect_dict)
lil_bit_less_perfect_dict.clear()
print(lil_bit_less_perfect_dict)
ugly_dict = perfect_dict.copy()
print(ugly_dict)
dict_to_test = {1:2, 3:4, 5:6}
new_value = ugly_dict.fromkeys(ugly_dict)
print(new_value)
a = None
print(a)
print(type(a))
a = 1
print(a)
print(None)
print('')
print("" == None)
print(perfect_dict.get('one'))
keys_list = list(perfect_dict.keys())
print(perfect_dict.values())
keys_list.pop()
print(keys_list)'''
print(perfect_dict)
for key, value in perfect_dict.items():
    print(key, value)
a = perfect_dict.pop('one')
print(a)
print(perfect_dict)
b = perfect_dict.popitem()
print(b)
new_value = 100
new_key = 'hundred'
new_key1 = 'thousand'
new_value1 = 1000
perfect_dict[new_key]=new_value
print(perfect_dict)
new_dict = dict()
counter = 0
for key, value in perfect_dict.items():
    if counter == 1:
        new_dict[new_key1]=new_value1
    new_dict[key] = value
    counter+=1
print(new_dict)


# set_examples


v={'A', 'C', 4, False}
list_v = ['A', 'C', 4, False, 'A']
another_v = set(list_v)
print(list_v)
list_vv = list(another_v)
print(list_vv)
print(list(set(list_v)))
print(len(another_v))
print(False in v)
first_set = {1,2,3,4,5}
second_set = {3,4,5,6,7}
third_set = {3,4,5}
print(first_set.isdisjoint(second_set))
print(third_set.issubset(first_set))
print(third_set<=first_set)
print(second_set.issuperset(third_set)) # >=
print(v.issuperset(another_v))
fourth_set = first_set.intersection(second_set)
print(fourth_set)
fifth_set = first_set.union(second_set)
print(fifth_set)
sixth_set = fifth_set.difference(fourth_set)
print(sixth_set)
seventh_set = fifth_set.symmetric_difference(fourth_set)
print(seventh_set)
eight_set = seventh_set.copy()
print(eight_set)
eight_set.update(v)
print(eight_set)
third_set.intersection_update(v)
print(third_set)
fifth_set.difference_update(v)
print(fifth_set)
second_set.symmetric_difference_update(v)
print(second_set)
second_set.add(17)
second_set.remove(False)
print(second_set)
second_set.discard(11)
print(second_set)
exactly_new_set = second_set.pop()
print(exactly_new_set)
second_set.clear()
print(second_set)


# simp_func_examples

def name_greeter():
    your_name= input('hi please tell me what`s tour name ')
    print(f'henlo {your_name}')

a = 'sgsrgh'.isdigit()
name_greeter()
name_greeter()
name_greeter()


