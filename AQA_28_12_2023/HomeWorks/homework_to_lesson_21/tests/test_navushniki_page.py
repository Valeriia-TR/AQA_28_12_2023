
def test_bypass_main_to_navushniki(main_page):
    audio_page_inst = main_page.catalog_audio_item()
    navushniki_page_inst = audio_page_inst.navigate_navushniki_catalog_item()
    assert navushniki_page_inst.get_title() == "Навушники"


def test_sale_filter(navushniki_page):
    navushniki_page.click_on_sale_filter()
    assert navushniki_page.get_selected_filter() == "Акція"


def test_remove_selected_filter(navushniki_page):
    navushniki_page.click_on_sale_filter()
    navushniki_page.remove_selected_filter()
    assert navushniki_page.selected_filter_displayed() is False


def test_price_range_filter(navushniki_page):
    navushniki_page.click_on_price_filter_highest_price()
    navushniki_page.input_highest_price_filter()
    navushniki_page.click_price_filter_submit_button()
    navushniki_page.click_on_dropdown_filter()
    navushniki_page.click_dropdown_filter_option_price_from_highest()
    assert navushniki_page.get_first_product_price() < 5200
