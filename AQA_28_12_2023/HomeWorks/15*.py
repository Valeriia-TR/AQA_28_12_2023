"""
Опишіть об'єкт Train. Класс має поля і метод додавання вагонів (додавати треба об'єкти інстанси класа вагон).
Опишіть класс TrainCar (вагон). Вагон має свої поля і список пасажирів і дозволяє додавати пасажирів. В вагоні може бути,
 наприклад,10 пасажирів. При виконанні функції len на вагоні виведіть кількість пасажирів.
 При виконанні функції len на потязі виведіть кількість вагонів без локомотива. У кожного вагона має бути номер.

за допомогою __str__реалізуйте вивід в консоль:

При перегляді вагону виводьте данні за наступним паттерном(назви полів для прикладу):

"traincart" :"1"

"passanger_name": "John Dow",

"destination": "Name of station",

"place": 1

"passanger_name": "Alex Dowson",

"destination": "Name of station",

"place": 2

Створювати класи для пасажирів чи ні - на ваш розсуд

Необов'язкова задача з зірочкою. перепишіть ваш потяг, щоб він рухався по станціям, наприклад, Лондон-Гогвортс,
або інша комбінація. Нехай на певних зупинках люди заходять, на певних виходять. Виведіть в консоль людей, які зайшли
в потяг на кожній станції, які вийшли.


"""


class Train:
    def __init__(self, name, stations):
        self.name = name
        self.stations = stations
        self.current_station = 0
        self.cars = []

    def move_to_next_station(self):
        if self.current_station < len(self.stations) - 1:
            self.current_station += 1
            print(f"Train {self.name} is arrived to {self.stations[self.current_station]}")
        else:
            print(f"Train {self.name} has arrived to the destination station")

    def add_car(self, car):
        self.cars.append(car)

    def add_passenger(self, passenger):
        current_station = self.stations[self.current_station]
        for car in self.cars:
            if car.number != 0:
                car.add_passenger(passenger, current_station)

    def exit_passenger(self, passenger_name):
        for car in self.cars:
            car.exit_passengers(passenger_name)

    def __len__(self):
        return len(self.cars) - 1 if self.cars else 0


class TrainCar:
    def __init__(self, number):
        self.number = number
        self.passengers = []
        self.capacity = 5

    def __len__(self):
        return len(self.passengers)

    def add_passenger(self, passenger, station):
        if len(self.passengers) < self.capacity:
            self.passengers.append({"name": passenger, "station": station})
        else:
            print(f"There are no available sits in the {self.number} car")

    def exit_passenger(self, passenger_name):
        self.passengers = [passenger for passenger in self.passengers if passenger["name"] != passenger_name]

    def __str__(self):
        string = f'"Train Car": "{self.number}"\n'
        for passenger in self.passengers:
            string += f'"passenger_name": "{passenger["name"]}",\n'
            string += f'"station": "{passenger["station"]}",\n'
        return string


stations = ["King's Cross", "Diagon Alley", "Hogsmeade Village", "Hogwarts"]
train = Train("Hogwarts Express", stations)

locomotive = TrainCar(0)
car1 = TrainCar(1)
car2 = TrainCar(2)
car3 = TrainCar(3)

passenger_boarding = {"King's Cross": ["Harry Potter", "Hermione Granger"], "Diagon Alley": ["Ron Weasley", "Ginny Weasley"]}
passenger_exit = {"Hogsmeade Village": "Harry Potter"}

for i in range(len(stations)):
    train.move_to_next_station()


for station in stations:
    if station in passenger_boarding:
        for passenger in passenger_boarding[station]:
            train.add_passenger(passenger)
            print(f"{passenger} boarded the train at {station}.")

    if station in passenger_exit:
        train.exit_passenger(passenger_exit[station])
        print(f"{passenger_exit[station]} left the train at {station}.")
