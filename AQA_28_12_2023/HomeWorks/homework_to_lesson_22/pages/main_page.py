from .base_page import BasePage
from .robot_pylesos_page import RobotPylesosPage
from .audio_page import AudioPage
from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainLocators()

    def click_search_field(self):
        self.click_on_element(self.locators.locator_main_page_search_input)

    def text_to_input_field(self, text):
        self.enter_text(self.locators.locator_main_page_search_input, text)

    def click_on_catalog(self):
        self.click_on_element(self.locators.locator_main_page_catalog_button)

    def services_title_present(self):
        return self.element_is_displayed(self.locators.locator_main_page_services_title)

    def services_tittle_text(self):
        return self.get_text(self.locators.locator_main_page_services_title)

    def catalog_button_presence(self):
        return self.element_is_displayed(self.locators.locator_main_page_catalog_button)

    def title_of_search(self):
        return self.get_text(self.locators.locator_macbook_search)

    def language_changing_ru(self):
        return self.click_on_element(self.locators.locator_main_page_ru_language)

    def robot_pylesos_category(self):
        self.click_on_element(self.locators.locator_main_page_robot_pylesos_button)
        return RobotPylesosPage(self.driver)

    def catalog_audio_item(self):
        self.click_on_element(self.locators.locator_main_catalog_audio_item)
        return AudioPage(self.driver)

    def add_cookies(self, name, value):
        return self.cookies.add({'name': name, 'value': value})

    def get_cookie(self, name):
        cookie = self.cookies.get(name)
        print(cookie)
        return cookie['value'] if cookie else None

    def delete_cookie(self, name):
        self.cookies.delete(name)

    def clear_cookies(self):
        self.cookies.clear()

    def localstorage_get_item(self, key):
        try:
            return self.local_storage.get_item(key)
        except:
            return None

    def localstorage_set(self, key, value):
        self.local_storage.set_item(key, value)
        value = self.localstorage_get_item(key)
        print(value)
        return value

    def localstorage_delete(self, key):
        self.local_storage.remove_item(key)
        self.local_storage.clear()

    def connect_button_click(self):
        self.click_on_element(self.locators.locator_connect_button)

    def connect_items_list_visible(self):
        return self.wait_element_visible(self.locators.locator_connect_items_list)
