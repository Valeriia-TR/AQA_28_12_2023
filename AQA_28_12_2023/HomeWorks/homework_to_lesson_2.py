import math

# Exercise 1
first_name = "valeriia"
last_name = "Bakanova"

#1.1
print(first_name + " " + last_name)

#1.2
full_name = first_name + " " + last_name
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# 1.3
first_name = "  Valeriia\n"
last_name = "\tBakanova   "
full_name = first_name + last_name
print(full_name)
full_name_trimmed = first_name.strip() + " " + last_name.strip()
print(full_name_trimmed)

# Exercise 2
radius = 100
circle_length = 2 * math.pi * radius
circle_area = math.pi * radius ** 2
print(f'Having {radius} as a radius of the circle, \
the length of the circle is {circle_length} and the area of the circle is {circle_area}')

# Exercise 3
exchange_rate_hrn = 37.94
converted_amount_hrn = 1000
exchange_result_usd = round(converted_amount_hrn/exchange_rate_hrn, 2)
print('The current rate is: {} USD'.format(exchange_result_usd))