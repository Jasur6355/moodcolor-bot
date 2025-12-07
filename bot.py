import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.start import router as start_router
from handlers.choose_part import router as choose_part_router
from handlers.pick_color import router as pick_color_router
from handlers.finish import router as finish_router

from config import BOT_TOKEN

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(choose_part_router)
    dp.include_router(pick_color_router)
    dp.include_router(finish_router)

    print("Bot ishlayapti...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
