import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_23.swapi import Planets


@pytest.fixture
def planets():
    yield Planets()