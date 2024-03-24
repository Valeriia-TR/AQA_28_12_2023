import pytest
from selenium import webdriver
from AQA_28_12_2023.HomeWorks.homework_to_lesson_20.pages.main_page import MainPage
from AQA_28_12_2023.HomeWorks.homework_to_lesson_20.pages.robot_pylesos_page import RobotPylesosPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get("https://wo.ua/ua/")
    yield MainPage(driver)
    driver.quit()

@pytest.fixture
def robot_pylesos_page(driver):
    driver.get("https://wo.ua/ua/roboty-pylesosy/")
    yield RobotPylesosPage(driver)
    driver.quit()
