from time import sleep as pause
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def parse_characteristics_page(driver: uc.Chrome, url, model_name):
    """ Парсит страницу товара по ссылке."""
    try:
        driver.get(url=url)
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.TAG_NAME, "html")))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    soup: BeautifulSoup = BeautifulSoup(driver.page_source, 'lxml')
    items: list[BeautifulSoup] = soup.find_all('div', class_='catalog-product')

    notebook = {}
    prices = []
    for item in items:
        skip_item = False
        name = item.find('a', class_="catalog-product__name").text.split(' [')[0].lower()
        href = item.find('a', class_="catalog-product__name").get('href')
        price = item.find('div', class_="product-buy__price").text.replace(' ', '').split('₽')[0]
        price = int(price)

        model_words = model_name.split(' ')
        for word in model_words:
            if word not in name:
                skip_item = True
                break
        if skip_item == True:
            continue
        avail = item.find('span', class_="available").text
        if avail != 'В наличии ':
            continue
        
        prices.append(price)
        if price not in notebook:
            notebook[price] = href

    return notebook, prices


def main(model_name: str):

    driver = uc.Chrome()
    url_to_parse = f'https://www.dns-shop.ru/search/?q={model_name.replace(' ', '+')}&category=17a8a01d16404e77'

    note, prices = parse_characteristics_page(driver, url_to_parse, model_name)

    min_price = min(prices)
    min_item_link = note[min_price]
    return min_item_link, min_price