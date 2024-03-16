from .base_page import BasePage



class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_main_page_logo = ('xpath', '//a[@class="Header__container-logo"]')
        self.locator_main_page_catalog_button = ('xpath', '//div[@class="Header-catalog"]')
        self.locator_main_page_search_input = ('xpath', '//input[@class="Header-search__search-input"]')
        self.locator_main_page_services_title = ('xpath', '//div[@class="AvailableServices__head"]')
        self.locator_macbook_search = ('xpath', '//h1[@class="filter__head-title-text"]')
        self.locator_main_page_ru_language = ('xpath', "//div[contains(text(), 'RU')]")

    def click_search_field(self):
        self.click_on_element(self.locator_main_page_search_input)

    def text_to_input_field(self, text):
        self.enter_text(self.locator_main_page_search_input, text)

    def click_on_catalog(self):
        self.click_on_element(self.locator_main_page_catalog_button)

    def services_title_present(self):
        return self.element_is_displayed(self.locator_main_page_services_title)

    def services_tittle_text(self):
        return self.get_text(self.locator_main_page_services_title)

    def catalog_button_presence(self):
        return self.element_is_displayed(self.locator_main_page_catalog_button)

    def title_of_search(self):
        return self.get_text(self.locator_macbook_search)

    def language_changing_ru(self):
        return self.click_on_element(self.locator_main_page_ru_language)