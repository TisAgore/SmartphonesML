import telebot
from telebot import types
from RegressionML import data_from_telebot

token = '6579188711:AAHf34uQGiGLfd-7GsBXKj0r5umufdex2fc'
MLDockerBot = telebot.TeleBot(token)
characteristic = []

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

def say_hello(message):
    markup = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton('Начать', callback_data='price')
    markup.row(start_button)
    MLDockerBot.send_message(message.chat.id, 'Привет! Я помогу тебе выбрать телефон!', reply_markup=markup)


@MLDockerBot.message_handler(commands=['start'])
def hello(message):
    say_hello(message)
    MLDockerBot.delete_message(message.chat.id, message.message_id)


def buttons(characteristic) -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    if characteristic == 'price':
        price_1 = types.InlineKeyboardButton('До 10 тысяч', callback_data='0-10')
        price_2 = types.InlineKeyboardButton('10-20 тысяч', callback_data='10-20')
        price_3 = types.InlineKeyboardButton('20-30 тысяч', callback_data='20-30')
        price_4 = types.InlineKeyboardButton('30-40 тысяч', callback_data='30-40')
        price_5 = types.InlineKeyboardButton('40-50 тысяч', callback_data='40-50')
        price_6 = types.InlineKeyboardButton('Больше 50 тысяч', callback_data='50+')
        next_but = types.InlineKeyboardButton('Далее ▶️', callback_data='specifications')
        return_but = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(price_1, price_2, price_3)
        markup.row(price_4, price_5, price_6)
        markup.row(next_but, return_but)
        return markup
    elif characteristic == 'specifications':
        CPU = types.InlineKeyboardButton('CPU ⚙️', callback_data='CPU')
        Camera = types.InlineKeyboardButton('Камера 📷', callback_data='Camera')
        RAM = types.InlineKeyboardButton('RAM 🧮', callback_data='RAM')
        Battery = types.InlineKeyboardButton('Батарея 🔋', callback_data='Battery')
        Display = types.InlineKeyboardButton('Экран 🖥️', callback_data='Display')
        Brand = types.InlineKeyboardButton('Бренд 🍎', callback_data='Brand')
        Memory = types.InlineKeyboardButton('Память 📁', callback_data='Memory')
        next_but = types.InlineKeyboardButton('Далее ▶️', callback_data='result')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(CPU, Camera, Brand, RAM)
        markup.row(Battery, Display, Memory)
        markup.row(next_but, clear_button)
        return markup
    elif characteristic == 'Display':
        Display60 = types.InlineKeyboardButton('60 Гц', callback_data='60gz')
        Display90 = types.InlineKeyboardButton('90 Гц', callback_data='90gz')
        Display120 = types.InlineKeyboardButton('120 Гц', callback_data='120gz')
        Display144 = types.InlineKeyboardButton('144 Гц', callback_data='144gz')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(Display60, Display90)
        markup.row(Display120, Display144)
        markup.row(return_but, clear_button)
        return markup
    elif characteristic == 'Brand':
        Apple = types.InlineKeyboardButton('Apple', callback_data='Apple')
        Samsung = types.InlineKeyboardButton('Samsung', callback_data='Samsung')
        Honor = types.InlineKeyboardButton('Honor', callback_data='Honor')
        Huawei = types.InlineKeyboardButton('Huawei', callback_data='Huawei')
        Xiaomi = types.InlineKeyboardButton('Xiaomi', callback_data='Xiaomi')
        Realme = types.InlineKeyboardButton('Realme', callback_data='Realme')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(Apple, Samsung, Honor)
        markup.row(Huawei, Xiaomi, Realme)
        markup.row(return_but, clear_button)
        return markup
    elif characteristic == 'Memory':
        Memory64 = types.InlineKeyboardButton('64 Гб', callback_data='64gb')
        Memory128 = types.InlineKeyboardButton('128 Гб', callback_data='128gb')
        Memory256 = types.InlineKeyboardButton('256 Гб', callback_data='256gb')
        Memory512 = types.InlineKeyboardButton('512 Гб', callback_data='512gb')
        Memory1024 = types.InlineKeyboardButton('1024 Гб', callback_data='1024gb')
        MemorySD = types.InlineKeyboardButton('Слот под SD-карту', callback_data='SD')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(Memory64, Memory128, Memory256, Memory512)
        markup.row(Memory1024, MemorySD)
        markup.row(return_but, clear_button)
        return markup
    elif characteristic == 'restart':
        restart_but = types.InlineKeyboardButton('Еще раз', callback_data='price')
        markup.add(restart_but)
        return markup


@MLDockerBot.callback_query_handler(
    func=lambda callback: callback.data in ('price', 'specifications', 'result',
                                            '0-10', '10-20', '20-30', '30-40', '40-50', '50+',
                                            'CPU', 'Camera', 'RAM', 'Battery', 'Display', 'Brand', 'Memory',
                                            '60hz', '90hz', '120hz', '144hz'
                                            'Apple', 'Samsung', 'Honor', 'Huawei', 'Xiaomi', 'Realme',
                                            '64gb', '128gb', '256gb', '512gb', '1024gb', 'SD'
                                            )
)
def characteristics_choice(callback):
    if callback.data == 'price':
        characteristic.clear()
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Давайте начнем с диапазона цен!\n'
                                 'Каким бюджетом для покупки телефона вы обладаете?\n'
                                 'Вы можете выбрать больше одного варианта:',
                                 reply_markup=buttons('price'))
    elif callback.data == 'specifications':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Теперь выбирете важные для вас характеристики.\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('specifications'))
    elif callback.data == 'Display':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Выберите частоту обновления экрана\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('Display'))
    elif callback.data == 'Brand':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Выберите интересующий вас бренд смартфона\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('Brand'))
    elif callback.data == 'Memory':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Выберите нужный вам объем памяти\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('Memory'))
    elif callback.data in ('0-10', '10-20', '20-30', '30-40', '40-50', '50+'):
        characteristic.append(callback.data)
    elif callback.data in ('CPU', 'Camera', 'RAM', 'Battery'):
        characteristic.append(callback.data)
    elif callback.data in ('60hz', '90hz', '120hz', '144hz'):
        characteristic.append(callback.data)
    elif callback.data in ('Apple', 'Samsung', 'Honor', 'Huawei', 'Xiaomi', 'Realme'):
        characteristic.append(callback.data)
    elif callback.data in ('64gb', '128gb', '256gb', '512gb', '1024gb', 'SD'):
        characteristic.append(callback.data)
    elif callback.data == 'result':
        phone_models = data_from_telebot(characteristic)
        str_for_message = 'Вот ваш результат:\n'
        for phone_model in phone_models:
            str_for_message = str_for_message + f'{phone_model.upper()}\n'
            str_for_message = str_for_message + f'https://www.dns-shop.ru/search/?q={phone_model.replace(' ', '+')}&order=opinion\n'
            str_for_message = str_for_message + f'https://megamarket.ru/catalog/?q={phone_model.replace(' ', '+')}&collectionId=12546\n\n'
        str_for_message = str_for_message + 'Попробовать еще раз?'
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                str_for_message,
                                reply_markup=buttons('restart'))


if __name__ == '__main__':
    MLDockerBot.infinity_polling()
