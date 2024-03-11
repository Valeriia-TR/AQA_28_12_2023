import time
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    browser = webdriver.Chrome()
    browser.get(url="https://metro.zakaz.ua/uk/")
    browser.maximize_window()
    yield browser
    browser.quit()


def test_status_code(setup):
    browser = setup
    current_url = browser.current_url
    response = requests.get(current_url)
    assert response.status_code == 200


def test_sales_page(setup):
    browser = setup
    browser.find_element(
        by=By.XPATH,
        value="//li[@title='Акційні пропозиції']"
    ).click()
    expected_text = "Акційні пропозиції"
    wait = WebDriverWait(browser, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h1"), expected_text))
    element_text = browser.find_element(
        by=By.XPATH,
        value="//h1").text
    assert expected_text in element_text


def test_search_input_box(setup):
    browser = setup
    browser.find_element(
        by=By.XPATH,
        value="//input[@data-testid='searchBoxInput']"
    ).send_keys("Хліб")
    browser.find_element(
        by=By.CSS_SELECTOR,
        value="[data-testid='loupe']"
    ).click()
    expected_text = "Хліб"
    wait = WebDriverWait(browser, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '(//span[@data-testid="product_tile_title"])[1]'), expected_text))
    element_text = browser.find_element(
        by=By.XPATH,
        value='(//span[@data-testid="product_tile_title"])[1]').text
    assert expected_text in element_text


def test_pagination(setup):
    browser = setup
    browser.find_element(
        by=By.XPATH,
        value="//li[@title='Випічка']"
    ).click()
    browser.implicitly_wait(5)
    first_product_title_page_1 = browser.find_element(
        by=By.XPATH,
        value='//div[@class="jsx-ebc81387b8a52f64 ProductsBox__listItem"][1]'
    ).text
    browser.find_element(
        by=By.XPATH,
        value="//a[@class='Pagination__item' and text()='5']"
    ).click()
    time.sleep(2)
    first_product_title_page_5 = browser.find_element(
        by=By.XPATH,
        value='//div[@class="jsx-ebc81387b8a52f64 ProductsBox__listItem"][1]'
    ).text
    assert first_product_title_page_1 != first_product_title_page_5


def test_filter_lowest_price(setup):
    browser = setup
    browser.implicitly_wait(5)
    browser.find_element(
        by=By.XPATH,
        value="//li[@title='Акційні пропозиції']"
    ).click()
    browser.implicitly_wait(5)
    browser.find_element(
        by=By.XPATH,
        value='//div[@data-testid="sort-button"]'
    ).click()
    browser.find_element(
        by=By.XPATH,
        value='//div[@data-testid="price_asc"]'
    ).click()
    price_of_first_product = browser.find_element(
        by=By.XPATH,
        value='(//span[@class="jsx-ed1ae448ea3f5172 Price__value_caption Price__value_discount"])[1]'
    ).text
    price_of_second_product = browser.find_element(
        by=By.XPATH,
        value='(//span[@class="jsx-ed1ae448ea3f5172 Price__value_caption Price__value_discount"])[2]'
    ).text

    price_of_fifteenth_product = browser.find_element(
        by=By.XPATH,
        value='(//span[@class="jsx-ed1ae448ea3f5172 Price__value_caption Price__value_discount"])[15]'
    ).text

    assert float(price_of_first_product) <= float(price_of_second_product) and float(price_of_first_product) <= float(price_of_fifteenth_product)

