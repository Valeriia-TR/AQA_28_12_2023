import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core.locators import BaseLocators
from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core.datasample import *

def test_services_title_presence(main_page):
    assert main_page.services_title_present()


def test_services_title_text(main_page):
    assert main_page.services_tittle_text() == "Наші сервіси"


def test_language_changing(main_page):
    main_page.language_changing_ru()
    assert main_page.services_tittle_text() == "Наши сервисы"


def test_catalog_button_presence(main_page):
    assert main_page.catalog_button_presence()


def test_search_input_field(main_page):
    main_page.click_search_field()
    main_page.text_to_input_field("macbook")
    main_page.click_enter_key()
    assert "macbook" in main_page.title_of_search()


def test_cart_popup_displaing(main_page):
    main_page.cart_icon_click()
    assert main_page.cart_popup_displayed()


def test_cookies_add(main_page):
    main_page.add_cookies("test_cookie", "12345")
    cookie_value = main_page.get_cookie("test_cookie")
    assert cookie_value == "12345"


def test_delete_cookie(main_page):
    main_page.delete_cookie("test_cookie")
    cookie_value = main_page.get_cookie("test_cookie")
    assert cookie_value is None


def test_localstorage_setting(main_page):
    set_value = main_page.localstorage_set("test_localstorage", "test value")
    assert set_value == "test value"


def test_localstorage_set_value_delete(main_page):
    main_page.localstorage_delete("test_localstorage")
    test_value = main_page.localstorage_get_item("test_localstorage")
    assert test_value is None


def test_navigate_to_category_tehnika_dlia_domu(main_page):
    assert main_page.navigate_to_category_tehnika_dlia_domu()


def test_navigate_to_category_tekhnika_dlya_kukhni(main_page):
    assert main_page.navigate_to_category_tekhnika_dlya_kukhni()


@pytest.mark.parametrize('category,list_of_subcategories',
                         [(BaseLocators.locator_catalog_tehnika_dlia_domu,tehnika_dlia_domu_list),
                          (BaseLocators.locator_catalog_tekhnika_dlya_kukhni,tekhnika_dlya_kukhni_list)])
def test_navigate_to_category_tekhnika_dlya_kukhni(main_page,category,list_of_subcategories):
    main_page.navigate_to_category(category, list_of_subcategories)


@pytest.mark.parametrize("button_locator, expected_popup_title", services_data)
def test_service_popups(main_page, button_locator, expected_popup_title):
    button = main_page.wait_element_clickable(button_locator)
    main_page.click_on_element(button)
    popup_title = main_page.locators.locator_service_popup_title
    popup_title_text = main_page.get_text(popup_title)
    assert popup_title_text == expected_popup_title


def test_connect_button(main_page):
    main_page.connect_button_click()
    main_page.connect_items_list_visible()
    assert True




