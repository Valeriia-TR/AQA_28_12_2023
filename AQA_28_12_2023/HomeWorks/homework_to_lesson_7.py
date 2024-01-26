from functools import reduce
# Exercise 1

list_1 = [1, 2, 5, 6, 7, 9, 10]
list_2 = [8, 9, 10, 4]
match = list(filter(lambda x: x in list_1, list_2))
print(match)

# Exercise 2

is_digit = lambda x: x.isdigit()
value = "82918"
result = "The value is digit" if is_digit(value) else "The value is not a digit"
print(result)

# Exercise 3

list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
list_4 = [1, 2, 3, 4, 5]

max_len = lambda x,y: x if len(x) > len(y) else y
min_len = lambda x,y: x if len(x) < len(y) else y

result_2 = f"The {max_len(list_3, list_4)} is longer than the {min_len(list_3, list_4)}"

print(result_2)

# another solution

list_of_lists = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10]]

longest = reduce(lambda x, y: x if len(x) > len(y) else y, list_of_lists)
print(longest)

shortest = reduce(lambda x, y: x if len(x) < len(y) else y, list_of_lists)
print(shortest)