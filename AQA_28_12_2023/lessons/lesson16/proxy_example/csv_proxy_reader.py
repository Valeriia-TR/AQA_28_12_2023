from lesson16.proxy_example.reader import Reader


class CSVProxyReader(Reader):
    def __init__(self, csv_reader):
        self.csv_reader = csv_reader
        self.result = ''
        self.is_actual = False

    def read(self):
        if self.is_actual:
            return self.result
        else:
            self.result = self.csv_reader.read()
            self.is_actual = True
            return self.result
