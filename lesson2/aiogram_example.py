"""
This is a echo bot.
It echoes any incoming text messages.
"""
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    await message.answer("hello")
    photo = await message.photo[-1].download("test.png")
    await bot.send_photo(
        chat_id=message.chat.id, photo=open("/Users/skhaliullin/edu/practice-2022/lesson2/test.png", 'rb')
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
