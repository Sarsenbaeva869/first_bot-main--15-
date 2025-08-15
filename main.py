import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

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
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

soup_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Борщ — 30 000 сум", callback_data="price_borshch")],
    [InlineKeyboardButton(text="Суп Харчо — 32 000 сум", callback_data="price_harcho")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

drinks_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Фанта 1.5л — 15 000 сум", callback_data="price_fanta")],
    [InlineKeyboardButton(text="Кола 2л — 20 000 сум", callback_data="price_kola")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

dessert_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Чизкейк — 28 000 сум", callback_data="price_cheesecake")],
    [InlineKeyboardButton(text="Черный Лес — 32 000 сум", callback_data="price_black_forest")],
    [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
])

prices = {
    "price_salat_kapriz": "Салат Каприз — 25 000 сум",
    "price_grecheskiy": "Салат Греческий — 28 000 сум",
    "price_borshch": "Борщ — 30 000 сум",
    "price_harcho": "Суп Харчо — 32 000 сум",
    "price_fanta": "Фанта 1.5л — 15 000 сум",
    "price_kola": "Кола 2л — 20 000 сум",
    "price_cheesecake": "Чизкейк — 28 000 сум",
    "price_black_forest": "Черный Лес — 32 000 сум",
}

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("🥂 Добро пожаловать в наш ресторан!\n\n📋 Вот наше меню:", reply_markup=menu_keyboard)

@dp.callback_query(F.data == "menu")
async def show_menu(callback: CallbackQuery):
    await callback.message.edit_text("📋 Наше меню:", reply_markup=menu_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "salad")
async def show_salad(callback: CallbackQuery):
    await callback.message.edit_text("🥗 Выберите салат:", reply_markup=salad_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "soup")
async def show_soup(callback: CallbackQuery):
    await callback.message.edit_text("🍲 Выберите суп:", reply_markup=soup_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "drinks")
async def show_drinks(callback: CallbackQuery):
    await callback.message.edit_text("🥤 Выберите напиток:", reply_markup=drinks_keyboard)
    await callback.answer()

@dp.callback_query(F.data == "dessert")
async def show_dessert(callback: CallbackQuery):
    await callback.message.edit_text("🍰 Выберите десерт:", reply_markup=dessert_keyboard)
    await callback.answer()

@dp.callback_query(lambda c: c.data in prices)
async def show_price(callback: CallbackQuery):
    await callback.answer(prices[callback.data], show_alert=True)

@dp.callback_query(F.data == "back_to_menu")
async def go_back_to_menu(callback: CallbackQuery):
    new_text = "📋 Наше меню:"
    new_markup = menu_keyboard

    # Чтобы не вызвать ошибку "message is not modified"
    if callback.message.text == new_text:
        await callback.answer()
    else:
        await callback.message.edit_text(new_text, reply_markup=new_markup)
        await callback.answer()

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
