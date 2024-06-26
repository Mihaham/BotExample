import sys

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import admin, user

from loguru import logger as lg

async def main() -> None:
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    lg.remove()
    lg.level("INFO", color="<cyan>")
    lg.add("debug.txt", format="{time} | {level} | {file} | {line} | {message}", level="DEBUG",
           rotation="100 MB",
           colorize=True, compression="zip")
    lg.add(sys.stdout,
           format="<level><b>{time} | {level} | {file} | {line} | {message}</b></level>",
           level="DEBUG",
           colorize=True)

    dp.include_routers(admin.router, user.router)

    await dp.start_polling(bot)
