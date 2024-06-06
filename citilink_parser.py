from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup


CITILINK_URL = "https://www.citilink.ru"

class ParserError(Exception):
    pass

def get_html(url: str, model_name: str):
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
        raise ParserError()
    finally:
        driver.close()
        driver.quit()
    return ITEMS, ITEMS_PRICES

def get_items(html: str, items: dict, model_name: str, prices: list[int]):
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    items: list[BeautifulSoup] = soup.find_all('div', class_ = 'app-catalog-1bogmvw')
    for item in items:
        kip_item = False
        name = item.find('div', class_ = 'app-catalog-oacxam').get_text().lower()
        url = CITILINK_URL + item.find('a', class_ = 'app-catalog-1k0cnlg').get("href")
        price = item.find('span', class_ = 'app-catalog-0')
        models_words = model_name.split(' ')
        for word in models_words:
            if word not in name or price is None:
                skip_item = True
                break
        if skip_item == True:
            continue
        price = int(price.get_text())
        prices.append(price)
        items[price] = url
    

def main(model_name: str):
    citilink_smartphone_url = CITILINK_URL + f"/search/?text={model_name.replace(' ', '+')}&menu_id=214"

    items, prices = get_html(citilink_smartphone_url, model_name)
    min_price = min(prices)
    min_item_link = items[min_price]
    return min_item_link, min_price
