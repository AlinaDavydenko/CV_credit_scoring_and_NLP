import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

import os
from dotenv import load_dotenv


# we get keys and settings from the file .env
load_dotenv()

BOT_API = api_key = os.getenv('BOT_TOKEN')  # authorization token for bot
# print(BOT_API)

bot = Bot(token=BOT_API)  # pass the bot token to the class
dp = Dispatcher()  # monitors incoming messages, analyzes them, is responsible for functionality


@dp.message(CommandStart())
async def start_command(message: types.Message):
    """ The function processes messages from the user """
    await message.answer("It's time to begin")


@dp.message()
async def exco(message: types.Message):
    """ The function responds with the user's message """
    text = message.text.lower()
    for word in ['fuck', 'bitch', 'shit', 'gay']:
        if text in word:
            await message.answer(f'{message.text.upper()} U TOO, BRO!!!')
            break
    for word in ['dick', 'prick', 'cunt', 'pussy', 'ass']:
        if text in word:
            await message.answer(f'U {message.text.upper()} IS BIG!!! \nInnit?')
            break
    for word in ['hi', 'hello', 'bye', 'goodbye']:
        if word in text:
            await message.answer(f'{message.text.upper()} BRO \ngo to your asshole...')
            break
    for word in ['jokes', 'fun', 'joke', 'trick', 'prank']:
        if text in word:
            await message.answer(f'What do you call a fake noodle? \nAn impasta.')
            break
    else:
        await message.answer(f'{message.text.upper()}!!!')


async def main_bot() -> None:
    """ asking tg about new messages to the bot"""
    await dp.start_polling(bot)  # launches the bot into operation

asyncio.run(main_bot())
