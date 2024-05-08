import pandas as pd
import numpy as np
import math
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
# %pip install selenium
# %pip install undetected-chromedriver
# !pip install selenium
# !apt-get update
# !apt install chromium-chromedriver
# import json
# import re
# import time

# import undetected_chromedriver as uc
# from bs4 import BeautifulSoup
# from openpyxl import Workbook
# from selenium.common import NoSuchWindowException
# from selenium import webdriver
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

array_append = lambda arr, x: arr.append(x)


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
smartphones.loc[smartphones['rating'].isin([np.nan]) == True, 'rating'] = int(smartphones[smartphones['rating'].isin([np.nan]) == False]['rating'].mean()) - 6
## print(smartphones[smartphones.display.str.count('inch') == 0])
## smartphones['display'] = smartphones.display.str.replace('\u2009', ' ')
# print(smartphones[smartphones.os == 'os'])
smartphones.loc[(smartphones.card == 'card') | (smartphones.card == 'memory card supported'), 'card'] = 'memory card supported, upto 256 gb'
# print(smartphones[smartphones.card.str.count('not') == 0])
smartphones['ram'] = smartphones.ram.str.replace('\u2009', ' ')
smartphones['ram'] = smartphones.ram.str.replace(' ram', '')
smartphones['ram'] = smartphones.ram.str.replace(' inbuilt', '')
smartphones['ram'] = smartphones.ram.str.replace(' tb', '024 gb')
smartphones['ram'] = smartphones.ram.str.replace('512 mb', '1 gb')
smartphones['ram'] = smartphones.ram.str.replace(' gb', '')
smartphones['battery'] = smartphones.battery.str.replace('\u2009', ' ')
smartphones['battery'] = smartphones.battery.str.replace(' battery', '')
smartphones['battery'] = smartphones.battery.str.replace(' mah', ', ')
smartphones['battery'] = smartphones.battery.str.replace(' with', '')
# print(smartphones['battery'].unique())
smartphones['battery'] = smartphones.battery.str.replace(' fast charging', '')
smartphones['card'] = smartphones.card.str.replace('\u2009', ' ')
smartphones['sim'] = smartphones.sim.str.replace('\u2009', ' ')
smartphones['processor'] = smartphones.processor.str.replace('\u2009', ' ')
smartphones['processor'] = smartphones.processor.str.replace(' processor', '')
smartphones['processor'] = smartphones.processor.str.replace(' ghz', '')
smartphones['processor'] = smartphones.processor.str.replace(' core', '')
smartphones['processor'] = smartphones.processor.str.split(', ').str[-2::]
# smartphones['display'] = smartphones.display.str.replace('display, ', '')
new_displays = ['7.1 inches, 1792 x 1920 px, 120 hz display with foldable dual', '8.0 inches, 2200 x 2480 px, 120 hz display with foldable',
                '2.7 inches, 240 x 320 px, 60 hz display with dual', '7.1 inches, 1792 x 1920 px, 120 hz display with foldable dual',
                '8.0 inches, 1080 x 2520 px, 120 hz display with foldable dual', '2.8 inches, 240 x 320 px, 60 hz with dual',
                '6.7 inches, 1080 x 2640 px, 120 hz display with foldable dual', '7.6 inches, 1812 x 2176 px, 120 hz display with foldable dual',
                '7.8 inches, 1440 x 1920 px, 60 hz display with foldable dual', '7.1 inches, 1792 x 1920 px, 120 hz display with foldable dual',
                '6.8 inches, 1080 x 2520 px, 120 hz display with foldable dual', '8.0 inches, 1916 x 2160, 120 hz display with foldable dual',
                '6.7 inches, 1080 x 2640 px, 120 hz display with foldable dual', '7.6 inches, 1768 x 2208 px, 120 hz display with foldable dual',
                '6.8 inches, 1080 x 2460 px display with dual', '6.8 inches, 1080 x 2460 px, 120 hz display with dual',
                '6.8 inches, 1080 x 2460 px display with dual', '7.1 inches, 1792 x 1920 px, 120 hz display with foldable dual',
                '7.4 inches, 1812 x 2176 px display with dual', '6.8 inches, 1080 x 2448 px, 165 hz display with dual',
                '6.5 inches, 2480 x 2200 px, 120 hz display with foldable', '8.0 inches, 1860 x 2480 px, 60 hz display with foldable dual',
                '2.8 inches, 480 x 640 px, 60 hz display with dual', '7.2 inches, 1920 x 1440 px, 60 hz display with foldable dual',
                '7.6 inches, 1812 x 2176 px, 120 hz display with foldable dual', '8.0 inches, 2200 x 2480 px, 120 hz display with foldable',
                '8.0 inches, 2200 x 2480 px, 60 hz display with foldable', '8.0 inches, 1916 x 2160 px, 120 hz display with foldable']
# print(smartphones.loc[smartphones.display.str.count('inch') == 0])
smartphones.loc[smartphones.display.str.count('inch') == 0, 'display'] = new_displays
smartphones['display'] = smartphones.display.str.replace('\u2009', ' ')
smartphones['display'] = smartphones.display.str.replace('x display', 'x, 60 hz display')
smartphones['camera'] = smartphones.camera.str.replace('\u2009', ' ')
smartphones['camera'] = smartphones.camera.str.replace(' &', '')
smartphones['camera'] = smartphones.camera.str.replace(' camera', '')
smartphones['camera'] = smartphones.camera.str.replace(' front', '')
smartphones['camera'] = smartphones.camera.str.replace(' main', '')
smartphones['camera'] = smartphones.camera.str.split(' rear')
# print(smartphones['card'].unique())
smartphones['card'] = smartphones.card.str.replace(' tb', '024 gb')
smartphones['card'] = smartphones.card.str.split(', upto')
# print(smartphones.card.str.len())
smartphones.loc[smartphones.card.str.len() == 1.0, 'card'].apply(array_append, args=('0 gb',))
# print(smartphones['card'].str[1].str.replace(' gb', ''))
smartphones.insert(len(smartphones.columns) - 1, 'card_value (gb)', smartphones['card'].str[1].str.replace(' gb', '').astype('int'))
del smartphones['card']
smartphones['battery'] = smartphones.battery.str.split(', ')
smartphones.insert(len(smartphones.columns) - 4, 'fast charging (w)', smartphones['battery'].str[1].str.replace('w', ''))
smartphones.loc[smartphones['fast charging (w)'] == '', 'fast charging (w)'] = '0'
smartphones['fast charging (w)'] = smartphones['fast charging (w)'].astype('float')
smartphones['battery'] = smartphones.battery.str[0].astype('int')
smartphones['display'] = smartphones.display.str.replace(' with', ',')
smartphones['display'] = smartphones.display.str.replace(' display', '')
smartphones['display'] = smartphones.display.str.split(', ')
# smartphones.insert(len(smartphones.columns) - 3, 'additional display parametrs', smartphones['display'].str[3])
smartphones.insert(len(smartphones.columns) - 3, 'display frequancy (hz)', smartphones['display'].str[2].str.replace(' hz', '').astype('int'))
smartphones.insert(len(smartphones.columns) - 4, 'display heigth (px)', smartphones['display'].str[1].str.replace(' px', ''))
smartphones['display heigth (px)'] = smartphones['display heigth (px)'].str.split(' x ')
smartphones.insert(len(smartphones.columns) - 4, 'display width (px)', smartphones['display heigth (px)'].str[0].astype('int'))
smartphones['display heigth (px)'] = smartphones['display heigth (px)'].str[1].astype('int')
smartphones.insert(len(smartphones.columns) - 6, 'display size (inch)', smartphones['display'].str[0].str.replace(' inches', '').astype('float'))
del smartphones['display']
# smartphones['sim'] = smartphones.display.str.replace(' sim', '')
# print(smartphones['sim'].unique())
smartphones['sim'] = smartphones.sim.str.split(', ')
unique_sim_qualities = []
# print(smartphones['sim'].unique())
for index in smartphones.index:
  qualities = smartphones.sim.loc[index]
  # print(smartphones.sim.loc[index])
  for quality in qualities:
    if quality not in unique_sim_qualities:
      unique_sim_qualities.append(quality)
# smartphones['sim'] = smartphones.sim.str.join(', ')
# print(smartphones['sim'])
# for sim_quality in
qualities_all = []
for index in smartphones.index:
  qualities = list(smartphones.sim.loc[index])
  new_qualities = []
  for unique_quality in unique_sim_qualities:
      if unique_quality in qualities:
        new_qualities.append(1)
      else:
        new_qualities.append(0)
  qualities_all.append(new_qualities)
  # print(smartphones.loc[index, 'sim'])
  # print(qualities)
smartphones['sim'] = qualities_all
column_id = 3
for unique_quality in unique_sim_qualities:
  smartphones.insert(column_id, unique_quality, smartphones['sim'].str[column_id - 3])
  column_id += 1
del smartphones['sim']
# smartphones['sim'] = smartphones.sim.str.split(', ')
smartphones.insert(len(smartphones.columns) - 11, 'cores num', smartphones['processor'].str[0])
smartphones['processor'] = smartphones['processor'].str[1].astype('float')
cores_num = {'octa': '8', 'hexa': '6', 'quad': '4', 'dual': '2'}
for core in cores_num:
  smartphones['cores num'] = smartphones['cores num'].str.replace(core, cores_num[core])
smartphones['cores num'] = smartphones['cores num'].astype('int')
# print(smartphones[smartphones['ram'].isin(['4, 512 mb'])])
smartphones['ram'] = smartphones.ram.str.split(', ')
smartphones.insert(len(smartphones.columns) - 10, 'inbuilt memory', smartphones['ram'].str[1].astype('int'))
smartphones['ram'] = smartphones['ram'].str[0].astype('int')
# smartphones.insert(len(smartphones.columns) - 2, '')
smartphones.insert(len(smartphones.columns) - 3, 'rear camera (max mp)', smartphones['camera'].str[0])
smartphones.insert(len(smartphones.columns) - 3, 'front camera (max mp)', smartphones['camera'].str[1])
del smartphones['camera']
smartphones.loc[smartphones['front camera (max mp)'] == '', 'front camera (max mp)'] = '0 mp'
cameras_num = {'triple': '3', 'dual': '2', 'mp': '1', 'quad': '4', 'penta': '5'}
smartphones['rear camera (max mp)'] = smartphones['rear camera (max mp)'].str.split()
smartphones.insert(len(smartphones.columns) - 4, 'rear num', smartphones['rear camera (max mp)'].str[-1])
smartphones['front camera (max mp)'] = smartphones['front camera (max mp)'].str.split()
smartphones.insert(len(smartphones.columns) - 3, 'front num', smartphones['front camera (max mp)'].str[-1])
for cam_num in cameras_num:
  smartphones['rear num'] = smartphones['rear num'].str.replace(cam_num, cameras_num[cam_num])
  smartphones['front num'] = smartphones['front num'].str.replace(cam_num, cameras_num[cam_num])
smartphones['rear num'] = smartphones['rear num'].astype('int')
smartphones['front num'] = smartphones['front num'].astype('int')
smartphones['rear camera (max mp)'] = smartphones['rear camera (max mp)'].str[0].astype('float')
smartphones['front camera (max mp)'] = smartphones['front camera (max mp)'].str[0].astype('float')
# print(smartphones['rear camera'].unique())
le = LabelEncoder()
os_as_str = smartphones['os'].unique()
smartphones['os'] = le.fit_transform(smartphones['os'])
os_as_num = smartphones['os'].unique()

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

# # def load_cookies():
# #     with open("cookie.json", encoding="utf-8", errors="ignore") as config_file:
# #         cookies = json.load(config_file)
# #     return [[cookie["name"], cookie["value"]] for cookie in cookies]

# def parse(model_name, driver):
#     global smartphones
#     url = f"https://megamarket.ru/catalog/?q={model_name.replace(' ', '+')}&collectionId=12546"
#     print(model_name)
#     new_model_name = model_name.replace('(','')
#     new_model_name = new_model_name.replace(')','')
#     new_model_name = new_model_name.replace(' 5g','')
#     new_model_name = new_model_name.replace(' ram','')
#     new_model_name = new_model_name.replace('gb','')
#     new_model_name = new_model_name.replace(' + ','/')
#     new_model_name = new_model_name.replace(' plus','')
#     words_in_model = new_model_name.split(' ')
#     print(words_in_model)
#     driver.get(url)
#     html = BeautifulSoup(driver.page_source, "html.parser")
#     catalog_items = html.find("div", class_ = "catalog-items-list")
#     # print(catalog_items)

#     if catalog_items is None:
#         print(f"Нет каталога | Рекурсия на странице {url}")
#         smartphones = smartphones.drop(smartphones[smartphones['model'].isin([model_name])].index)
#         return False
#         # return parse(model_name, driver)

#     # items = catalog_items.find_all("div", class_ = "catalog-item-regular-desktop ddl_product catalog-item-desktop")
#     items = catalog_items.find_all("div", class_ = "catalog-item-mobile ddl_product")
#     # print(items)
#     if len(items) == 0:
#         print(f"0 Предметов | Рекурсия на странице {url}")
#         smartphones = smartphones.drop(smartphones[smartphones['model'].isin([model_name])].index)
#         return False
#         # return parse(model_name, driver)

#     for item in items:
#       count_model = 0
#       # print(item.find("a", class_="ddl_product_link"))
#       item_title = item.find("div", class_="item-title").a.get('title').strip()[9:].lower()
#       # print(item.find("div", class_="item-title"))
#       # item_url = "https://megamarket.ru" + item.find("a", class_="ddl_product_link").get("href").strip()
#       for model_word in words_in_model:
#         if model_word in item_title:
#           count_model += 1
#       print(count_model, len(words_in_model))
#       if count_model == len(words_in_model):
#         return True
#       print(item_title)

#     smartphones = smartphones.drop(smartphones[smartphones['model'].isin([model_name])].index)
#     return False


# def main():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(f"--user-agent={user_agent}")
#     chrome_options.add_argument('--disable-notifications')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     # options.binary_location = "\Application\chrome.exe"
#     # print(options.binary_location)
#     driver = webdriver.Chrome(options=chrome_options)
#     # driver.get("https://megamarket.ru/")
#     # cookies = load_cookies()
#     # print("Подгрузка куки файлов")
#     # for name, value in cookies:
#     #     driver.add_cookie({"name": name, "value": value})
#     # print("Куки подгружены")
#     driver.get("https://megamarket.ru/")
#     print("Start")

#     try:
#         # current_page = 1
#         for model_name in smartphones['model']:
#         # while current_page != pages + 1:
#           print(model_name)
#           result = parse(model_name, driver)
#             # if result:
#             #     print(f"{time.strftime('%H:%M:%S %d/%m/%Y')} | {current_page} / {pages}")
#             # else:
#             #     break
#             # current_page += 1

#         print("Все товары просмотрены")

#     except Exception as e:
#         print(e)
#     finally:
#         try:
#             driver.close()
#             driver.quit()
#         except NoSuchWindowException:
#             driver.quit()

#     print("Finish")

# main()

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
    features = dataset.iloc[:, 2:]
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=RANDOM_SEED)
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = prepare_dataset_for_regression(smartphones, 'price')

def print_regression_report(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mean_error = np.mean(np.abs(y_pred - np.array(y_test)))
    print(f"MSE: {mse:.2f}", f"R2-score: {r2:.2f}", mean_error, sep="\n")

phones_model_v1 = GradientBoostingRegressor(loss='huber', n_estimators=140, random_state=RANDOM_SEED)
phones_model_v1.fit(X_train, y_train)
# print(X_test)
y_pred_v1 = phones_model_v1.predict(X_test)
# print(y_pred_v1, np.array(smartphones.iloc[1, :]))
# print_regression_report(y_test, y_pred_v1)

feature_names = smartphones.columns[2:]
coefs = phones_model_v1.feature_importances_

for name, cf in sorted(zip(feature_names, coefs), key=lambda x: x[1], reverse=True):
    print(f"{name}\t{cf}")

# print_regression_report(y_test, y_pred_v1)
# print(smartphones.columns)
def data_from_telebot(characteristics):
    characteristics_for_ml = set(characteristics)
    cores_num = 0
    display_freq = []
    inbuilt_mem = []
    brands = []
    borders = []
    sd = False
    sort_by = []
    smartphones_data = pd.read_csv('smartphones_ready_for_ml.csv')
    smartphones_data = smartphones_data.iloc[:, 1:]
    smartphones_megamarket = pd.read_csv('clear_smartphones.csv')
    # new_characteristics = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0,]
    for characteristic in characteristics_for_ml:
        characteristic = characteristic.lower()
        if 'apple' in characteristic:
            cores_num = 6
            brands += ['iphone']
        elif 'hz' in characteristic:
            display_freq += [int(characteristic[:-2])]
        elif 'gb' in characteristic:
            inbuilt_mem += [int(characteristic[:-2])]
        elif 'sd' in characteristic:
            sd = True
        elif characteristic in ('samsung', 'honor', 'huawei', 'xiaomi', 'realme'):
            brands += [characteristic]
        elif '-' in characteristic:
            low_border, high_border = characteristic.split('-')
            low_border, high_border = int(low_border), int(high_border)
            borders.extend([low_border, high_border])
        elif '+' in characteristic:
            low_border = int(characteristic[:-1])
            borders.extend([low_border, -1])
        elif characteristic in ('cpu', 'camera', 'ram', 'battery', 'display'):
            if characteristic == 'cpu':
                characteristic = 'processor'
            elif characteristic == 'camera':
                characteristic = 'rear camera (max mp)'
            elif characteristic == 'display':
                characteristic = 'display size (inch)'
            sort_by.append(characteristic)
    if cores_num == 0:
        cores_num = 8
    if -1 in borders:
        borders.remove(-1)
        high_border = smartphones['price'].max()
        borders.append(high_border)
    low_border = min(borders)
    high_border = max(borders)
    smartphones_for_search = smartphones_data[(smartphones_data.price >= low_border*1000) & (smartphones_data.price <= high_border*1000)]
    if sd:
        sort_by.append('card_value (gb)')
    if len(inbuilt_mem) != 0:
        sort_by.append('inbuilt memory')
        min_gb = min(inbuilt_mem)
        max_gb = max(inbuilt_mem)
        smartphones_for_search = smartphones_for_search[(smartphones_for_search['inbuilt memory'] >= min_gb) & (smartphones_for_search['inbuilt memory'] <= max_gb)]
    if len(display_freq) != 0:
        sort_by.append('display_freq (hz)')
        min_hz = min(display_freq)
        max_hz = max(display_freq)
        smartphones_for_search = smartphones_for_search[(smartphones_for_search['display frequancy (hz)'] >= min_hz) & (smartphones_for_search['display frequancy (hz)'] <= max_hz)]
    smartphones_by_brands = pd.DataFrame(columns=smartphones.columns)
    if len(brands) != 0:
        for brand_name in brands:
          if smartphones_by_brands.empty:
              smartphones_by_brands = smartphones_for_search[smartphones_for_search.model.str.count(brand_name) > 0]
          else:
              smartphones_by_brands = pd.concat([smartphones_by_brands, smartphones_for_search[smartphones_for_search.model.str.count(brand_name) > 0]])
    else:
        smartphones_by_brands = smartphones_for_search
    smartphones_for_search = smartphones_by_brands.sort_values(by=sort_by)
    models_in_megamarket = np.array(smartphones_megamarket['model'])
    for model in np.array(smartphones_for_search['model']):
        if model not in models_in_megamarket:
            smartphones_for_search = smartphones_for_search.drop(smartphones_for_search[smartphones_for_search.model.isin([model])].index)
    print(smartphones_for_search)
    return np.array(smartphones_for_search.iloc[:3, 1])
