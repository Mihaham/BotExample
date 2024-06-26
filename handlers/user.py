import asyncio
import logging

from aiogram import Router, Bot, F
from aiogram.filters import Command, ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER
from aiogram.types import Message, ChatMemberUpdated


router = Router()


@router.message(Command(commands=["help", "start"]))
async def helping_handler(message: Message):
    pass


@router.message(F.photo)
async def message_hadler(message: Message, bot : Bot):
    pass
