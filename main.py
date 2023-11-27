import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from config import token
from Keyboard import key

rasm1 = "https://www.pexels.com/photo/landscape-photography-of-snowy-mountain-1366919/"
rasm2 = "https://www.pexels.com/photo/close-up-photo-of-green-fern-leaf-1226302/"
rasm3 = "https://www.pexels.com/photo/low-angle-photo-of-buildings-during-evening-1707215/"
rasm4 = "https://www.pexels.com/photo/sunflower-selective-focus-photography-1366630/"
rasm5 = "https://www.pexels.com/photo/photography-of-red-rose-plant-1122639/"
rasm6 = "https://www.pexels.com/photo/photo-of-purple-flower-1172849/"
imagelist = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6]

logging.basicConfig(level=logging.INFO)

myToken = token
bot = Bot(token=myToken, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.reply(f" <b>{message.from_user.first_name}</b> sizga qanday yordam bera olaman  <u>  </u> ",
                        parse_mode="HTML")
    print(message.from_user.first_name)
    print(message.from_user.username)
    print(message.from_user.id)


@dp.message(Command("rasm"))
async def rasm(message: Message):
    imageList = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6]
    img = random.choice(imageList)
    await message.answer_photo(photo=f"{img}")


@dp.message(Command("images"))
async def images(message: Message):
    for img in imagelist:
        await message.answer_photo(photo=f"{img}")


@dp.message(Command("contact"))
async def contact(message: Message):
    f = message.from_user.first_name
    await message.answer_contact("+998774446688", first_name=f)


@dp.message(Command("audio"))
async def audio(message: Message):
    await message.reply_audio(audio="https://dl.uzxit.net/2023-mp3/konsta-insonlar_(uzxit.net).mp3",
                              caption="I love my music")


@dp.message(Command("location"))
async def location(message: Message):
    key = [
        [types.KeyboardButton(text="location", request_location=True)],
        [types.KeyboardButton(text="contact", request_contact=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)
    await message.answer("location or contact", reply_markup=keyboard)


@dp.message(Command("shop"))
async def shop(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/QeCLLpW4WpN1NVnj6", caption="shop link",
                               reply_markup=key.as_markup())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
