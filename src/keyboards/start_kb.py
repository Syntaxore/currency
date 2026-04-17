from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def start_kb():
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(text="💱 Конвертация", callback_data="conv")
    )
    return kb.as_markup()