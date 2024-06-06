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
        price_1 = types.InlineKeyboardButton('До 10 тысяч', callback_data='5000')
        price_2 = types.InlineKeyboardButton('10-20 тысяч', callback_data='15000')
        price_3 = types.InlineKeyboardButton('20-30 тысяч', callback_data='25000')
        price_4 = types.InlineKeyboardButton('30-40 тысяч', callback_data='35000')
        price_5 = types.InlineKeyboardButton('40-50 тысяч', callback_data='45000')
        price_6 = types.InlineKeyboardButton('Больше 50 тысяч', callback_data='120000')
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
        Display60 = types.InlineKeyboardButton('60 Гц', callback_data='60hz')
        Display90 = types.InlineKeyboardButton('90 Гц', callback_data='90hz')
        Display120 = types.InlineKeyboardButton('120 Гц', callback_data='120hz')
        Display144 = types.InlineKeyboardButton('144 Гц', callback_data='144hz')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(Display60, Display90, Display120, Display144)
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
        #        MemorySD = types.InlineKeyboardButton('Слот под SD-карту', callback_data='SD')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        #        markup.row(Memory64, Memory128, Memory256, Memory512)
        #        markup.row(Memory1024, MemorySD)
        markup.row(Memory64, Memory128, Memory256, Memory512, Memory1024)
        markup.row(return_but, clear_button)
        return markup
    elif characteristic == 'Battery':
        Battery3000 = types.InlineKeyboardButton('3000 mAh', callback_data='3000mAh')
        Battery4000 = types.InlineKeyboardButton('4000 mAh', callback_data='4000mAh')
        Battery5000 = types.InlineKeyboardButton('5000 mAh', callback_data='5000mAh')
        Battery6000 = types.InlineKeyboardButton('6000 mAh', callback_data='6000mAh')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(Battery3000, Battery4000, Battery5000, Battery6000)
        markup.row(return_but, clear_button)
        return markup
    elif characteristic == 'Camera':
        Camera16 = types.InlineKeyboardButton('16 Mp', callback_data='16Mp')
        Camera40 = types.InlineKeyboardButton('40 Mp', callback_data='40Mp')
        Camera50 = types.InlineKeyboardButton('50 Mp', callback_data='50Mp')
        Camera64 = types.InlineKeyboardButton('64 Mp', callback_data='64Mp')
        Camera100 = types.InlineKeyboardButton('100 Mp', callback_data='100Mp')
        return_but = types.InlineKeyboardButton('Назад ◀️', callback_data='specifications')
        clear_button = types.InlineKeyboardButton('Заново 🔄', callback_data='price')
        markup.row(Camera16, Camera40, Camera50, Camera64, Camera100)
        markup.row(return_but, clear_button)
        return markup
    elif characteristic == 'restart':
        restart_but = types.InlineKeyboardButton('Еще раз', callback_data='price')
        markup.add(restart_but)
        return markup


@MLDockerBot.callback_query_handler(
    func=lambda callback: callback.data in ('price', 'specifications', 'result',
                                            '5000', '15000', '25000', '35000', '45000', '120000',
                                            'CPU', 'Camera', 'RAM', 'Battery', 'Display', 'Brand', 'Memory',
                                            '60hz', '90hz', '120hz', '144hz',
                                            'Apple', 'Samsung', 'Honor', 'Huawei', 'Xiaomi', 'Realme',
                                            '64gb', '128gb', '256gb', '512gb', '1024gb',  # 'SD'
                                            '16Mp', '40Mp', '50Mp', '64Mp', '100Mp',
                                            '3000mAh', '4000mAh', '5000mAh', '6000mAh'
                                            )
)
def characteristics_choice(callback):
    if callback.data == 'price':
        characteristic.clear()
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
    elif callback.data == 'Battery':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Выберите нужный вам объем батареи\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('Battery'))
    elif callback.data == 'Camera':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Выберите разрешение матрицы (в Мегапикселях)\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('Camera'))
    elif callback.data in ('CPU', 'RAM'):
        characteristic[callback.data] = True
    elif callback.data in ('5000', '15000', '25000', '35000', '45000', '120000'):
        if 'Price' not in characteristic.keys():
            characteristic['Price'] = [int(callback.data[:])]
        else:
            characteristic['Price'].append(int(callback.data))
    elif callback.data in ('60hz', '90hz', '120hz', '144hz'):
        if 'Display' not in characteristic.keys():
            characteristic['Display'] = [int(callback.data[:-2])]
        else:
            characteristic['Display'].append(int(callback.data[:-2]))
    elif callback.data in ('Apple', 'Samsung', 'Honor', 'Huawei', 'Xiaomi', 'Realme'):
        if 'Brand' not in characteristic.keys():
            characteristic['Brand'] = [callback.data]
        else:
            characteristic['Brand'].append(callback.data)
    elif callback.data in ('64gb', '128gb', '256gb', '512gb', '1024gb'):  # 'SD'
        if 'Memory' not in characteristic.keys():
            characteristic['Memory'] = [int(callback.data[:-2])]
        else:
            characteristic['Memory'].append(int(callback.data[:-2]))
    elif callback.data in ('16Mp', '40Mp', '50Mp', '64Mp', '100Mp'):
        if 'Camera' not in characteristic.keys():
            characteristic['Camera'] = [int(callback.data[:-2])]
        else:
            characteristic['Camera'].append(int(callback.data[:-2]))
    elif callback.data in ('3000mAh', '4000mAh', '5000mAh', '6000mAh'):
        if 'Battery' not in characteristic.keys():
            characteristic['Battery'] = [int(callback.data[:-3])]
        else:
            characteristic['Battery'].append(int(callback.data[:-3]))
    elif callback.data == 'result':
        for characteristics in ('CPU', 'RAM'):
            if characteristics not in characteristic.keys():
                characteristic[characteristics] = False
        for characteristics in ('Price', 'Camera', 'Battery', 'Memory', 'Brand', 'Display'):
            if characteristics not in characteristic.keys():
                characteristic[characteristics] = []
        for i in ['Brand', 'Display', 'CPU', 'RAM']:  # КОСТЫЛЬ
            del characteristic[i]
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 f'Вот ваш результат: {characteristic}\n'
                                 'Попробовать еще раз?',
                                 reply_markup=buttons('restart'))


if __name__ == '__main__':
    MLDockerBot.infinity_polling()
