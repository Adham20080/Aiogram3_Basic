from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

key = InlineKeyboardBuilder()
key.row(types.InlineKeyboardButton(
    text="Apple", url="https://www.apple.com/")
)
key.row(types.InlineKeyboardButton(
    text="Aiogram",
    url="https://docs.aiogram.dev/en/latest/")
)
