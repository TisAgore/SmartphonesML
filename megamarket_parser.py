import json
from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

BASEURL = 'https://megamarket.ru'

def get_pages_html(url: str, model_name: str):
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    ITEMS = {}
    ITEMS_PRICES = []
    try:
        driver.get(url=url)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.TAG_NAME, "html")))
        get_items(driver.page_source, ITEMS, model_name, ITEMS_PRICES)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return ITEMS, ITEMS_PRICES


def get_items(html: str, items: dict, model_name: str, prices: list[int]):
    soup = BeautifulSoup(html, 'html.parser')
    items_divs: list[BeautifulSoup] = soup.find_all('div', class_ = 'catalog-item-regular-desktop')
    if len(items_divs) == 0:
        return False
    for item in items_divs:
        stop_running = False
        link = BASEURL + item.find('a', class_='ddl_product_link').get('href')
        item_price = item.find('div', class_='catalog-item-regular-desktop__price').get_text()
        chars_to_remove = ['\n', '\t', ' ', '₽', '\xa0']
        for char in chars_to_remove:
            item_price = item_price.replace(char, '')
        item_title = item.find('a', class_='catalog-item-regular-desktop__title-link').get('title').lower()
        words_in_model = model_name.split(' ')
        for word in words_in_model:
            if word not in item_title:
                stop_running = True
                break
        if stop_running:
            continue
        if price not in items:
            items[int(item_price)] = link
        prices.append(int(item_price))


def main(model_name: str):
    model_name_url = f"{BASEURL}/catalog/?q={model_name}&collectionId=12546"
    filter = {
        "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]} # фильтр по наличию товара
    json_data = json.dumps(filter)
    # Кодирование JSON строки для передачи через URL
    url_encoded_data = parse.quote(json_data)
    model_name_url += '#?filters=' + url_encoded_data

    items, prices = get_pages_html(model_name_url, model_name)
    min_price = min(prices)
    min_item_link = items[min_price]
    return min_item_link, min_price

if __name__ == '__main__':
    lnk, price = main('iphone 15 128')
    print(lnk)
    print(price)
