
# Exercise 4

x_str = input("Enter x: ")
y_str = input("Enter y: ")

try:
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

except ValueError:
    print("Invalid")
