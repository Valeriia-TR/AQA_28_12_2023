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

class DTEKEmployee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m welder from DTEK')


mykola = DTEKEmployee(3000, 'welder')
mykola.do_work()
mykola.chill()
#employee = Employee(1, 'a')
