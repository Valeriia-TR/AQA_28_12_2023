# Exercise 2

import csv


class CSVManager:
    def __init__(self, filename):
        self.filename = filename

    def add_row(self, row_data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=row_data.keys())
            writer.writerow(row_data)

    def remove_row(self, match_criteria):
        rows = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not all(row[key] == match_criteria[key] for key in match_criteria):
                    rows.append(row)

        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)


def test_add_row():
    filename = "example.csv"
    manager = CSVManager(filename)
    manager.add_row({
        'first_name': 'John',
        'last_name': 'Doe',
        'age': '37',
        'gender': 'Male',
        'salary': '39900'
    })
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        print(rows[-1])
        assert rows[-1] == {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': '37',
            'gender': 'Male',
            'salary': '39900'
        }


def test_remove_row():
    filename = 'example.csv'
    manager = CSVManager(filename)

    manager.remove_row({
        'first_name': 'John',
        'last_name': 'Doe',
        'age': '37',
        'gender': 'Male',
        'salary': '39900'
    })

    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        for row in rows:
            assert not (row['first_name'] == 'John' and row['age'] == '37'), "Row was not removed"
