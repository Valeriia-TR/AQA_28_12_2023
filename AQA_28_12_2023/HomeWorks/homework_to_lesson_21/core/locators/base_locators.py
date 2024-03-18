class BaseLocators:
    def __init__(self):
        self.locator_header_cart = (
            "xpath",
            '//div[@class="Header-right-buttons__button cart"]/div[@class="Header-right-buttons__button-icon"]')
        self.locator_cart_popup = ("xpath", '//div[@class="HeaderCart__popup-no-items"]')
        self.locator_compare_icon_disabled = ("xpath", '//div[@class="Header-right-buttons__button compare disabled"]')
        self.locator_compare_icon = ("xpath", '//div[@class="Header-right-buttons__button compare"]')
