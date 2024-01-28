import re


# Exercise 1
string = "AaZz67_"


def checking_of_the_string(string):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return bool(re.match(pattern, string))


if checking_of_the_string(string):
    print("The string contains only upper and lower case letters, numbers and underscores.")
else:
    print("The string contains NOT only upper and lower case letters, numbers and underscores.")


# Exercise 2

string = ["example (.com)", "github (.com)", "stackoverflow (.com)"]
for i in string:
    new_string = re.sub(r'\s*\(.+?\)', '', i)
    print(new_string)


# Exercise 3
string = "It'sAn ExampleString"


def insert_spaces(string):
    res = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return res


new_string = insert_spaces(string)
print(new_string)