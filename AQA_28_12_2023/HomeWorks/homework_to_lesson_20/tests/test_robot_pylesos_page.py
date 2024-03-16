def test_page_title(robot_pylesos_page):
    assert "Роботи-пилососи" in robot_pylesos_page.page_title()


def test_brand_filter(robot_pylesos_page):
    robot_pylesos_page.click_brand_filter_first_item()
    assert robot_pylesos_page.selected_filter_displayed()


def test_clear_brand_filter(robot_pylesos_page):
    robot_pylesos_page.click_brand_filter_first_item()
    robot_pylesos_page.selected_filter_displayed()
    robot_pylesos_page.click_clear_brand_filter_button()
    assert not robot_pylesos_page.selected_filter_displayed()

def test_filter_dropdown(robot_pylesos_page):
    robot_pylesos_page.click_filter_dropdown()
    robot_pylesos_page.click_filter_dropdown_hit()
    assert robot_pylesos_page.hit_label_displayed()


def test_type_filter(robot_pylesos_page):
    robot_pylesos_page.click_type_filter_zi_stantsiey()
    assert robot_pylesos_page.text_of_selected_type_filter() == "База автовивантаження сміття в комплекті: Так"

