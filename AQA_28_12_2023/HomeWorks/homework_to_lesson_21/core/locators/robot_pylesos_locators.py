from .base_locators import BaseLocators


class RobotPylesos(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_robot_pylesos_title = ('xpath', '//h1[@class="catalog-page__head"]')
        self.locator_robot_pylesos_brand_filter_first = ('xpath', '(//div[@class="CatalogBrandFilters__item"])[1]')
        self.locator_robot_pylesos_selected_brand_filter = ('xpath', '//div[@class="CatalogSelectedFiltersItem__text"]')
        self.locator_robot_pylesos_clear_brand_filter_button = ('xpath', '//div[@class="CatalogSelectedFilters__remove"]')
        self.locator_robot_pylesos_filter_dropdown = ('xpath', '//div[@class="FormSelect__input"]')
        self.locator_robot_pylesos_filter_dropdown_hit = ('xpath', "//li[contains(text(), 'Хіт')]")
        self.locator_robot_pylesos_hit_label = ('xpath', "(//div[contains(text(), 'HIT')])[1]")
        self.locator_robot_pylesos_type_filter_zi_stantsiey = ('xpath', "//div[contains(text(), 'Роботи зі станцією вивантаження')]")
        self.locator_robot_pylesos_roborock_checkbox = ('xpath', '//div[@class="FormCheckbox full"]/div[contains(text(), "Roborock")]')
