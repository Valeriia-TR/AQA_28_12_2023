from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core import BaseLocators


class BasePage:
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)
        self.locators = BaseLocators()
        self.cookies = Cookies(driver)
        self.local_storage = LocalStorage(driver)

    def wait_element_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_on_element(self, locator):
        try:
            element = self.wait_element_clickable(locator)
            element.click()
        except Exception as e:
            raise Exception(f"Error clicking on element with locator: {locator}. Error: {e}")

    def enter_text(self, locator, text):
        try:
            element = self.wait_element_visible(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Error entering text into element with locator: {locator}. Error: {e}")

    def get_text(self, locator):
        try:
            element = self.wait_element_visible(locator)
            return element.text
        except Exception as e:
            raise Exception(f"Error getting text from element with locator: {locator}. Error: {e}")

    def element_presence(self, locator):
        try:
            self.wait_element_present(locator)
            return True
        except:
            return False

    def element_is_displayed(self, locator):
        try:
            self.wait_element_visible(locator).is_displayed()
            return True
        except:
            return False

    def click_enter_key(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def cart_icon_click(self):
        return self.click_on_element(self.locators.locator_header_cart)

    def cart_popup_displayed(self):
        return self.element_is_displayed(self.locators.locator_cart_popup)

    def return_compare_icon_class(self):
        button = self.wait_element_present(self.locators.locator_compare_icon)
        return button.get_attribute('class')

    def navigate_to_category_tehnika_dlia_domu(self):
        tehnika_dlia_domu = self.wait_element_present(self.locators.locator_catalog_tehnika_dlia_domu)
        actions = ActionChains(self.driver)
        actions.move_to_element(tehnika_dlia_domu).perform()
        roboty_pylesosy = self.wait_element_present(self.locators.locator_catalog_roboty_pylesosy)
        return roboty_pylesosy.is_displayed()

    def navigate_to_category_tekhnika_dlya_kukhni(self):
        tekhnika_dlya_kukhni = self.wait_element_present(self.locators.locator_catalog_tekhnika_dlya_kukhni)
        actions = ActionChains(self.driver)
        actions.move_to_element(tekhnika_dlya_kukhni).perform()
        kofevarki = self.wait_element_present(self.locators.locator_catalog_kofevarki)
        return kofevarki.is_displayed()

    def navigate_to_category(self, category, items_list):
        category_object = self.wait_element_present(category)
        actions = ActionChains(self.driver)
        actions.move_to_element(category_object).perform()
        for item in items_list:
            item_object = self.wait_element_present(item)
            assert item_object.is_displayed()


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def add(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def get(self, name):
        return self.driver.get_cookie(name)


    def delete(self, name):
        self.driver.delete_cookie(name)

    def clear(self):
        self.driver.delete_all_cookies()


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set_item(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def get_item(self, key):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def remove_item(self, key):
        self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")

