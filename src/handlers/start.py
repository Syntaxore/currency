from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram import F
from aiogram.filters import Command
from ..keyboards.start_kb import start_kb

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Это бот по конвертации валют в реальном времени", reply_markup=start_kb())

