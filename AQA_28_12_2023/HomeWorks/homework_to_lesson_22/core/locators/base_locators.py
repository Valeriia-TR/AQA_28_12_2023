class BaseLocators:
    locator_catalog_tehnika_dlia_domu = ("xpath", '//a[contains(@href, "/tovary-po-ukhodu-za-domom-i-odezhdoy/")]/ancestor::div[@class="popup-catalog__nav-item-container"]')
    locator_catalog_tekhnika_dlya_kukhni = ("xpath", '//a[contains(@href, "/tekhnika-dlya-kukhni/")]/ancestor::div[@class="popup-catalog__nav-item-container"]')
    locator_service_consulting = ("xpath", '//div[@class="AvailableServicesItem"]/div[contains(text(), "Консультація з експертом")]')
    locator_service_testdrive = ("xpath", '//div[@class="AvailableServicesItem"]/div[contains(text(), "Тест-драйв")]')
    locator_service_video_consulting = ("xpath", '//div[@class="AvailableServicesItem"]/div[contains(text(), "Відео консультація")]')
    def __init__(self):
        self.locator_header_cart = ("xpath",'//div[@class="Header-right-buttons__button cart"]/div[@class="Header-right-buttons__button-icon"]')
        self.locator_cart_popup = ("xpath", '//div[@class="HeaderCart__popup-no-items"]')
        self.locator_compare_icon_disabled = ("xpath", '//div[@class="Header-right-buttons__button compare disabled"]')
        self.locator_compare_icon = ("xpath", '//div[@class="Header-right-buttons__button compare"]')
        self.locator_catalog_tehnika_dlia_domu = ("xpath",'//a[contains(@href, "/tovary-po-ukhodu-za-domom-i-odezhdoy/")]/ancestor::div[@class="popup-catalog__nav-item-container"]')
        self.locator_catalog_roboty_pylesosy = ("xpath", '//li[@class="popup-catalog__nav-item-list-sub"]/a[contains(@href, "/roboty-pylesosy/")]')
        self.locator_catalog_tekhnika_dlya_kukhni = ("xpath", '//a[contains(@href, "/tekhnika-dlya-kukhni/")]/ancestor::div[@class="popup-catalog__nav-item-container"]')
        self.locator_catalog_kofevarki = ("xpath", '//li[@class="popup-catalog__nav-item-list-sub"]/a[contains(@href, "/kofevarki/")]')
        self.locator_service_popup_title = ("xpath", '//div[@class="AvailableServicesPopup__container-head-text"]')



