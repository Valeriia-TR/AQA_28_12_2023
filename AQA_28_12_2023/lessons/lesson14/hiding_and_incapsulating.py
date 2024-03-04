from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position

    @abstractmethod
    def do_work(self):
        pass

    def chill(self):
        print('chillin')

class Engineer(Employee):
    def __init__(self):
        super().__init__(4000, 'Engineer')

    def _deploy_program(self):
        print('Deploying')

    def __create_framework(self):
        print('Creating new framework')

    def __create_infrastructure(self):
        print('Creating infrastructure')

    def deploy(self):
        self.__create_infrastructure()
        self.__create_framework()
        self._deploy_program()

    def do_work(self):
        print('I`m creating new framework')

class Developer(Engineer):
    def __init__(self):
        super().__init__()

    def do_work(self):
        print('I`m writing new programs using framework')
        self._deploy_program()
        self.deploy()

dev = Developer()
dev.do_work()
engineer = Engineer()
engineer.__create_framework()

class Human:
    def __init__(self, name:str, age:int):
        self.__hidden_name = name
        self._age = age

    @property
    def name(self):
        return self.__hidden_name

john = Human('John', 30)