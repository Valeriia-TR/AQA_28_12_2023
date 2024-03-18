from .base_page import BasePage
from AQA_28_12_2023.HomeWorks.homework_to_lesson_21.core import RobotPylesos


class RobotPylesosPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RobotPylesos()

    def page_title(self):
        return self.get_text(self.locators.locator_robot_pylesos_title)

    def click_brand_filter_first_item(self):
        return self.click_on_element(self.locators.locator_robot_pylesos_brand_filter_first)

    def selected_filter_displayed(self):
        return self.element_is_displayed(self.locators.locator_robot_pylesos_selected_brand_filter)

    def click_clear_brand_filter_button(self):
        return self.click_on_element(self.locators.locator_robot_pylesos_clear_brand_filter_button)

    def click_filter_dropdown(self):
        return self.click_on_element(self.locators.locator_robot_pylesos_filter_dropdown)

    def click_filter_dropdown_hit(self):
        return self.click_on_element(self.locators.locator_robot_pylesos_filter_dropdown_hit)

    def hit_label_displayed(self):
        return self.element_is_displayed(self.locators.locator_robot_pylesos_hit_label)

    def click_type_filter_zi_stantsiey(self):
        return self.click_on_element(self.locators.locator_robot_pylesos_type_filter_zi_stantsiey)

    def text_of_selected_type_filter(self):
        return self.get_text(self.locators.locator_robot_pylesos_selected_brand_filter)

    def click_filter_checkbox_roborock(self):
        self.click_on_element(self.locators.locator_robot_pylesos_roborock_checkbox)
