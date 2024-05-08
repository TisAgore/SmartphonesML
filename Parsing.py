# %pip install selenium
# %pip install undetected-chromedriver
# !pip install selenium
# !apt-get update
# !apt install chromium-chromedriver
import json
import re
import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium.common import NoSuchWindowException
from selenium import webdriver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

# def load_cookies():
#     with open("cookie.json", encoding="utf-8", errors="ignore") as config_file:
#         cookies = json.load(config_file)
#     return [[cookie["name"], cookie["value"]] for cookie in cookies]

def parse(model_name, driver):
    global smartphones
    url = f"https://megamarket.ru/catalog/?q={model_name.replace(' ', '+')}&collectionId=12546"
    print(model_name)
    new_model_name = model_name.replace('(','')
    new_model_name = new_model_name.replace(')','')
    new_model_name = new_model_name.replace(' 5g','')
    new_model_name = new_model_name.replace(' ram','')
    new_model_name = new_model_name.replace('gb','')
    new_model_name = new_model_name.replace(' + ','/')
    new_model_name = new_model_name.replace(' plus','')
    words_in_model = new_model_name.split(' ')
    print(words_in_model)
    driver.get(url)
    html = BeautifulSoup(driver.page_source, "html.parser")
    catalog_items = html.find("div", class_ = "catalog-items-list")
    # print(catalog_items)

    if catalog_items is None:
        print(f"Нет каталога | Рекурсия на странице {url}")
        smartphones = smartphones.drop(smartphones[smartphones['model'].isin([model_name])].index)
        return False
        # return parse(model_name, driver)

    # items = catalog_items.find_all("div", class_ = "catalog-item-regular-desktop ddl_product catalog-item-desktop")
    items = catalog_items.find_all("div", class_ = "catalog-item-mobile ddl_product")
    # print(items)
    if len(items) == 0:
        print(f"0 Предметов | Рекурсия на странице {url}")
        smartphones = smartphones.drop(smartphones[smartphones['model'].isin([model_name])].index)
        return False
        # return parse(model_name, driver)

    for item in items:
      count_model = 0
      # print(item.find("a", class_="ddl_product_link"))
      item_title = item.find("div", class_="item-title").a.get('title').strip()[9:].lower()
      # print(item.find("div", class_="item-title"))
      # item_url = "https://megamarket.ru" + item.find("a", class_="ddl_product_link").get("href").strip()
      for model_word in words_in_model:
        if model_word in item_title:
          count_model += 1
      print(count_model, len(words_in_model))
      if count_model == len(words_in_model):
        return True
      print(item_title)

    smartphones = smartphones.drop(smartphones[smartphones['model'].isin([model_name])].index)
    return False


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--user-agent={user_agent}")
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # options.binary_location = "\Application\chrome.exe"
    # print(options.binary_location)
    driver = webdriver.Chrome(options=chrome_options)
    # driver.get("https://megamarket.ru/")
    # cookies = load_cookies()
    # print("Подгрузка куки файлов")
    # for name, value in cookies:
    #     driver.add_cookie({"name": name, "value": value})
    # print("Куки подгружены")
    driver.get("https://megamarket.ru/")
    print("Start")

    try:
        # current_page = 1
        for model_name in smartphones['model']:
        # while current_page != pages + 1:
          print(model_name)
          result = parse(model_name, driver)
            # if result:
            #     print(f"{time.strftime('%H:%M:%S %d/%m/%Y')} | {current_page} / {pages}")
            # else:
            #     break
            # current_page += 1

        print("Все товары просмотрены")

    except Exception as e:
        print(e)
    finally:
        try:
            driver.close()
            driver.quit()
        except NoSuchWindowException:
            driver.quit()

    print("Finish")

main()
