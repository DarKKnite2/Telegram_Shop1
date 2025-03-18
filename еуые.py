import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram.executor import start_polling
from aiocryptopay import AioCryptoPay, Network

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
CRYPTO_API_TOKEN = 'YOUR_AIOCRYPTOPAY_API_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

cryptopay = AioCryptoPay(api_key=CRYPTO_API_TOKEN, network=Network.MAINNET)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который принимает оплату криптовалютой.")

@dp.message_handler(commands=['pay'])
async def pay(message: types.Message):
    invoice = await cryptopay.create_invoice(asset='BTC', amount=0.001, description='Оплата услуги')
    await message.reply(f"Оплата: {invoice['pay_url']}")

if __name__ == '__main__':
    start_polling(dp, skip_updates=True)
