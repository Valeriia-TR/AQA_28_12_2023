from lesson16.proxy_example.reader import Reader


class CSVReader(Reader):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as csv_file:
            text = csv_file.read()
            return text