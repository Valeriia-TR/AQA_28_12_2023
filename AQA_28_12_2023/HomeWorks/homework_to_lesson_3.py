import random

# Exercise 1

minutes = random.randint(0, 59)
if 0 <= minutes < 15:
    print(f"({minutes}) This is the first quarter of hour")
elif 15 <= minutes < 30:
    print(f"({minutes}) This is the second quarter of hour")
elif 30 <= minutes < 45:
    print(f"({minutes}) This is the third quarter of hour")
else:
    print(f"({minutes}) This is the fourth quarter of hour")

# Exercise 2

birth_month = input("Enter your birth month number: ")
print(birth_month)
winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)
if birth_month.isdigit():
    if int(birth_month) in winter:
        print("It was snowing outside the window")
    elif int(birth_month) in spring:
        print("Everything around blossomed")
    elif int(birth_month) in summer:
        print("The children enjoyed their summer vacation")
    elif int(birth_month) in autumn:
        print("Everything around lit up with bright colors")
    else:
        print("It is not a month")
else:
    print("It is invalid value, you should enter a number of the month")

# Exercise 3

random_number = random.randint(0, 999999999)
digits = str(random_number)
sum_digits = sum(int(digit) for digit in digits)
last_digit = int(digits[-1])

if last_digit % 2 == 0 and sum_digits % 3 == 0:
    print(f"The {random_number} can be divided by 6")
else:
    print(f"The {random_number} cannot be divided by 6")

# Exercise 4

x_str = input("Enter x: ")
y_str = input("Enter y: ")

if (x_str.replace("-", "", 1).replace(".", "", 1).isdigit()
        and y_str.replace("-", "", 1).replace(".", "", 1).isdigit()):
    x = float(x_str)
    y = float(y_str)

    if x == 0 and y == 0:
        print("The point lies at the origin")
    elif x == 0:
        print("The point lies on the X axis")
    elif y == 0:
        print("The point is on the Y axis")
    elif x > 0 and y > 0:
        print("The point lies in the 1st quarter of the coordinates")
    elif x > 0 and y < 0:
        print("The point lies in the 2nd quarter of the coordinates")
    elif x < 0 and y < 0:
        print("The point lies in the 3rd quarter of the coordinates")
    else:
        print("The point lies in the 4th quarter of the coordinates")
else:
    if (not x_str.replace("-", "", 1).replace(".", "", 1).isdigit()
            and not y_str.replace("-", "", 1).replace(".", "", 1).isdigit()):
        print("It's not valid coordinates, try again")
    elif not x_str.replace("-", "", 1).replace(".", "", 1).isdigit():
        print("X is not a digit")
    else:
        print("Y is not a digit")
