import logging
from sys import exit

from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, FSInputFile



router = Router()
@router.message(Command(commands=["get_log"]))
async def stop(message: Message, bot: Bot):
        await bot.send_document(message.from_user.id, FSInputFile("logs.txt"))

@router.message(F.photo)
async def photo_hadler(message: Message, bot : Bot):
    pass