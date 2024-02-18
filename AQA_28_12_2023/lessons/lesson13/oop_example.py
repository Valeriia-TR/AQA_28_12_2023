class Dog:
    owner_friends = []

class Human:
    def __init__(self, name:str, age:int, salary, job_position, hair_color):
        self.name = name
        self.age = age
        self.salary = salary
        self.job_position = job_position
        self.hair_color = hair_color

    def get_name(self):
        return self.name

    @classmethod
    def from_name_and_age(cls, name, age):
        return cls(name, age, None, None, None)

    @staticmethod
    def count_bonus(salary):
        return salary*1.2

john = Human.from_name_and_age('John', 30)
evelynn = Human.from_name_and_age('Evelynn', 32)
evelynn.salary = 4000
print(john.get_name())
print(evelynn.get_name())
print(evelynn.count_bonus(evelynn.salary))