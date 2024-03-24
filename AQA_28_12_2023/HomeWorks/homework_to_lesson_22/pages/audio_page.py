from .base_page import BasePage
from .navushniki_page import NavushnikiPage
from AQA_28_12_2023.HomeWorks.homework_to_lesson_22.core import AudioLocators


class AudioPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AudioLocators()


    def navushniki_item_presence(self):
        return self.element_is_displayed(self.locators.locator_audio_navushniki_item)

    def get_title(self):
        return self.get_text(self.locators.locator_audio_title)

    def navigate_navushniki_catalog_item(self):
        self.click_on_element(self.locators.locator_audio_navushniki_item)
        return NavushnikiPage(self.driver)

    def click_on_compare_button_first_product(self):
        return self.click_on_element(self.locators.locator_compare_icon_first_product)

    def click_feedback_item(self):
        return self.click_on_element(self.locators.locator_audio_feedback_icon)

    def get_product_card_feedback_title(self):
        return self.get_text(self.locators.locator_audio_product_card_feedback_title)