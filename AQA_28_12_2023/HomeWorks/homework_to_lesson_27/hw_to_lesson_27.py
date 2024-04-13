import requests
from bs4 import BeautifulSoup
import json


class ProductScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.product_links = []

    def get_soup(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"An error occurred while getting soup: {e}")
            return None

    def scrape_pagination_links(self):
        soup = self.get_soup(self.base_url)
        if soup:
            pagination = soup.find('ul', class_="pagination")
            if pagination:
                return [link['href'] for link in pagination.find_all('a', href=True) if
                        link['href'] not in self.base_url]
        return []

    def scrape_product_links(self, soup):
        product_links = []
        if soup:
            products = soup.find('div', class_="products-block row row-flex")
            if products:
                product_links = [a['href'] for a in products.find_all('a', class_="product-thumb__name", href=True)]
        return product_links

    def scrape_all_products(self):
        initial_links = self.scrape_product_links(self.get_soup(self.base_url))
        self.product_links.extend(initial_links)
        pagination_links = self.scrape_pagination_links()
        for link in pagination_links:
            page_soup = self.get_soup(link)
            page_links = self.scrape_product_links(page_soup)
            self.product_links.extend(page_links)

    def save_links_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.product_links, file, indent=4)

    def scrape_product_names(self, soup):
        product_names = []
        if soup:
            products = soup.find_all('div', class_='product-thumb__caption')
            for product in products:
                name_tag = product.find('a', class_='product-thumb__name')
                if name_tag:
                    product_names.append(name_tag.get_text(strip=True))
        return product_names

    def scrape_all_product_info(self):
        pagination_links = self.scrape_pagination_links()
        first_page_soup = self.get_soup(self.base_url)
        if first_page_soup:
            product_links = self.scrape_product_links(first_page_soup)
            if product_links:
                self.product_links.extend(product_links)
            product_names = self.scrape_product_names(first_page_soup)
        else:
            product_names = []

        for page_link in pagination_links:
            soup = self.get_soup(page_link)
            if soup:
                product_links = self.scrape_product_links(soup)
                if product_links:
                    self.product_links.extend(product_links)
                product_names.extend(self.scrape_product_names(soup))

        return product_names

    def scrape_product_prices(self, soup):
        product_prices = []
        if soup:
            price_divs = soup.find_all('div', class_='product-thumb__price')
            for div in price_divs:
                price = div.get('data-price', None)
                if price:
                    product_prices.append(float(price))
                else:
                    price_text = div.text.strip().replace('₴', '').replace(',', '.')
                    product_prices.append(float(price_text))
        return product_prices

    def scrape_all_product_info(self):
        pagination_links = self.scrape_pagination_links()
        first_page_soup = self.get_soup(self.base_url)
        product_info = []

        if first_page_soup:
            product_links = self.scrape_product_links(first_page_soup)
            self.product_links.extend(product_links)
            product_names = self.scrape_product_names(first_page_soup)
            product_prices = self.scrape_product_prices(first_page_soup)
            product_info.extend(zip(product_names, product_prices))

        for page_link in pagination_links:
            soup = self.get_soup(page_link)
            if soup:
                product_links = self.scrape_product_links(soup)
                self.product_links.extend(product_links)
                product_names = self.scrape_product_names(soup)
                product_prices = self.scrape_product_prices(soup)
                product_info.extend(zip(product_names, product_prices))

        return product_info


scraper = ProductScraper('https://zoocomplex.com.ua/ua-tovary-dlya-gryzunov/')
scraper.scrape_all_products()
scraper.save_links_to_file('product_links.json')
product_names = scraper.scrape_all_product_info()
all_product_info = scraper.scrape_all_product_info()

print(f'List of Pagination Links: {scraper.scrape_pagination_links()}')
print(f"Total product links scraped: {len(scraper.product_links)}")
print(f"Total product names scraped: {product_names}")
print(f"Total product information scraped: {len(all_product_info)}")
for name, price in all_product_info:
    print(f'{name}: {price}')
