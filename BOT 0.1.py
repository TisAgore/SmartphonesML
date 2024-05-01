import telebot
from telebot import types

token = '6579188711:AAHf34uQGiGLfd-7GsBXKj0r5umufdex2fc'
MLDockerBot = telebot.TeleBot(token)
characteristic = []


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
        next_but = types.InlineKeyboardButton('Далее', callback_data='specifications')
        return_but = types.InlineKeyboardButton('Очистить', callback_data='price')
        markup.row(price_1, price_2, price_3)
        markup.row(price_4, price_5, price_6)
        markup.row(next_but, return_but)
        return markup
    elif characteristic == 'specifications':
        CPU = types.InlineKeyboardButton('CPU ‍🦽', callback_data='CPU')
        Camera = types.InlineKeyboardButton('Камера 📸', callback_data='Camera')
        RAM = types.InlineKeyboardButton('RAM 👙', callback_data='RAM')
        Battery = types.InlineKeyboardButton('Батарея 💥', callback_data='Battery')
        Display = types.InlineKeyboardButton('Экран 👁️', callback_data='Display')
        Brand = types.InlineKeyboardButton('Бренд 🇷🇺', callback_data='Brand')
        next_but = types.InlineKeyboardButton('Далее', callback_data='result')
        return_but = types.InlineKeyboardButton('Назад', callback_data='price')
        markup.row(CPU, Camera, Brand)
        markup.row(Battery, Display, RAM)
        markup.row(next_but, return_but)
        return markup
    elif characteristic == 'restart':
        restart_but = types.InlineKeyboardButton('Еще раз', callback_data='price')
        markup.add(restart_but)
        return markup


@MLDockerBot.callback_query_handler(
    func=lambda callback: callback.data in ('price', 'specifications', 'result', '0-10', '10-20',
                                            '20-30', '30-40', '40-50', '50+', 'CPU', 'Camera',
                                            'RAM', 'Battery', 'Display', 'Brand', 'manual')
)
def characteristics_choice(callback):
    global characteristic
    if callback.data == 'manual':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Как пользоваться ботом?\n'
                                 'Вы можете выбрать скок бабок и там еще\n'
                                 'Бля вы вообще дауны это же ебать изи')
    if callback.data == 'price':
        characteristic = []
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Давайте начнем с диапазона цен!\n'
                                 'Каким бюджетом для покупки телефона вы обладаете?\n'
                                 'Вы можете выбрать больше одного варианта:',
                                 reply_markup=buttons('price'))
    elif callback.data in ('0-10', '10-20', '20-30', '30-40', '40-50', '50+'):
        characteristic.append(callback.data)
    elif callback.data == 'specifications':
        for temp_characteristic in ('CPU', 'Camera', 'RAM', 'Battery', 'Display', 'Brand'):
            if temp_characteristic in characteristic:
                characteristic.remove(temp_characteristic)
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 'Теперь выбирете важные для вас характеристики.\n'
                                 'Вы можете выбрать больше одного варианта:\n',
                                 reply_markup=buttons('specifications'))
    elif callback.data in ('CPU', 'Camera', 'RAM', 'Battery', 'Display', 'Brand'):
        characteristic.append(callback.data)
    elif callback.data == 'result':
        MLDockerBot.delete_message(callback.message.chat.id, callback.message.message_id)
        MLDockerBot.send_message(callback.message.chat.id,
                                 f'Вот ваш результат: {characteristic}\n'
                                 'Попробовать еще раз?',
                                 reply_markup=buttons('restart'))


if __name__ == '__main__':
    MLDockerBot.infinity_polling()
