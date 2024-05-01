import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

RANDOM_SEED = 400220401

smartphones = pd.read_csv('smartphones - smartphones.csv')

def check_column(card_str_value, column_name, *args):
  # try:
    if type(card_str_value) == float:
      false_id = smartphones.loc[smartphones[column_name].isin([card_str_value]), column_name].index
      smartphones.loc[false_id, column_name] = np.nan
      print(smartphones.loc[false_id, column_name])
    else:
      if column_name not in card_str_value:
        # print(column_name, card_str_value)
        # print(card_str_value)
        false_id = smartphones.loc[smartphones[column_name].isin([card_str_value]), column_name].index
        false_os = False
        search_words = np.append(np.array(smartphones.columns), ['inbuilt', ''])
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
        elif 'processor' in card_str_value:
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
    print(os_str_value, false_id)
    smartphones = smartphones.drop(false_id)
  else:
    # print(2)
    if 'android' not in os_str_value and 'ios' not in os_str_value and 'a1' not in os_str_value and 'os' not in os_str_value:
      # print(3)
      smartphones = smartphones.drop(false_id)


columns_names = np.array(smartphones.columns)
columns_names[0], columns_names[1] = columns_names[1], columns_names[0]
smartphones = smartphones.reindex(columns = columns_names)
for column in columns_names[3:]:
  smartphones[column] = smartphones[column].str.lower()
for column in columns_names[3:]:
  smartphones[column].apply(func=check_column, args=(column, ))
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
for column in columns_names:
  print(column)
  print(smartphones[smartphones[column] == column])


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
