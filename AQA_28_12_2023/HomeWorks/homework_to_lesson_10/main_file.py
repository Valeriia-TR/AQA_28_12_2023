#  Exercise 1
from functions import multiplication, summation, division

print(summation(2,2))
print(division(10,5))
print(multiplication(87,93))


#  Exercise 2

def reading_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return [element[1:-1] for element in lines]


print(reading_file("domains.txt"))



#  Exercise 3

def write_file(filename, content):
    with open(filename, "w") as file:
        for number, name, country in content:
            file.write(f'{number}, {name}, {country}\n')


filename = "names.txt"
content = [
    (1, "Johnson", "USA"),
    (2, "Brown", "Canada"),
    (3, "Bakanova", "Ukraine"),
    (4, "Sandahl", "GB"),
    (5, "Brianna", "USA")
]

write_file(filename, content)


def reading_file(filename):
    names = []
    with open(filename, "r") as file:
        for line in file:
            item = line.strip().split(", ")
            name = item[1]
            names.append(name)
    return names


print(reading_file("names.txt"))


#  Exercise 4

def date_reading(filename):
    dates = []
    with open(filename, "r") as file:
        for line in file:
            item = line.split(" - ")
            if len(item[0].split(' ')) > 1:
                dates.append(item[0])
    return [{"date": item} for item in dates]


print(date_reading("authors.txt"))


#  Exercise 5

import csv

def reading_file(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        return rows


def write_file(filename, content):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(content)


filename = "csv_file.csv"
data_for_file = [
    ["FIRST_NAME", "LAST_NAME", "AGE"],
    ["Bob", "Smith", "78"],
    ["John", "Smith", "40"],
    ["Alice", "Grey", "15"],
    ["Britney", "Fox", "93"]
]

write_file(filename, data_for_file)
read_file = reading_file(filename)
for row in read_file:
    print(row)


adding_data = [
    ["Julie", "Kennedy", "33"],
    ["Eva", "Lorem", "62"],
    ["Denny", "Jons", "29"]
]

updated_data = data_for_file + adding_data

new_file = "updated_data.csv"
write_file(new_file, updated_data)
