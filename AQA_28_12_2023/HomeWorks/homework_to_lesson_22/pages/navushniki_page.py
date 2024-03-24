from .base_page import BasePage
from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core import NavushnikiLocators

class NavushnikiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavushnikiLocators()


    def get_title(self):
        return self.get_text(self.locators.locator_navushniki_title)

    def click_on_sale_filter(self):
        return self.click_on_element(self.locators.locator_navushniki_filter_sale)

    def get_selected_filter(self):
        return self.get_text(self.locators.locator_navushniki_selected_filter)

    def selected_filter_displayed(self):
        return self.element_is_displayed(self.locators.locator_navushniki_selected_filter)

    def remove_selected_filter(self):
        return self.click_on_element(self.locators.locator_navushniki_remove_selected_filter_button)

    def click_on_price_filter_highest_price(self):
        return self.click_on_element(self.locators.locator_navushniki_highest_price_filter)

    def input_highest_price_filter(self):
        return self.enter_text(self.locators.locator_navushniki_highest_price_filter, "100")

    def click_on_dropdown_filter(self):
        return self.click_on_element(self.locators.locator_navushniki_dropdown_filter)

    def click_dropdown_filter_option_price_from_highest(self):
        return self.click_on_element(self.locators.locator_navushniki_dropdown_filter_option_price_from_highest)

    def click_price_filter_submit_button(self):
        return self.click_on_element(self.locators.locator_navushniki_price_filter_submit_button)

    def get_first_product_price(self):
        price = self.get_text(self.locators.locator_navushniki_first_product_price)
        return int(''.join(c for c in price if c.isdigit()))


