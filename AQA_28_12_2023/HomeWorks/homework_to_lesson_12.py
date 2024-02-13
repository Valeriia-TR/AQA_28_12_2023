from datetime import datetime, timedelta
# Exercise 1


def add_subtract(date_time, days, add):
    if add:
        return date_time + timedelta(days=days)
    else:
        return date_time - timedelta(days=days)


date_string = "2024-02-10"
date_format = "%Y-%m-%d"

date_time = datetime.strptime(date_string, date_format)

print(f"5 days after date_time: {add_subtract(date_time, 5, True)}")
print(f"5 days before date_time: {add_subtract(date_time, 5, False)}")



# Exercise 2


def age_calculator(birthday):
    current_date = datetime.now()
    birthday = datetime.strptime(birthday, date_format)
    age_delta = current_date - birthday
    age_timestamp = birthday.timestamp()

    birthday_string = birthday.strftime("%y-%d-%m %I:%M:%S %p")

    return current_date, age_delta, birthday_string, age_timestamp


birthday_date = "21-11-2011 15:00:00"
date_format = "%d-%m-%Y %H:%M:%S"
current_date, age_delta, birthday_string, age_timestamp = age_calculator(birthday_date)

print(f"current_date: {current_date}")
print(f"age_delta: {age_delta}")
print(f"age_timestamp: {age_timestamp}")
print(f"birthday_string: {birthday_string}")


# Exercise 3

item1 = [1,2,3,4,5,6]


def some_function(item):
    try:
        print(item[7])
    except NameError as e:
        print("Name error")
    except IndexError as e:
        print("Index error")
    except Exception as e:
        print("Exception error")

try:
    some_function(item1)
    some_function(item2)
except NameError:
    print("Name error occurred")
except Exception as e:
    print("Exception error")

try:
    x = 5
    x.append(10)
except AttributeError:
    print("AttributeError occurred")
except Exception as e:
    print("Exception error")