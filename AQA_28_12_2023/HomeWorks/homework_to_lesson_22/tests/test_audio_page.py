def test_bypass_main_to_audio_page(main_page):
    audio_page_inst = main_page.catalog_audio_item()
    title = audio_page_inst.get_title()
    assert title == "Аудіо"


def test_navushniki_item_presence(audio_page):
    assert audio_page.navushniki_item_presence()


def test_compare_product(audio_page):
    audio_page.click_on_compare_button_first_product()
    assert audio_page.return_compare_icon_class() == "Header-right-buttons__button compare"


def test_feedback_item_displaying(audio_page):
    audio_page.click_feedback_item()
    assert "Відгуки" in audio_page.get_product_card_feedback_title()