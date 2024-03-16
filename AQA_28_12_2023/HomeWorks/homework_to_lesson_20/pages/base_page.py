from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)

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
