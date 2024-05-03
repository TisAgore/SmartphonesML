import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
%pip install selenium
%pip install undetected-chromedriver
!pip install selenium
!apt-get update 
!apt install chromium-chromedriver

RANDOM_SEED = 400220401

smartphones = pd.read_csv('smartphones - smartphones.csv')

def check_column(card_str_value, column_name, *args):
  # try:
    if type(card_str_value) == float:
      false_id = smartphones.loc[smartphones[column_name].isin([card_str_value]), column_name].index
      smartphones.loc[false_id, column_name] = np.nan
    else:
      if column_name not in card_str_value:
        # print(column_name, card_str_value)
        # print(card_str_value)
        false_id = smartphones.loc[smartphones[column_name].isin([card_str_value]), column_name].index
        false_os = False
        search_words = np.append(np.array(smartphones.columns), ['inbuilt', 'a1', 'snapdragon'])
        if column_name == 'os':
          for column in np.array(smartphones.columns):
            if column in card_str_value:
              false_os = True
              break
          if false_os == False:
            return card_str_value
        # print(falsh_id)
        # false_elem = smartphones.loc[false_id, 'card'].iloc[0]
        # print(smartphones.loc[false_id, column_name])
        # print(column_name, card_str_value)
        # print('camera' in card_str_value)
        if 'camera' in card_str_value:
          smartphones.loc[false_id, 'camera'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        elif 'processor' in card_str_value or 'a1' in card_str_value:
          smartphones.loc[false_id, 'processor'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        elif 'ram' in card_str_value or 'inbuilt' in card_str_value:
          smartphones.loc[false_id, 'ram'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        elif 'battery' in card_str_value:
          smartphones.loc[false_id, 'battery'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        elif 'display' in card_str_value:
          smartphones.loc[false_id, 'display'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        elif 'card' in card_str_value:
          smartphones.loc[false_id, 'card'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        elif 'sim' in card_str_value:
          smartphones.loc[false_id, 'sim'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        else:
          smartphones.loc[false_id, 'os'] = card_str_value
          smartphones.loc[false_id, column_name] = column_name
        # print(smartphones.loc[false_id, :])
        # if column_name != 'os':
        #   smartphones.loc[false_id, column_name] = column_name
        # print(smartphones.loc[false_id, column_name])
        # print(smartphones.loc[falsh_id])
        # smartphones.drop(falsh_id)
      return column_name
  # except:
  #   pass
    # print(math.isnan(card_str_value), column_name)

def clear_os(os_str_value):
  global smartphones
  false_id = smartphones.loc[smartphones['os'].isin([os_str_value]), 'os'].index
  # print(os_str_value)
  if type(os_str_value) == float:
    # print(1)
    smartphones = smartphones.drop(false_id)
  else:
    # print(2)
    if 'android' not in os_str_value and 'os' not in os_str_value:
      # print(3)
      smartphones = smartphones.drop(false_id)


columns_names = np.array(smartphones.columns)
columns_names[0], columns_names[1] = columns_names[1], columns_names[0]
smartphones = smartphones.reindex(columns = columns_names)
# print(columns_names[1:2], columns_names[3:])
for column in np.concatenate((columns_names[1:2], columns_names[3:])):
  smartphones[column] = smartphones[column].str.lower()
for column in columns_names[3:]:
  smartphones[column].apply(func=check_column, args=(column, ))
# print(smartphones['os'].unique())
for column in columns_names[3:]:
  smartphones.dropna()
smartphones.drop_duplicates(subset=['model'])
# print(smartphones['os'].iloc[250:300])
smartphones['os'].apply(clear_os)
smartphones['price'] = smartphones.price.str.replace('₹', '')
smartphones['price'] = smartphones.price.str.replace(',', '').astype('float') * 1.11
# smartphones['sim'] = smartphones.sim.str.split(', ')
# smartphones['ram'] = smartphones.ram.str.split(', ')
# smartphones['display'] = smartphones.display.str.split(', ')
# smartphones['camera'] = smartphones.camera.str.split(' & ')
# smartphones['processor'] = smartphones.processor.str.replace(' Processor', '')
# smartphones['processor'] = smartphones.processor.str.split(', ')
# smartphones['card'].apply(check_memory_card)
# for column in columns_names:
  # print(column)
  # print(smartphones[smartphones[column] == column])
# print(smartphones.processor.str.count('ghz') == 0)
# print(smartphones.loc[(smartphones.processor.str.count('ghz') == 0) == True, 'processor'])
# print(smartphones['processor'].isin(smartphones[(smartphones.processor.str.count('ghz') == 0) == True].processor))


new_processors = ['apple a16, hexa core, 3.46 ghz processor', 'exynos 1280, octa core, 2.4 ghz processor', 'apple a16, hexa core, 3.46 ghz processor',
                  'snapdragon 855, octa core, 2.84 ghz processor', 'google tensor, octa core, 2.8 ghz processor', 'google tensor, octa core, 2.8 ghz processor',
                  'apple a17, hexa core, 3.78 ghz processor', 'exynos 1380, octa core, 2.4 ghz processor', 'apple a16, hexa core, 3.46 ghz processor',
                  'mediatek helio p22, octa core, 2 ghz processor', 'snapdragon 778g+, octa core, 2.5 ghz processor', 'exynos  2300, octa core, 3.09 ghz processor',
                  'apple a12, hexa core, 2.49 ghz processor', 'apple a15, hexa core, 3.23 ghz processor', 'apple a16, hexa core, 3.46 ghz processor',
                  'snapdragon 8 gen 3, octa core, 3.3 ghz processor', 'unisoc tiger t610, octa core, 1.82 ghz processor', 'apple a17, hexa core, 3.78 ghz processor',
                  'apple a16, hexa core, 3.46 ghz processor', 'mediatek helio g99, octa core, 2.2 ghz processor', 'exynos 1330, octa core, 2.4 ghz processor',
                  'mediatek dimensity 9200, octa core, 3.05 ghz processor', 'mediatek helio p22, octa core, 2 ghz processor', 'apple a16, hexa core, 3.46 ghz processor',
                  'mediatek dimensity 8200, octa core, 3.1 ghz processor', 'apple a16, hexa core, 3.46 ghz processor', 'google tensor g3, octa core, 2.91 ghz processor',
                  'apple a16, hexa core, 3.46 ghz processor', 'exynos 2200, octa core, 2.8 ghz processor', 'snapdragon 730g, octa core, 2.2 ghz processor',
                  'mediatek dimensity 8300 ultra, octa core, 3.35 ghz processor', 'exynos 1330, octa core, 2.4 ghz processor', 'mediatek dimensity 7200, octa core, 2.8 ghz processor',
                  'mediatek dimensity 7200, octa core, 2.8 ghz processor', 'apple a16, hexa core, 3.46 ghz processor', 'exynos 1380, octa core, 2.4 ghz processor',
                  'mediatek helio g85, octa core, 2 ghz processor', 'google tensor g3, octa core, 2.91 ghz processor', 'snapdragon 778g, octa core, 2.4 ghz processor']
smartphones.loc[(smartphones.processor.str.count('ghz') == 0) == True, 'processor'] = new_processors
# df[(df['some_column_name'].isin(['some_value_1', 'some_value_2']) == False)]
smartphones.loc[smartphones.ram == 'ram', 'ram'] = '12 gb ram, 256 gb inbuilt'
# print(smartphones['display'].unique())
# print(smartphones[smartphones.display.str.count('hz') == 0])
smartphones.loc[smartphones['rating'].isin([np.nan]) == True, 'rating'] = int(smartphones[smartphones['rating'].isin([np.nan]) == False]['rating'].mean())
## print(smartphones[smartphones.display.str.count('inch') == 0])
## new_displays = ['6.7 inches, 2640 x 1080 px, 120 hz display with foldable dual', '7.8 inches, 1920 x 1440 px, 60 hz display with foldable dual',
    ##           '7.1 inches, 1792 x 1920 px, 120 hz display with foldable dual', '6.8 inches, 2520 x 1080 px, 120 hz display with foldable dual',
   ##            '6.7 inches, 2640 x 1080 px, 120 hz display with foldable dual', '7.6 inches, 2208 x 1768 px, 120 hz display with foldable dual',
    ##           '6.8 inches, 2460 x 1080 px display with dual', '6.78 inches, 2460 x 1080 px, 120 hz display with dual',
    ##           '7.4 inches, 2400 x 1080 px display with dual', '7.8 inches, 2480 x 2200, 120 hz display with foldable',
     ##          '7.2 inches, 1920 x 1440 px, 60 hz display with foldable dual']
## smartphones.loc[smartphones.display.str.count('inch') == 0, 'display'] = new_displays
## smartphones['display'] = smartphones.display.str.replace('\u2009', ' ')
# print(smartphones[smartphones.os == 'os'])
smartphones.loc[(smartphones.card == 'card') | (smartphones.card == 'memory card supported'), 'card'] = 'memory card supported, upto 256 gb'
# print(smartphones[smartphones.card.str.count('not') == 0])
smartphones['ram'] = smartphones.ram.str.replace('\u2009', ' ')
smartphones['ram'] = smartphones.ram.str.replace(' ram', '')
smartphones['ram'] = smartphones.ram.str.replace(' inbuilt', '')
smartphones['ram'] = smartphones.ram.str.replace(' tb', '024 gb')
smartphones['ram'] = smartphones.ram.str.replace(' gb', '')
smartphones['battery'] = smartphones.battery.str.replace('\u2009', ' ')
smartphones['battery'] = smartphones.battery.str.replace(' battery', '')
smartphones['battery'] = smartphones.battery.str.replace(' fast charging', '')
smartphones['card'] = smartphones.card.str.replace('\u2009', ' ')
smartphones['sim'] = smartphones.sim.str.replace('\u2009', ' ')
smartphones['processor'] = smartphones.processor.str.replace('\u2009', ' ')
smartphones['processor'] = smartphones.processor.str.replace(' processor', '')
smartphones['processor'] = smartphones.processor.str.replace(' ghz', '')
smartphones['processor'] = smartphones.processor.str.split(', ').str[-2::]
smartphones['display'] = smartphones.display.str.replace('\u2009', ' ')
smartphones['display'] = smartphones.display.str.replace('x display', 'x, 60 hz display')
smartphones['camera'] = smartphones.camera.str.replace('\u2009', ' ')
# print(smartphones['card'].unique())
smartphones['card'] = smartphones.card.str.replace(' tb', '024 gb')
smartphones['card'] = smartphones.card.str.split(', upto')
# print(smartphones.card.str.len())
smartphones.loc[smartphones.card.str.len() == 1.0, 'card'].apply(array_append, args=('0 gb',))
# print(smartphones['card'].str[1].str.replace(' gb', ''))
smartphones.insert(len(smartphones.columns) - 1, 'card_value (gb)', smartphones['card'].str[1].str.replace(' gb', '').astype('int'))
del smartphones['card']
smartphones['battery'] = smartphones.battery.str.split(' with')
smartphones['display'] = smartphones.display.str.replace(' with', ',')
smartphones['display'] = smartphones.display.str.replace(' display', '')
smartphones['display'] = smartphones.display.str.split(' ,')
smartphones

import json
import re
import time

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium.common import NoSuchWindowException
from selenium import webdriver

# from config import catalog, pages, headless, minimum_percentage, max_price, min_price, max_price_with_discounted, \
#     cookie_file

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

# def load_cookies():
#     with open("cookie.json", encoding="utf-8", errors="ignore") as config_file:
#         cookies = json.load(config_file)
#     return [[cookie["name"], cookie["value"]] for cookie in cookies]

def parse(model_name, driver):
    url = f"https://megamarket.ru/catalog/?q={model_name.replace(' ', '+')}&collectionId=12546"
    driver.get(url)
    html = BeautifulSoup(driver.page_source, "html.parser")
    catalog_items = html.find("div", class_ = "catalog-items-list")
    # print(catalog_items)

    if catalog_items is None:
        print(f"Нет каталога | Рекурсия на странице {url}")
        # return parse(model_name, driver)

    # items = catalog_items.find_all("div", class_ = "catalog-item-regular-desktop ddl_product catalog-item-desktop")
    items = catalog_items.find_all("div", class_ = "catalog-item-mobile ddl_product")
    # print(items)
    if len(items) == 0:
        print(f"0 Предметов | Рекурсия на странице {url}")
        # return parse(model_name, driver)

    for item in items:
        item_title = item.find("div", class_="item-title").get("title").strip()
        print(item_title, item.find("div", class_="item-title").get("title"))
        item_url = "https://megamarket.ru" + item.find("a", class_="ddl_product_link").get("href").strip()
        print(item_title)

    return True


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

def shuffle_dataset(dataset: pd.DataFrame) -> np.ndarray:
    """Функция для чтения данных с диска, а также их случайного перемешивания

    Parameters
    ----------
    path_to_csv: Путь к файлу boston.csv
    shuffle: Если True, то перемешивает данные

    Return
    ------
    dataframe: Данные в формате DataFrame
    """
    dataset = pd.DataFrame(dataset.sample(frac=1, random_state=RANDOM_SEED, ignore_index=True))
    return dataset

smartphones = shuffle_dataset(smartphones)

def prepare_dataset_for_regression(
    dataset: pd.DataFrame, label_col_name: str = "medv", test_size: float = 0.1
) -> tuple[np.ndarray, ...]:
    """Функция для выделения таргета и признаков,
    а также разделения на тренировочную и тестовую части.

    Parameters
    ----------
    dataset: DataFrame с датасетом
    label_col_name: Название колонки с таргетом
    test_size: доля тестовой выборки относительно всего датасета

    Return
    ------
        4 numpy массива: X_train, X_test, y_train, y_test
        X_train, X_test -- матрицы признаков размером [n_elements; 13]
        y_train, y_test -- массивы с ценами размером [n elements]
    """
    target = dataset.loc[:, label_col_name]
    features = dataset.iloc[:, 2]
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=RANDOM_SEED)
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = prepare_dataset_for_regression(smartphones, 'price')

def print_regression_report(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MSE: {mse:.2f}", f"R2-score: {r2:.2f}", sep="\n")

model_v1 = LinearRegression(n_jobs=-1)
model_v1.fit(X_train, y_train)
y_pred_v1 = model_v1.predict(X_test)

print_regression_report(y_test, y_pred_v1)
