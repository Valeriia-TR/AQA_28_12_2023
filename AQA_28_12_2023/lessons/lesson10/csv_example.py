import csv

with open('birthday.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
    print(csv_reader, type(csv_reader))

with open('birthday.txt', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

with open('birthday.csv', 'w') as birthday:
    birthday_writer = csv.writer(birthday, delimiter=',')
    birthday_writer.writerow(['name', 'surname', 'group', 'birthday'])
    birthday_writer.writerow(['Jhon', 'Dow','python',12])
    birthday_writer.writerows([['mister', 'twister','backend',2], ['Missis', 'Porrige', 'DevOps',7]])

with open('birthday2.csv', 'w') as birthday:
    birthday_headers = ['name', 'surname', 'group', 'birthday']
    birthday_dict_writer = csv.DictWriter(birthday, fieldnames=birthday_headers)
    birthday_dict_writer.writeheader()
    birthday_dict_writer.writerow({'name':'Jhon', 'surname':'Dow', 'group':'python', 'birthday':12})
    birthday_dict_writer.writerows([{'name':'mister', 'surname':'twister', 'group':'backend', 'birthday':2},
                                    {'name':'Missis', 'surname':'Porrige', 'group':'DevOps', 'birthday':7}])

