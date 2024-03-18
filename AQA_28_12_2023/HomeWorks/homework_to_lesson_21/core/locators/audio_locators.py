from .base_locators import BaseLocators


class AudioLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_audio_navushniki_item = ("xpath", '//div[@class="catalog-category__body-grid"]//a[contains(text(), "Навушники")]')
        self.locator_audio_title = ("xpath", '//div[@class="catalog-category"]/h1')
        self.locator_compare_icon_first_product = ("xpath", '(//div[@class="product-item__compare-icon"])[1]')
        self.locator_audio_feedback_icon = ("xpath", '(//div[@class="product-item__rating-count"])[1]')
        self.locator_audio_product_card_feedback_title = ("xpath", '//div[@class="ProductCardComments"]/h1')