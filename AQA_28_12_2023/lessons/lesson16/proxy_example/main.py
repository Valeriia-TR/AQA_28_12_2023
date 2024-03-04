from lesson16.proxy_example.csv_reader import CSVReader
from lesson16.proxy_example.csv_proxy_reader import CSVProxyReader


csv_reader = CSVReader('example_to_read.csv')
reader = CSVProxyReader(csv_reader)
print(reader.read())
print(reader.read())
print()