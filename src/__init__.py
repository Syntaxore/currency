import os
from aiogram import Bot, Dispatcher
import logging
from .handlers.start import router as start
from .handlers.get_currency import router as currency
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=os.getenv("BOT_API"))
dp = Dispatcher(storage=storage)
dp.include_routers(start, currency)

async def main_start():
    await dp.start_polling(bot)