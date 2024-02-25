class TrainCar:
    def __init__(self, number, locomotive=False):
        self.__number = number
        self.__capacity = 10
        self.__passengers = []
        self.__locomotive = locomotive

    def __len__(self):
        return len(self.__passengers)

    def add_passenger(self, passenger):
        if len(self.__passengers) < self.__capacity:
            self.__passengers.append(passenger)
        else:
            print(f"There are no available sits in the {self.__number} car")

    def __str__(self):
        string = f'"Car": "{self.__number}"\n'
        for idx, passenger in enumerate(self.__passengers, start=1):
            string += f'"passenger_name": "{passenger["name"]}"\n'
            string += f'"destination": "{passenger["destination"]}",\n'
            string += f'"place": {passenger["place"]}\n'
        return string


class Train:
    def __init__(self, name):
        self.__name = name
        self.__cars = []

    def add_car(self, car):
        self.__cars.append(car)

    def __len__(self):
        return len(self.__cars) - 1 if self.__cars else 0


train = Train("England Express")
locomotive = TrainCar(0, locomotive=True)
car1 = TrainCar(1)
car2 = TrainCar(2)
car3 = TrainCar(3)
car4 = TrainCar(4)

train.add_car(locomotive)
train.add_car(car1)
train.add_car(car2)
train.add_car(car3)
train.add_car(car4)

car1.add_passenger({"name": "John Dow", "destination": "London", "place": 1})
car1.add_passenger({"name": "Grace Ford", "destination": "London", "place": 2})
car1.add_passenger({"name": "Billy Down", "destination": "Manchester", "place": 3})
car2.add_passenger({"name": "Mikky Red", "destination": "London", "place": 1})
car3.add_passenger({"name": "Judy Fox", "destination": "Manchester", "place": 2})
car3.add_passenger({"name": "Emma Rather", "destination": "London", "place": 4})
car3.add_passenger({"name": "Mikky Loud", "destination": "Manchester", "place": 5})
car4.add_passenger({"name": "Boris Johnson", "destination": "London", "place": 1})

print(car1)
print(car2)
print(car3)
print(car4)


print(f"Number of train cars: {train.__len__()}")
print(f"Number of passengers in the 1st car: {car1.__len__()}")
print(f"Number of passengers in the 2nd car: {car2.__len__()}")
print(f"Number of passengers in the 3rd car: {car3.__len__()}")
print(f"Number of passengers in the 4th car: {car4.__len__()}")