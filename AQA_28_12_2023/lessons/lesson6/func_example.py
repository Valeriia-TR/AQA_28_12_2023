# def check_range(start_value, end_value):
#     value = int(input("Enter a number: "))
#     if start_value <= value <= end_value:
#         return True
#     else:
#         return False
#
#
# result = check_range(3, 7)
# print(result)

# def delete_characters_mine(*characters):
#     string_value = input("Enter a string: ")
#     new_string = []
#     for character in string_value:
#         if not character in characters:
#             new_string.append(character)
#         else:
#             continue
#     return new_string
#
#
# result = delete_characters_mine("a", "z", "w", "e")
#
# print(result)

# def delete_characters(*characters):
#     string_value = input("Enter a string: ")
#     for character in string_value:
#         if character in characters:
#         #     string_value.replace(character, "")
#         # else:
#         #     continue
#
#             return string_value.replace(character, "")
#
#
# result = delete_characters("a", "z", "w", "e")
#
# print(result)

def delete_characters(*characters):
    string_value = input("Enter a string: ")
    for character in characters:
        string_value = string_value.replace(character, "")
    return string_value


result = delete_characters("a", "z", "w", "e")
print(result)




# func_examples

'''
def name_greeter():
    your_name= input('hi please tell me what`s tour name ')
    print(f'henlo {your_name}')

a = 'sgsrgh'.isdigit()
name_greeter()
name_greeter()
name_greeter()



def im_a_new_cool_func(value, value2):
    print(value**value2)

im_a_new_cool_func(value=6,value2=3)


def print_full_name(first_name, last_name, birthdate=0):
    if birthdate > 15:
        print('haha too old')
        birthdate = birthdate/2
        print('hehe younger you twice')
    print(f'Full name is {first_name} {last_name}, and I was born on {birthdate}')

print_full_name('Oleh', 'Vershynin', 16)
print_full_name(first_name='Oleh', last_name='Vershynin')


def my_favorite_language(name, language='Python'):
    print(f'hi my name is {name}, and my favourite language is {language}')


my_favorite_language('Alex', 'Java')
my_favorite_language('Mykyta')



def mr_sum_two_numbers(first_number, second_number)->int:
    return first_number+second_number


new_value = mr_sum_two_numbers(124352463, 68567634523)
print(new_value)

def make_pizza(*ingridients):
    for ingr in ingridients:
        print(f'{ingr} is a {ingridients.index(ingr)} number ingridient in pizza cooking')



make_pizza('cheese')
make_pizza('cheese', 'cheese', 'cheese', 'cheese')
make_pizza('pineapple', 'curse')
'''


def dogs(**dog_info):
    for key, value in dog_info.items():
        print(f'{key} : {value}')


def sum_and_diff(first_number, second_number):
    return first_number+second_number, first_number-second_number


if __name__ == '__main__':
    sum_result, diff_result = sum_and_diff(5, 10)
    print(sum_result)
    print(diff_result)
    sum_and_diff_result = sum_and_diff(20, 10)
    print(sum_and_diff_result)
    dogs(first_name='patron', required_amount=1000000, cooler_than='iphon')

    # *args
    # **kwargs

    dog_dict = {'1': 1, '2': 2}
    dog_items = dog_dict.items()
    print()