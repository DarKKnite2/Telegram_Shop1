import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiocryptopay import AioCryptoPay, Networks
from App.handlers import router

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
crypto = AioCryptoPay(token=os.getenv('CRYPTO_TOKEN'), network=Networks.MAIN_NET)

async def main():
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print('Exit')

if __name__ == '__main__':
    asyncio.run(main())
