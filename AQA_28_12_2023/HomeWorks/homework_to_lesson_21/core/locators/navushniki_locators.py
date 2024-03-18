from .base_locators import BaseLocators


class NavushnikiLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_navushniki_title = ("xpath", '//div[@class="catalog-page"]/h1')
        self.locator_navushniki_filter_sale = ("xpath", '//div[@class="CatalogFiltersBadges__item-text"][contains(text(), "Акція")]')
        self.locator_navushniki_selected_filter = ("xpath", '//div[@class="CatalogSelectedFiltersItem"]')
        self.locator_navushniki_remove_selected_filter_button = ("xpath", '//div[@class="CatalogSelectedFilters__remove"]')
        self.locator_navushniki_highest_price_filter = ("xpath", '//div[@class="CatalogFiltersPrice__top"]/input[@class="CatalogFiltersPrice__top-max"]')
        self.locator_navushniki_dropdown_filter = ("xpath", '//div[@class="FormSelect__input"]')
        self.locator_navushniki_dropdown_filter_option_price_from_highest = ("xpath", '//li[contains(text(), "Від дорогих до дешевих")]')
        self.locator_navushniki_price_filter_submit_button = ("xpath", '//div[@class="CatalogFiltersPrice__button"]')
        self.locator_navushniki_first_product_price = ("xpath", '(//div[@class="ProductItem__bottom-price-new"])[1]')