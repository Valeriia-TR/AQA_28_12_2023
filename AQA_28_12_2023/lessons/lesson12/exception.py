

def sum_two_numbers(a,b):
    try:
        print(a/b)
    except TypeError as e:
        print("not supported type")
    except Exception as e:
        print("you try to divide by zero")
    else:
        print('I`m else statement')
    finally:
        print('final block')
    print('hello')


sum_two_numbers(1,2)