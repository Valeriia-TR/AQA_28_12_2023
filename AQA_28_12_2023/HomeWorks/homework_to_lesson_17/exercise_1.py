# Exercise 1
import csv
import json


class JSONToCSVConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__lines = json.load(json_file)

    def write_file(self, filename: str):
        if self.__lines:
            headers = self.__lines[0].keys()

            with open(filename, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()

                for line in self.__lines:
                    writer.writerow(line)
            self.cleanup()
        else:
            print("No data to write")

    def cleanup(self):
        self.__lines = []


converter = JSONToCSVConverter()
converter.read_file('example.json')
converter.write_file('example_from_json.csv')
