import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core.datasample import category_data


@pytest.mark.parametrize("url_path, expected_title", category_data)
def test_categories_pages(driver, url_path, expected_title):
    driver.get(f"https://wo.ua/ua{url_path}")
    assert expected_title in driver.title
