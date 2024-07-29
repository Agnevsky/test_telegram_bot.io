import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from bot_cmd import cmd_bot as cb



bot = Bot(token='6836417550:AAHW7Y7VWr4cM2tUmVQVcPB5A0-tgmsKTEg')
dp = Dispatcher()

@dp.message(CommandStart())
async def start_bot(message: types.Message):

    kb = [[types.KeyboardButton(text='Вот меню')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Привет я бот для кальянной, что бы хотели сделать?', reply_markup=keyboard)
    

async def main():
    await bot.set_my_commands(commands=cb, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())