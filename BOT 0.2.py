import telebot
from telebot import types

token = '6579188711:AAHf34uQGiGLfd-7GsBXKj0r5umufdex2fc'
MLDockerBot = telebot.TeleBot(token)
characteristic = {}


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
                                            '60gz', '90gz', '120gz', '144gz',
                                                                     'Apple', 'Samsung', 'Honor', 'Huawei', 'Xiaomi',
                                            'Realme',
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
    elif callback.data in ('CPU', 'Camera', 'RAM', 'Battery'):
        characteristic[callback.data] = True
    elif callback.data in ('0-10', '10-20', '20-30', '30-40', '40-50', '50+'):
        if 'Price' not in characteristic.keys():
            characteristic['Price'] = [callback.data]
        else:
            characteristic['Price'].append(callback.data)
    elif callback.data in ('60gz', '90gz', '120gz', '144gz'):
        if 'Display' not in characteristic.keys():
            characteristic['Display'] = [callback.data]
        else:
            characteristic['Display'].append(callback.data)
    elif callback.data in ('Apple', 'Samsung', 'Honor', 'Huawei', 'Xiaomi', 'Realme'):
        if 'Brand' not in characteristic.keys():
            characteristic['Brand'] = [callback.data]
        else:
            characteristic['Brand'].append(callback.data)
    elif callback.data in ('64gb', '128gb', '256gb', '512gb', '1024gb', 'SD'):
        if 'Memory' not in characteristic.keys():
            characteristic['Memory'] = [callback.data]
        else:
            characteristic['Memory'].append(callback.data)
    elif callback.data == 'result':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 f'Вот ваш результат: {characteristic}\n'
                                 'Попробовать еще раз?',
                                 reply_markup=buttons('restart'))


if __name__ == '__main__':
    MLDockerBot.infinity_polling()
