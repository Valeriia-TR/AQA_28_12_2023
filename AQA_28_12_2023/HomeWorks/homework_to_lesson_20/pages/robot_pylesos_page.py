from selenium.webdriver.common.by import By

from .base_page import BasePage


class RobotPylesosPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_robot_pylesos_title = ('xpath', '//h1[@class="catalog-page__head"]')
        self.locator_robot_pylesos_brand_filter_first = ('xpath', '(//div[@class="CatalogBrandFilters__item"])[1]')
        self.locator_robot_pylesos_selected_brand_filter = ('xpath', '//div[@class="CatalogSelectedFiltersItem__text"]')
        self.locator_robot_pylesos_clear_brand_filter_button = ('xpath', '//div[@class="CatalogSelectedFilters__remove"]')
        self.locator_robot_pylesos_filter_dropdown = ('xpath', '//div[@class="FormSelect__input"]')
        self.locator_robot_pylesos_filter_dropdown_hit = ('xpath', "//li[contains(text(), 'Хіт')]")
        self.locator_robot_pylesos_hit_label = ('xpath', "(//div[contains(text(), 'HIT')])[1]")
        self.locator_robot_pylesos_type_filter_zi_stantsiey = ('xpath', "//div[contains(text(), 'Роботи зі станцією вивантаження')]")

    def page_title(self):
        return self.get_text(self.locator_robot_pylesos_title)

    def click_brand_filter_first_item(self):
        return self.click_on_element(self.locator_robot_pylesos_brand_filter_first)

    def selected_filter_displayed(self):
        return self.element_is_displayed(self.locator_robot_pylesos_selected_brand_filter)

    def click_clear_brand_filter_button(self):
        return self.click_on_element(self.locator_robot_pylesos_clear_brand_filter_button)

    def click_filter_dropdown(self):
        return self.click_on_element(self.locator_robot_pylesos_filter_dropdown)

    def click_filter_dropdown_hit(self):
        return self.click_on_element(self.locator_robot_pylesos_filter_dropdown_hit)

    def hit_label_displayed(self):
        return self.element_is_displayed(self.locator_robot_pylesos_hit_label)

    def click_type_filter_zi_stantsiey(self):
        return self.click_on_element(self.locator_robot_pylesos_type_filter_zi_stantsiey)

    def text_of_selected_type_filter(self):
        return self.get_text(self.locator_robot_pylesos_selected_brand_filter)