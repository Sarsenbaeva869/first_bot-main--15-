import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputMediaPhoto

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

# Клавиатуры
menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Салаты", callback_data="salad")],
    [InlineKeyboardButton(text="Супы", callback_data="soup")],
    [InlineKeyboardButton(text="Напитки", callback_data="drinks")],
    [InlineKeyboardButton(text="Десерты", callback_data="dessert")]
])

salad_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Салат Каприз — 25 000 сум", callback_data="price_salat_kapriz")],
    [InlineKeyboardButton(text="Салат Греческий — 28 000 сум", callback_data="price_grecheskiy")],
    [InlineKeyboardButton(text="Салат  Оливье -25 000 сум ",  callback_data="price_olivie")],
    [InlineKeyboardButton(text="Салат  Винеграт -32 000 сум", callback_data="price_vinegrat")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

soup_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Борщ — 30 000 сум", callback_data="price_borshch")],
    [InlineKeyboardButton(text="Суп Харчо — 32 000 сум", callback_data="price_harcho")],
    [InlineKeyboardButton(text="Харчо с говяддиной - 26 000 сум", callback_data="price_Xarcho govyodinoy")],
    [InlineKeyboardButton(text="Чихиртма с курицей-20 000 сум", callback_data="price_chixirtma")],
    [InlineKeyboardButton(text="Томатный суп с фасолъю 22 000 сум", callback_data="price_tomatniy_sup")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

drinks_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Фанта 1.5л — 15 000 сум", callback_data="price_fanta")],
    [InlineKeyboardButton(text="Кола 2л — 20 000 сум", callback_data="price_kola")],
    [InlineKeyboardButton(text="Классический 1 л  -50 000 сум", callback_data="price_klasicheckiy")],
    [InlineKeyboardButton(text="Малина с мятой 350 мл -30 000 сум ", callback_data="price_Malinoviy")],
    [InlineKeyboardButton(text="Ягодный  -35 000 сум", callback_data="price_yagodniy")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

dessert_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Чизкейк — 28 000 сум", callback_data="price_cheesecake")],
    [InlineKeyboardButton(text="Черный Лес — 32 000 сум", callback_data="price_black_forest")],
    [InlineKeyboardButton(text="Торт йогурт-Маракуйя -40 000 сум", callback_data="price_tort yogurt")],
    [InlineKeyboardButton(text="Шоколадная Меренга -50 000 сум",callback_data="price_merenga")],
    [InlineKeyboardButton(text="Наполеон -30 000 сум", callback_data="price_napoleon")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

prices = {
    "price_salat_kapriz": "Салат Каприз — 25 000 сум",
    "price_grecheskiy": "Салат Греческий — 28 000 сум",
    "price_olivie": "Салат Оливье - 25 000 сум",
    "price_vinegrat":"Салат  Винеграт -32 000 сум",
    "price_borshch": "Борщ — 30 000 сум",
    "price_harcho": "Суп Харчо — 32 000 сум",
    "price_Xarcho govyodinoy":"Харчо с говяддиной - 26 000 сум" ,
    "price_chixirtma": "Чихиртма с курицей-20 000 сум",
    "price_tomatniy_sup": "Томатный суп с фасолъю 22 000 сум",
    "price_fanta" :"Фанта 1.5л — 15 000 сум",
    "price_kola": "Кола 2л — 20 000 сум",
    "price_klasicheckiy" :"Классический 1 л  -50 000 сум",
    "price_Malinoviy":"Малина с мятой 350 мл -30 000 сум ",
    "price_yagodniy":"Ягодный  -35 000 сум",
    "price_cheesecake": "Чизкейк — 28 000 сум",
    "price_black_forest": "Черный Лес — 32 000 сум",
    "price_tort yogurt":"Торт йогурт-Маракуйя -40 000 сум",
    "price_merenga":"Шоколадная Меренга -50 000 сум",
    "price_napoleon":"Наполеон -30 000 сум",
}

@dp.message(Command("start"))
async def start_cmd(message: Message):
    file_id="AgACAgIAAxkBAAMJaJ4KsQXBVPHGSs6-lRBd0c68ChwAAov2MRtcVfFI3HSm8tBaMXEBAAMCAAN4AAM2BA"
    await message.answer_photo( photo=file_id , caption="🥂Добро пожаловать в  наш ресторан!\n\n📋 Вот наше меню:", reply_markup=menu_keyboard)


photo_id = ""


async def sum_numbers(a: int, b: int):
    return a + b
@dp.message(F.photo)
async def get_file_id(message:Message):
    file_id= message.photo[-1].file_id
    await  message.answer(f"Suwret file_id: {file_id}")



@dp.callback_query(F.data == "menu")
async def show_menu(callback: CallbackQuery):
    await callback.message.edit_text("📋 Наше меню:", reply_markup=menu_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "salad")
async def show_salad(callback: CallbackQuery):
    file_id_salad="AgACAgIAAxkBAANaaKGZCtfF1QtvHBUP2Gf_5-Kv2_IAAqPxMRuUihBJwq_MN-xgIsEBAAMCAAN5AAM2BA"
    media = InputMediaPhoto(media=file_id_salad, caption="🥗 Выберите салат:")
    await callback.message.edit_media(media=media, reply_markup=salad_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "soup")
async def show_soup(callback: CallbackQuery):
    file_id_soup="AgACAgIAAxkBAANmaKGa8jh692Fos_AOGM5g5YZ3ZvUAAq3xMRuUihBJxMWePNJelSQBAAMCAAN4AAM2BA"
    media=InputMediaPhoto(media=file_id_soup, caption="🍲 Выберите суп:")
    await callback.message.edit_media( media=media,reply_markup=soup_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "drinks")
async def show_drinks(callback: CallbackQuery):
    file_id_drinks="AgACAgIAAxkBAAN6aKGeGtxUYOWz0CeUEm5wMqmlHDoAArbxMRuUihBJYDxWWy2G1XUBAAMCAAN5AAM2BA"
    media=InputMediaPhoto(media=file_id_drinks,caption="🥤 Выберите напиток:")
    await callback.message.edit_media(media=media, reply_markup=drinks_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "dessert")
async def show_dessert(callback: CallbackQuery):
    file_id_desert="AgACAgIAAxkBAAN8aKGfBw9F2vAQAuLmKp7CIgLX63wAArnxMRuUihBJ2Xm1UeDFY9sBAAMCAAN5AAM2BA"
    media=InputMediaPhoto(media=file_id_desert,caption="🍰 Выберите десерт:")
    await callback.message.edit_media(media=media, reply_markup=dessert_keyboard)
    await callback.answer()

@dp.callback_query(lambda c: c.data in prices)
async def show_price(callback: CallbackQuery):
    await callback.answer(prices[callback.data], show_alert=True)
    


@dp.callback_query(F.data == "back_to_menu")
async def go_back_to_menu(callback: CallbackQuery):
    file_id_menu = "AgACAgIAAxkBAANWaKGWBdnPyNIbI9zx1998aFDlBicAAo_xMRuUihBJi1UE5zDcwj4BAAMCAAN4AAM2BA"
    media = InputMediaPhoto(media=file_id_menu, caption="🥂Добро пожаловать в наш ресторан!\n\n📋 Вот наше меню:")
    await callback.message.edit_media(media=media, reply_markup=menu_keyboard)
    await callback.answer()


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
