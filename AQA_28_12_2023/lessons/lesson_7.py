from functools import reduce
list_c = [[6, 4, 5], [6, 1], [9, 10, 11]]

sorted_list = lambda x: (sorted(el) for el in x)

print(list(sorted_list(list_c)))
"""
1. сделать одним списком и отсортировать
2. найти суммы каждого элемента и отсортировать по суммам
"""

