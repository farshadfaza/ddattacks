from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- منو ---#
btnTon = KeyboardButton('Top Charts')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTon)

