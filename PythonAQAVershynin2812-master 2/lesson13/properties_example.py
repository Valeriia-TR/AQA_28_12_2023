class Human:
    def __init__(self, name:str, age:int):
        self.__hidden_name = name
        self._age = age

    @property
    def name(self):
        return self.__hidden_name

    @name.setter
    def name(self, new_name):
        self.__hidden_name = new_name

    def modify_age(self, new_age):
        self.__age=new_age
john = Human('John', 30)
john.modify_age(29)
print(john.name)
john.name = 'John1'
print(john.name)
john.name='1'

