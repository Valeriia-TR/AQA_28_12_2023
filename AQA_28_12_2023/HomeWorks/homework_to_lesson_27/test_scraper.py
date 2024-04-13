import pytest
from AQA_28_12_2023.HomeWorks.homework_to_lesson_27.hw_to_lesson_27 import ProductScraper

@pytest.fixture
def scraper():
    return ProductScraper("https://zoocomplex.com.ua/ua-tovary-dlya-gryzunov/")

def test_get_soup(scraper):
    soup = scraper.get_soup(scraper.base_url)
    assert soup is not None, "get_soup should return a BeautifulSoup object, not None"

def test_pagination_links(scraper):
    links = scraper.scrape_pagination_links()
    assert type(links) is list, "scrape_pagination_links should return a list"

def test_product_links(scraper):
    soup = scraper.get_soup(scraper.base_url)
    links = scraper.scrape_product_links(soup)
    assert type(links) is list, "scrape_product_links should return a list"

def test_all_products(scraper):
    scraper.scrape_all_products()
    assert len(scraper.product_links) > 0, "scrape_all_products should find at least one product"

def test_save_links_to_file(scraper, tmp_path):
    file = tmp_path / "links.json"
    scraper.scrape_all_products()
    scraper.save_links_to_file(file)
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    assert len(data) > 0, "save_links_to_file should write data to the file"
