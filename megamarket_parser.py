import json
from urllib import parse
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions


BASEURL = 'https://megamarket.ru'


def get_pages_html(url, model_name):
    # options = Options()
    # options.add_argument('--ignore-certificate-errors')
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    ITEMS = {}
    ITEMS_PRICES = []
    try:
        driver.get(url=url)
        WebDriverWait(driver, 60).until(
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
    stop_running = False
    for item in items_divs:
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
        items[int(item_price)] = link
        prices.append(int(item_price))
        # items.append({
        #     'Наименование': item_title,
        #     'Цена': int(item_price),
        # # 'Сумма бонуса': bonus,
        # # 'Процент бонуса': bonus_percent,
        #     'Ссылка на товар': link
        # })
    return True


# def save_excel(data: list):
#     """сохранение результата в excel файл"""
#     # df = pd.DataFrame(data)
#     # print(df['Цена'])
#     print(min(data))
    # writer = pd.ExcelWriter(f'{filename}.xlsx')
    # df.to_excel(writer, sheet_name='data', index=False)
    # указываем размеры каждого столбца в итоговом файле
    # writer.sheets['data'].set_column(0, 1, width=50)
    # writer.sheets['data'].set_column(1, 2, width=30)
    # writer.sheets['data'].set_column(2, 3, width=8)
    # writer.sheets['data'].set_column(3, 4, width=20)
    # writer.sheets['data'].set_column(4, 5, width=15)
    # writer.close()
    # print(f'Все сохранено в {filename}.xlsx')


def main(target: str):
    # target = input('Введите название товара: ')
    # min_price = input('Минимальная цена (enter, чтобы пропустить): ')
    # min_price = min_price if min_price != '' else '0'
    # max_price = input('Максимальная цена (enter, чтобы пропустить): ')
    # max_price = max_price if max_price != '' else '9999999'
    target_url = f"{BASEURL}/catalog/?q={target}&collectionId=12546"
    filter = {
        # "88C83F68482F447C9F4E401955196697": {"min": int(min_price), "max": int(max_price)},# фильтр по цене
        "4CB2C27EAAFC4EB39378C4B7487E6C9E": ["1"]}# фильтр по наличию товара
    json_data = json.dumps(filter)
    # Кодирование JSON строки для передачи через URL
    url_encoded_data = parse.quote(json_data)
    target_url += '#?filters=' + url_encoded_data

    items, prices = get_pages_html(target_url, target)
    min_item_link = items[min(prices)]
    return min_item_link, min(prices)


if __name__ == '__main__':
    lnk, price = main('iphone 15 128')
    print(lnk)
    print(price)