# Exercise 1
# Створіть класс з описом будь-якої тварини. Додайте 1 static method


class Dog:
    def __init__(self, name, breed, colour, age):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age

    @staticmethod
    def facts_about_dogs(age):
        print("They can sense your emotions")
        print("They dream")
        print("They can be left- or right-pawed")
        print(f"The oldest dog lived to be 30, and your dog is just {age} years old")


dog_1 = Dog("Bob", "Doberman", "black", 2)
dog_2 = Dog("Micky", "dachshund", "brown", 12)

dog_1.age = 10
dog_1.facts_about_dogs(dog_1.age)

# Exercise 2

# Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod

class Company:
    def __init__(self, name, employees_amount, industry):
        self.name = name
        self.employees_amount = employees_amount
        self.industry = industry

    def __str__(self):
        return f"{self.name} is a greate company"

    @classmethod
    def from_string(cls, company_string):
        name, employees_amount, industry = company_string
        return cls(name, employees_amount, industry)


company_1 = Company("NovaPoshta", 500, "Post")
company_2 = Company("Samsung", 2000, "Mobile")
company_3 = Company("UZ", 3000, "Railway")


