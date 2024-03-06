import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_18.magic_methods import TrainCar


@pytest.mark.parametrize("passenger,expected", [
    ({"name": "Test Passenger", "destination": "Test City", "place": 3}, 3),
    ({"name": "Another Passenger", "destination": "Another City", "place": 4}, 4)])
def test_add_passenger(populated_car, passenger, expected):
    populated_car.add_passenger(passenger)
    assert len(populated_car) == expected


@pytest.mark.smoke
def test_car_str(populated_car):
    result = str(populated_car)
    assert "John Doe" in result and "Jane Doe" in result


@pytest.mark.regression
class TestTrain:
    def test_adding_car(self, train):
        car = TrainCar(1)
        train.add_car(car)
        assert len(train) == 1

    def test_train_len(self, train, populated_car):
        train.add_car(populated_car)
        assert len(train) == 1

    def test_train_str(self, train):
        result = str(train)
        assert "Express" in result
