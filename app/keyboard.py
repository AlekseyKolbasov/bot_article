from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = '/start'),
                                     KeyboardButton(text = '/get_article')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню... :)')