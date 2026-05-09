from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import (
Message,
ReplyKeyboardMarkup,
KeyboardButton,
ReplyKeyboardRemove,
)

from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio
import os

# =========================

# CONFIG

# =========================

TOKEN = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = -1003947220682

COACH_TOPIC_ID = 2

bot = Bot(
token=TOKEN,
default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

# =========================

# KEYBOARDS

# =========================

districts_keyboard = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="Andijon shahri")],
[KeyboardButton(text="Andijon tumani"), KeyboardButton(text="Asaka")],
[KeyboardButton(text="Baliqchi"), KeyboardButton(text="Bo‘z")],
[KeyboardButton(text="Buloqboshi"), KeyboardButton(text="Izboskan")],
[KeyboardButton(text="Jalaquduq"), KeyboardButton(text="Marhamat")],
[KeyboardButton(text="Oltinko‘l"), KeyboardButton(text="Paxtaobod")],
[KeyboardButton(text="Qo‘rg‘ontepa"), KeyboardButton(text="Shahrixon")],
[KeyboardButton(text="Ulug‘nor"), KeyboardButton(text="Xo‘jaobod")],
],
resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="🧑‍🏫 Murabbiy sifatida murojaat")],
[KeyboardButton(text="👦 Bolani ro‘yxatdan o‘tkazish")],
[KeyboardButton(text="📚 Batafsil ma’lumot")],
[KeyboardButton(text="📞 Aloqa")],
],
resize_keyboard=True
)

info_menu = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="⭐ Nima uchun Andijon FK?")],
[KeyboardButton(text="👨‍👩‍👦 Ota-onalar uchun")],
[KeyboardButton(text="🧑‍🏫 Murabbiylar uchun")],
[KeyboardButton(text="🚀 Futbolchilar uchun")],
[KeyboardButton(text="💻 Elektron tizim")],
[KeyboardButton(text="🏆 Liga va turnirlar")],
[KeyboardButton(text="ℹ️ Loyiha haqida")],
[KeyboardButton(text="⬅️ Orqaga")],
],
resize_keyboard=True
)

phone_button = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="📲 Raqamni yuborish", request_contact=True)]
],
resize_keyboard=True,
one_time_keyboard=True
)

ha_yoq = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="✅ Ha")],
[KeyboardButton(text="❌ Yo‘q")]
],
resize_keyboard=True
)

skip_button = ReplyKeyboardMarkup(
keyboard=[
[KeyboardButton(text="⏭ O‘tkazib yuborish")]
],
resize_keyboard=True
)

# =========================

# STATES

# =========================

class CoachForm(StatesGroup):
full_name = State()
birth_year = State()
phone = State()
telegram = State()
district = State()
mahalla = State()
experience = State()
has_group = State()
players_count = State()
has_field = State()
extra = State()

class PlayerForm(StatesGroup):
full_name = State()
birth_year = State()
district = State()
mahalla = State()
parent_phone = State()
extra = State()

# =========================

# START

# =========================

@dp.message(CommandStart())
async def start(message: Message):
text = (
"<b>⚽ Andijon FK rasmiy futbol to‘garaklari platformasiga xush kelibsiz.</b>\n\n"
"Endi Andijon viloyatining barcha hududlarida bolalar "
"mahallaning o‘zida shug‘ullanib turib ham klubning "
"rasmiy tarbiyalanuvchisi bo‘lish imkoniyatiga ega bo‘ladi.\n\n"
"Kerakli bo‘limni tanlang 👇"
)

```
await message.answer(text, reply_markup=main_menu)
```

# =========================

# INFO MENU

# =========================

@dp.message(F.text == "📚 Batafsil ma’lumot")
async def info_section(message: Message):
text = (
"<b>📚 Batafsil ma’lumot</b>\n\n"
"Kerakli bo‘limni tanlang 👇"
)

```
await message.answer(text, reply_markup=info_menu)
```

# =========================

# BACK BUTTON

# =========================

@dp.message(F.text == "⬅️ Orqaga")
async def back_to_main(message: Message):
await message.answer(
"Asosiy menyu 👇",
reply_markup=main_menu
)

# =========================

# WHY ANDIJON FK

# =========================

@dp.message(F.text == "⭐ Nima uchun Andijon FK?")
async def why_andijon(message: Message):
text = (
"<b>⚽ Nima uchun Andijon FK rasmiy to‘garaklari?</b>\n\n"
"✅ Rasmiy klub tizimi\n"
"✅ Elektron nazorat tizimi\n"
"✅ Davomat va statistika\n"
"✅ Liga va turnirlar\n"
"✅ Ota-onalar uchun monitoring\n"
"✅ Akademiya sari imkoniyat\n"
"✅ Iqtidorli futbolchilar uchun grant\n"
"✅ Professional futbolga yo‘l"
)

```
await message.answer(text)
```

# =========================

# PARENTS INFO

# =========================

@dp.message(F.text == "👨‍👩‍👦 Ota-onalar uchun")
async def parents_info(message: Message):
text = (
"<b>👨‍👩‍👦 Ota-onalar uchun</b>\n\n"
"Farzandingiz:\n\n"
"✅ rasmiy klub tizimida shug‘ullanadi\n"
"✅ davomat nazoratida bo‘ladi\n"
"✅ statistikasi yuritiladi\n"
"✅ murabbiy baholari shakllantiriladi\n"
"✅ liga va turnirlarda qatnashadi\n\n"
"Ota-onalar uchun maxsus elektron monitoring tizimi ishlab chiqilmoqda."
)

```
await message.answer(text)
```

# =========================

# COACH BENEFITS

# =========================

@dp.message(F.text == "🧑‍🏫 Murabbiylar uchun")
async def coach_benefits(message: Message):
text = (
"<b>🧑‍🏫 Murabbiylar uchun imkoniyatlar</b>\n\n"
"✅ Klub metodikasi asosida ishlash\n"
"✅ Elektron tizim orqali boshqaruv\n"
"✅ KPI va bonus tizimi\n"
"✅ Har oy master-klasslar\n"
"✅ Malaka oshirish treninglari\n"
"✅ Professional futbol tizimida faoliyat\n"
"✅ Iqtidorli futbolchilar uchun rag‘bat tizimi"
)

```
await message.answer(text)
```

# =========================

# PLAYER OPPORTUNITIES

# =========================

@dp.message(F.text == "🚀 Futbolchilar uchun")
async def player_opportunities(message: Message):
text = (
"<b>🚀 Futbolchilar uchun imkoniyatlar</b>\n\n"
"⚽ Klub akademiyasiga yo‘llanma\n"
"⚽ Grant asosida shug‘ullanish imkoniyati\n"
"⚽ Klub seleksiyalarida qatnashish\n"
"⚽ Professional futbolga yo‘l\n"
"⚽ Asosiy jamoa futbolchilari bilan uchrashuvlar\n"
"⚽ Liga va turnirlarda ishtirok"
)

```
await message.answer(text)
```

# =========================

# ELECTRONIC SYSTEM

# =========================

@dp.message(F.text == "💻 Elektron tizim")
async def electronic_system(message: Message):
text = (
"<b>💻 Yagona elektron tizim</b>\n\n"
"Platforma orqali:\n\n"
"✅ davomat\n"
"✅ statistika\n"
"✅ to‘lov nazorati\n"
"✅ murabbiy baholari\n"
"✅ liga natijalari\n"
"✅ futbolchilar rivojlanishi\n\n"
"kuzatib boriladi."
)

```
await message.answer(text)
```

# =========================

# LEAGUES

# =========================

@dp.message(F.text == "🏆 Liga va turnirlar")
async def leagues_info(message: Message):
text = (
"<b>🏆 Liga va turnirlar tizimi</b>\n\n"
"⚽ Har oyda turnirlar\n"
"⚽ Ichki liga tizimi\n"
"⚽ O‘yin statistikasi\n"
"⚽ Eng yaxshi futbolchilar reytingi\n"
"⚽ Sovrinli musobaqalar"
)

```
await message.answer(text)
```

# =========================

# PROJECT INFO

# =========================

@dp.message(F.text == "ℹ️ Loyiha haqida")
async def about_project(message: Message):
text = (
"<b>Andijon FK rasmiy futbol to‘garaklari</b>\n\n"
"Bu oddiy futbol mashg‘ulotlari emas.\n\n"
"⚽ Klub tizimida shug‘ullanish\n"
"⚽ Seleksiya va skautlar kuzatuvi\n"
"⚽ Akademiya sari yo‘l\n"
"⚽ Professional futbol muhiti\n\n"
"8 yoshdan boshlab qabul qilinadi."
)

```
await message.answer(text)
```

# =========================

# CONTACT

# =========================

@dp.message(F.text == "📞 Aloqa")
async def contacts(message: Message):
text = (
"<b>📞 Aloqa</b>\n\n"
"📱 Telefon: +998 XX XXX XX XX\n"
"📍 Manzil: Andijon\n"
"📲 Telegram: @username\n"
"📸 Instagram: @username"
)

```
await message.answer(text)
```

# =========================

# COACH FLOW

# =========================

@dp.message(F.text == "🧑‍🏫 Murabbiy sifatida murojaat")
async def coach_start(message: Message, state: FSMContext):

```
await state.set_state(CoachForm.full_name)

await message.answer(
    "📋 1/9\n\n"
    "F.I.SH kiriting 👇",
    reply_markup=ReplyKeyboardRemove()
)
```

@dp.message(CoachForm.full_name)
async def coach_name(message: Message, state: FSMContext):

```
await state.update_data(full_name=message.text)

await state.set_state(CoachForm.birth_year)

await message.answer(
    "📋 2/9\n\n"
    "Tug‘ilgan yilingizni kiriting"
)
```

@dp.message(CoachForm.birth_year)
async def coach_birth(message: Message, state: FSMContext):

```
if not message.text.isdigit():
    await message.answer("Faqat yil kiriting")
    return

await state.update_data(birth_year=message.text)

await state.set_state(CoachForm.phone)

await message.answer(
    "📋 3/9\n\n"
    "Telefon raqamingizni yuboring 👇",
    reply_markup=phone_button
)
```

@dp.message(CoachForm.phone)
async def coach_phone(message: Message, state: FSMContext):

```
phone = message.contact.phone_number if message.contact else message.text

await state.update_data(phone=phone)

await state.set_state(CoachForm.telegram)

await message.answer(
    "📋 4/9\n\n"
    "Telegram username (ixtiyoriy)\n"
    "Misol: @username",
    reply_markup=ReplyKeyboardRemove()
)
```

@dp.message(CoachForm.telegram)
async def coach_telegram(message: Message, state: FSMContext):

```
await state.update_data(telegram=message.text)

await state.set_state(CoachForm.district)

await message.answer(
    "📋 5/9\n\n"
    "Hududingizni tanlang 👇",
    reply_markup=districts_keyboard
)
```

@dp.message(CoachForm.district)
async def coach_district(message: Message, state: FSMContext):

```
await state.update_data(district=message.text)

await state.set_state(CoachForm.mahalla)

await message.answer(
    "📋 6/9\n\n"
    "Mahallangiz nomini kiriting 👇",
    reply_markup=ReplyKeyboardRemove()
)
```

@dp.message(CoachForm.mahalla)
async def coach_mahalla(message: Message, state: FSMContext):

```
await state.update_data(mahalla=message.text)

await state.set_state(CoachForm.experience)

await message.answer(
    "📋 7/9\n\n"
    "Futbol yoki murabbiylik tajribangiz haqida yozing"
)
```

@dp.message(CoachForm.experience)
async def coach_experience(message: Message, state: FSMContext):

```
await state.update_data(experience=message.text)

await state.set_state(CoachForm.has_group)

await message.answer(
    "📋 8/9\n\n"
    "Hozir guruhingiz bormi?",
    reply_markup=ha_yoq
)
```

@dp.message(CoachForm.has_group)
async def coach_group(message: Message, state: FSMContext):

```
await state.update_data(has_group=message.text)

if message.text == "✅ Ha":

    await state.set_state(CoachForm.players_count)

    await message.answer(
        "Nechta bola shug‘ullanadi?",
        reply_markup=ReplyKeyboardRemove()
    )

else:

    await state.update_data(players_count="0")

    await state.set_state(CoachForm.has_field)

    await message.answer(
        "📋 9/9\n\n"
        "Mashg‘ulot uchun maydon bormi?",
        reply_markup=ha_yoq
    )
```

@dp.message(CoachForm.players_count)
async def coach_players(message: Message, state: FSMContext):

```
await state.update_data(players_count=message.text)

await state.set_state(CoachForm.has_field)

await message.answer(
    "📋 9/9\n\n"
    "Mashg‘ulot uchun maydon bormi?",
    reply_markup=ha_yoq
)
```

@dp.message(CoachForm.has_field)
async def coach_field(message: Message, state: FSMContext):

```
await state.update_data(has_field=message.text)

await state.set_state(CoachForm.extra)

await message.answer(
    "Qo‘shimcha ma’lumot yuborishingiz mumkin",
    reply_markup=skip_button
)
```

@dp.message(CoachForm.extra)
async def coach_finish(message: Message, state: FSMContext):

```
extra = message.text

if extra == "⏭ O‘tkazib yuborish":
    extra = "Yo‘q"

await state.update_data(extra=extra)

data = await state.get_data()

admin_text = f"""
```

🔔 <b>Yangi murabbiy arizasi</b>

👤 Ism: {data['full_name']}
📅 Tug‘ilgan yil: {data['birth_year']}
📞 Telefon: {data['phone']}
📲 Telegram: {data['telegram']}
📍 Hudud: {data['district']} / {data['mahalla']}
⚽ Tajriba: {data['experience']}
👥 Guruh: {data['has_group']}
👦 Bolalar soni: {data['players_count']}
🏟 Maydon: {data['has_field']}
📝 Qo‘shimcha: {data['extra']}
"""

```
await bot.send_message(
    chat_id=GROUP_CHAT_ID,
    text=admin_text,
    message_thread_id=COACH_TOPIC_ID
)

await message.answer(
    "✅ Murojaatingiz qabul qilindi.\n\n"
    "Mutaxassislarimiz siz bilan bog‘lanadi.\n\n"
    "Mahalladan katta futbolga.",
    reply_markup=main_menu
)

await state.clear()
```

# =========================

# PLAYER FLOW

# =========================

@dp.message(F.text == "👦 Bolani ro‘yxatdan o‘tkazish")
async def player_start(message: Message, state: FSMContext):

```
await state.set_state(PlayerForm.full_name)

await message.answer(
    "📋 1/5\n\n"
    "Farzandingiz F.I.SH kiriting 👇",
    reply_markup=ReplyKeyboardRemove()
)
```

@dp.message(PlayerForm.full_name)
async def player_name(message: Message, state: FSMContext):

```
await state.update_data(full_name=message.text)

await state.set_state(PlayerForm.birth_year)

await message.answer(
    "📋 2/5\n\n"
    "Bolaning tug‘ilgan yilini kiriting"
)
```

@dp.message(PlayerForm.birth_year)
async def player_birth(message: Message, state: FSMContext):

```
if not message.text.isdigit():
    await message.answer("Faqat yil kiriting")
    return

await state.update_data(birth_year=message.text)

await state.set_state(PlayerForm.district)

await message.answer(
    "📋 3/5\n\n"
    "Hududingizni tanlang 👇",
    reply_markup=districts_keyboard
)
```

@dp.message(PlayerForm.district)
async def player_district(message: Message, state: FSMContext):

```
await state.update_data(district=message.text)

await state.set_state(PlayerForm.mahalla)

await message.answer(
    "📋 4/5\n\n"
    "Mahallangiz nomini kiriting 👇",
    reply_markup=ReplyKeyboardRemove()
)
```

@dp.message(PlayerForm.mahalla)
async def player_mahalla(message: Message, state: FSMContext):

```
await state.update_data(mahalla=message.text)

await state.set_state(PlayerForm.parent_phone)

await message.answer(
    "📋 5/5\n\n"
    "Ota-ona telefon raqamini yuboring 👇",
    reply_markup=phone_button
)
```

@dp.message(PlayerForm.parent_phone)
async def player_phone(message: Message, state: FSMContext):

```
phone = message.contact.phone_number if message.contact else message.text

await state.update_data(parent_phone=phone)

await state.set_state(PlayerForm.extra)

await message.answer(
    "Qo‘shimcha ma’lumot yuborishingiz mumkin",
    reply_markup=skip_button
)
```

@dp.message(PlayerForm.extra)
async def player_finish(message: Message, state: FSMContext):

```
extra = message.text

if extra == "⏭ O‘tkazib yuborish":
    extra = "Yo‘q"

await state.update_data(extra=extra)

data = await state.get_data()

admin_text = f"""
```

👦 <b>Yangi bola ro‘yxatdan o‘tdi</b>

👤 Ism: {data['full_name']}
📅 Tug‘ilgan yil: {data['birth_year']}
📍 Hudud: {data['district']} / {data['mahalla']}
📞 Ota-ona: {data['parent_phone']}
📝 Qo‘shimcha: {data['extra']}
"""

```
await bot.send_message(
    chat_id=GROUP_CHAT_ID,
    text=admin_text,
    message_thread_id=PLAYER_TOPIC_ID
)

await message.answer(
    "✅ So‘rovingiz qabul qilindi.\n\n"
    "Hududingizdagi rasmiy to‘garak faoliyati boshlanishi bilan siz bilan bog‘lanamiz.",
    reply_markup=main_menu
)

await state.clear()
```

# =========================

# RUN BOT

# =========================

async def main():
print("Bot ishga tushdi...")
await dp.start_polling(bot)

if **name** == "**main**":
asyncio.run(main())
