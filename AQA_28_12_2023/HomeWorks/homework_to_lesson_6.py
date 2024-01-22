import random

# Exercise 1

same_numbers_list = []


def same_numbers():
    for i in list_1:
        if i in list_2:
            same_numbers_list.append(i)
    return sorted(same_numbers_list)


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 38, 13]
list_2 = [1, 7, 13, 9, 25, 16, 7, 38, 26, 5]

print(same_numbers())

# Exercise 2

students = {"Liza": 85, "Djoconda": 60, "John": 60, "Simba": 90, "Ashly": 90, "Bob": 100}
successful_students = []


def average_grade_calc():
    average_grade = sum(students.values()) / len(students)
    return average_grade


for k, v in students.items():
    if v > average_grade_calc():
        successful_students.append(k)

print(successful_students)



# Exercise 3

name = ['Liza', 'John', 'Simba', 'Dacota', 'Djoconda']
surname = ['Morgan', 'Smith', 'White']
location = ['New York', 'Paris', 'Amsterdam', 'London']


def random_name():
    random_name_choice = random.choice(name)
    return random_name_choice


def random_surname():
    random_surname_choice = random.choice(surname)
    return random_surname_choice


def random_location():
    random_location_choice = random.choice(location)
    return random_location_choice


random_data = {"name": random_name(), "surname": random_surname(), "location": random_location()}

print(random_data)

