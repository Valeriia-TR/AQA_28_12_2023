import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_18.magic_methods import TrainCar, Train


@pytest.fixture
def train():
    train = Train("Express")
    return train


@pytest.fixture(scope="module")
def populated_car():
    car = TrainCar(1)
    car.add_passenger({"name": "John Doe", "destination": "City A", "place": 1})
    car.add_passenger({"name": "Jane Doe", "destination": "City B", "place": 2})
    return car



