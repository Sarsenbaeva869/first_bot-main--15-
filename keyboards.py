from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главная клавиатура меню
menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🥗 Салаты", callback_data="salat")],
    [InlineKeyboardButton(text="🍲 Супы", callback_data="soup")],
    [InlineKeyboardButton(text="🥤 Напитки", callback_data="drinks")],
    [InlineKeyboardButton(text="🍰 Десерты", callback_data="desert")],
])

# Кнопки назад и главное меню
back_button = InlineKeyboardButton(text="⬅️ Назад", callback_data="back")
main_menu_button = InlineKeyboardButton(text="🏠 Главное меню", callback_data="menu")

# Салаты
salad_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Салат Каприз", callback_data="salat_kapriz")],
    [InlineKeyboardButton(text="Салат Греческий", callback_data="grecheskiy_salat")],
    [InlineKeyboardButton(text="Салат Ананас", callback_data="ananas_salat")],
    [InlineKeyboardButton(text="Салат Оливье", callback_data="oliviye")],
    [back_button],
])

# Супы
soup_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Стейк", callback_data="steyk")],
    [InlineKeyboardButton(text="Бешбармак", callback_data="beshmarmaq")],
    [back_button],
])

# Напитки
drinks_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Фанта 1.5л", callback_data="fanta")],
    [InlineKeyboardButton(text="Кола 2л", callback_data="kola")],
    [InlineKeyboardButton(text="Мохито", callback_data="moxito")],
    [InlineKeyboardButton(text="Бабл ти", callback_data="babl_ti")],
    [back_button],
])

# Десерты
dessert_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Генерал", callback_data="general")],
    [InlineKeyboardButton(text="Рошен", callback_data="roshen")],
    [InlineKeyboardButton(text="Чизкейк", callback_data="chizkeyk")],
    [back_button],
])

# Клавиатура для показа цены с кнопками "Назад" и "Главное меню"
def price_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [back_button, main_menu_button]
    ])







