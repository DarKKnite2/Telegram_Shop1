import os
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiohttp.client_exceptions import cert_errors

from App import keyboards as kb
from aiocryptopay import AioCryptoPay, Networks


router = Router()
#crypto = AioCryptoPay(token=os.getenv('CRYPTO_TOKEN'), network=Networks.MAIN_NET)

#@router.message(Command('pay'))
#async def process_payment_command(message: Message):
#    invoice = await  crypto.create_invoice(amount=1.0, asset='USDT')
#    await message.answer(f'Ссылка на оплату: {invoice.pay_url}')



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIH6mY7gcKh-DDJTU5YnHflvqnlwElIAAI83TEbMvnhSUenEPc4D28kAQADAgADeQADNQQ',
        caption='Привет!\nПотыкай кнопочки, чтобы узнать мои возможности',
        reply_markup=kb.main
    )


#@router.message(Command('balance'))
#async def balance(message: Message):
#    amount = 1.5  # пример суммы
#    invoice = await crypto.create_invoice(asset='TON', amount=amount)
#    await message.answer(f'Счет создан: {invoice.bot_invoice_url}')


# Новый обработчик для пополнения баланса
#@router.message(Command('deposit'))
#async def deposit(message: Message):
#    amount = 1.5  # пример суммы для пополнения
#    invoice = await crypto.create_invoice(asset='TON', amount=amount)
#    await message.answer(f'Используйте этот счет для пополнения баланса: {invoice.bot_invoice_url}')













@router.message(Command('my_id'))
async def cmd_my_id(message: Message):
    await message.reply(f'Твой Telegram ID: {message.from_user.id}')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.callback_query(F.data == 'startt')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIH6mY7gcKh-DDJTU5YnHflvqnlwElIAAI83TEbMvnhSUenEPc4D28kAQADAgADeQADNQQ',
            caption='Привет!'
                    '\nПотыкай кнопочки, чтобы узнать мои возможности'),
        reply_markup=kb.main)


@router.callback_query(F.data == 'profile')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(
        caption='Ваш профиль',
        reply_markup=kb.profile)


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIH6mY7gcKh-DDJTU5YnHflvqnlwElIAAI83TEbMvnhSUenEPc4D28kAQADAgADeQADNQQ',
            caption='Выберите категорию'),
        reply_markup=kb.catalog)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIH6mY7gcKh-DDJTU5YnHflvqnlwElIAAI83TEbMvnhSUenEPc4D28kAQADAgADeQADNQQ',
        caption='Привет!'
        '\nПотыкай кнопочки, чтобы узнать мои возможности',
        reply_markup=kb.main)


@router.callback_query(F.data == 'steam')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIIU2Y7pMoVgIWpBwvowG4nLYDxhYChAAJB3jEbMvnhSQK94v1lyX-WAQADAgADeQADNQQ',
            caption='Steam услуги'),
        reply_markup=kb.steam)


@router.callback_query(F.data == 'change_region')
async def change_region(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIIU2Y7pMoVgIWpBwvowG4nLYDxhYChAAJB3jEbMvnhSQK94v1lyX-WAQADAgADeQADNQQ',
            caption='Выберите регион'),
        reply_markup=kb.change_region)


@router.callback_query(F.data == 'minecraft')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIImWY8y7-6SE8fM1JI08q5oZewBzuuAAJO2jEbkRrpSb2nRXeeLQABXwEAAwIAA3kAAzUE',
            caption='Minecraft товар'),
        reply_markup=kb.minecraft)


@router.callback_query(F.data == 'fortnite')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIHl2Y6SlqvJNGyZzBhJVe1mYCaF9qtAALh2zEbUHPYSbF9SEmlbrSkAQADAgADeQADNQQ',
            caption='Fortnite услуги'),
        reply_markup=kb.fortnite)


@router.callback_query(F.data == 'fortnite_packs')
async def fortnite_packs(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIHl2Y6SlqvJNGyZzBhJVe1mYCaF9qtAALh2zEbUHPYSbF9SEmlbrSkAQADAgADeQADNQQ',
            caption='Выберите набор'),
        reply_markup=kb.fortnite_packs)


@router.callback_query(F.data == 'brawl_stars')
async def brawl_stars(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIIl2Y8yn3yVr2pTCOr-a92LQm3vKPQAAJE2jEbkRrpSXLGtlydI3cyAQADAgADeQADNQQ',
            caption='Выберите товар'),
        reply_markup=kb.brawl_stars)


@router.callback_query(F.data == 'discord')
async def discord(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIIlWY8yZUO53ftAz4MVzE8TxnNrwRuAAJA2jEbkRrpSVvOtJaVj8G-AQADAgADeQADNQQ',
            caption='Выберите подписку'),
        reply_markup=kb.discord)


@router.callback_query(F.data == 'twitch')
async def twitch(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media='AgACAgIAAxkBAAIIk2Y8yJADsDtNskHrv9T2Bv3yYjJWAAI82jEbkRrpSdqrX0moqcYyAQADAgADeQADNQQ',
            caption='Выберите подписку'),
        reply_markup=kb.twitch)
