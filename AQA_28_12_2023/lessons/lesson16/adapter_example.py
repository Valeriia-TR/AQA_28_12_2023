import csv
import json


class CSVConverter:
    def __init__(self):
        self.lines = []

    def read_file(self, filename):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.lines.append(line)

    def write_file(self, filename):
        with open(filename, 'w') as writer:
            json.dump(self.lines, writer, indent=4)
            self.cleanup()


    def cleanup(self):
        self.lines=[]


converter = CSVConverter()
converter.read_file('example_to_read.csv')
converter.write_file('example_to_read.json')
converter.read_file('example_to_read.csv')
converter.write_file('example_to_read2.json')