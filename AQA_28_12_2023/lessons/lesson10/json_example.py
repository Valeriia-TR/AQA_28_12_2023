import json

'''
dict -> object {}
list, tuple -> array []
str -> string
int, float -> number
True, False -> true, false
None -> null
'''

data = {
    'name':'Alejandro',
    'age':60,
    'songs':['halleluya', 'too late'],
    'alive':True,
    'minuses':None,
    'base':{'base1':{'base2':{'unique_value':'12423534534'}}}
}

json_str = ''
with open('alejandro.json', 'w') as writer:
    json.dump(data, writer,indent=4)
    json_str = json.dumps(data, indent=4)
    print(json_str)


'''
object->dict
array->list
string->str
number-> int, float
true, false->True, False
null->None
'''

data_otside_scope = {}
with open('alejandro.json','r') as reader:
    data_otside_scope = json.load(reader)
    print(type(data_otside_scope))

data1 = json.dumps(data_otside_scope)
data1 = data1.replace('unique_value', 'unique_value1', 2)
data2 = json.loads(data1)
with open('modified_alejandro.json', 'w') as writer:
    json.dump(data2, writer, indent=4)


