from .base_locators import BaseLocators


class MainLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_main_page_logo = ('xpath', '//a[@class="Header__container-logo"]')
        self.locator_main_page_catalog_button = ('xpath', '//div[@class="Header-catalog"]')
        self.locator_main_page_search_input = ('xpath', '//input[@class="Header-search__search-input"]')
        self.locator_main_page_services_title = ('xpath', '//div[@class="AvailableServices__head"]')
        self.locator_macbook_search = ('xpath', '//h1[@class="filter__head-title-text"]')
        self.locator_main_page_ru_language = ('xpath', "//div[contains(text(), 'RU')]")
        self.locator_main_page_robot_pylesos_button = (
            'xpath',
            '//div[@class="ScrollSlider__container"]/a[@class="MainCategories__item"]/div[contains(text(), "Роботи-пилососи")]')
        self.locator_main_catalog_audio_item = (
            'xpath',
            '//div[@class="popup-catalog__nav-item-container"]/a[contains(text(), "Аудіо")]')
