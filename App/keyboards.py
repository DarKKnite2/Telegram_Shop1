from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Профиль', callback_data='profile')],
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')]
])


profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Баланс', callback_data='balance'),
     InlineKeyboardButton(text='Пополнение', callback_data='deposit')],
    [InlineKeyboardButton(text='Назад', callback_data='startt')]
])


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Steam', callback_data='steam')],
    [InlineKeyboardButton(text='Minecraft', callback_data='minecraft')],
    [InlineKeyboardButton(text='Fortnite', callback_data='fortnite')],
    [InlineKeyboardButton(text='Brawl Stars', callback_data='brawl_stars')],
    [InlineKeyboardButton(text='Discord', callback_data='discord')],
    [InlineKeyboardButton(text='Twitch', callback_data='twitch')],
    [InlineKeyboardButton(text='Назад', callback_data='startt')]
])


steam = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Смена региона', callback_data='change_region'),
     InlineKeyboardButton(text='Пополнение баланса', callback_data='deposit_steam')],
    [InlineKeyboardButton(text='Назад', callback_data='catalog')]
])


change_region = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Казахстан', callback_data='kz_region'),
     InlineKeyboardButton(text='Украина', callback_data='ukr_region')],
    [InlineKeyboardButton(text='Назад', callback_data='steam')]
])


minecraft = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Купить лицензию Minecraft', callback_data='buy_minecraft')],
    [InlineKeyboardButton(text='Назад', callback_data='catalog')]
])

fortnite = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В-баксы', callback_data='v-bucks'),
     InlineKeyboardButton(text='Наборы', callback_data='fortnite_packs')],
    [InlineKeyboardButton(text='Назад', callback_data='catalog')]
])


fortnite_packs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мир грёз', callback_data='c5s1_pack'),
     InlineKeyboardButton(text='Совершенный баланс', callback_data='c5s2_pack')],
    [InlineKeyboardButton(text='Отряд Fornite', callback_data='fortnite_crew')],
    [InlineKeyboardButton(text='Назад', callback_data='fortnite')]
])


brawl_stars = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гемы', callback_data='gems'),
     InlineKeyboardButton(text='Brawl Pass', callback_data='brawl_pass')],
    [InlineKeyboardButton(text='Назад', callback_data='catalog')]
])


discord = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Nitro Basic(1 месяц)', callback_data='nitro_basic_1'),
     InlineKeyboardButton(text='Nitro Full(1 месяц)', callback_data='nitro_full_1')],
    [InlineKeyboardButton(text='Nitro Basic(12 месяцев)', callback_data='nitro_basic_12'),
     InlineKeyboardButton(text='Nitro Full(12 месяцев)', callback_data='nitro_full_12')],
    [InlineKeyboardButton(text='Назад', callback_data='catalog')]
])


twitch = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подписка на 1 месяц', callback_data='twitch_1'),
     InlineKeyboardButton(text='Подписка на 6 месяцев', callback_data='twitch_6')],
    [InlineKeyboardButton(text='Назад', callback_data='catalog')]
])
