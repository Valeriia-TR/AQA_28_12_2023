
def test_services_title_presence(main_page):
    assert main_page.services_title_present()


def test_services_title_text(main_page):
    assert main_page.services_tittle_text() == "Наші сервіси"


def test_language_changing(main_page):
    main_page.language_changing_ru()
    assert main_page.services_tittle_text() == "Наши сервисы"


def test_catalog_button_presence(main_page):
    assert main_page.catalog_button_presence()


def test_search_input_field(main_page):
    main_page.click_search_field()
    main_page.text_to_input_field("macbook")
    main_page.click_enter_key()
    assert "macbook" in main_page.title_of_search()


def test_cart_popup_displaing(main_page):
    main_page.cart_icon_click()
    assert main_page.cart_popup_displayed()