import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_24.infrastructure import Objects, Book


@pytest.fixture
def objects():
    yield Objects()
