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



