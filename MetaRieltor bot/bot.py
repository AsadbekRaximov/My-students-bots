import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ContentType

ADMINS = [5595643654]
API_TOKEN = "5904347795:AAFlB2Ce4A6_7WvjXPDhZFhpvaHbWz1D0x4"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


sell_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🎰Продать"), KeyboardButton("💳Сдать")]
    ],
    resize_keyboard=True
)

buy_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🤑Купить"), KeyboardButton("💸Взять")]
    ],
    resize_keyboard=True
)

type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🏢Квартира"),
            KeyboardButton("🏡Участок")
        ]
    ],
    resize_keyboard=True
)

place_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🌆Алмазарский"), KeyboardButton("🌆Бектемирский")],
        [KeyboardButton("🌆Мирабадский"), KeyboardButton("🌆Мирзо-Улугбекский")],
        [KeyboardButton("🌆Сергелийский"), KeyboardButton("🌆Учтепинский")],
        [KeyboardButton("🌆Чиланзарский"), KeyboardButton("🌆Шайхантахурский")],
        [KeyboardButton("🌆Юнусабадский"), KeyboardButton("🌆Яккасарайский")],
        [KeyboardButton("🌆Янгихаётский"), KeyboardButton("🌆Яшнабадский")],

    ],
    resize_keyboard=True
)

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📞Отправить номер☎", request_contact=True)]
    ], resize_keyboard=True
)

continue_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📝Продолжить заполнение заявки"), KeyboardButton("❌Отмена")]
    ], resize_keyboard=True
)


submit_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("✅Подтвердить"), KeyboardButton("❌Отмена")]
    ], resize_keyboard=True
)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    try:
        cur.execute(f"CREATE TABLE Users(ID INTEGER UNIQUE, Name TEXT, Username TEXT, State TEXT)")
    except:
        pass
    try:
        cur.execute(f"INSERT INTO Users (ID, Name, Username, State)"
                    f"Values({user_id}, '{name}', '@{username}', 'status')")
        con.commit()
    except:
        pass
    await message.answer("Вас приветствует бот MetaRieltor!!!\nЭтот бот поможет продать или сдать недвижимость в городе Ташкент🌆\nВыберите команду из списка:\n/sell - продать(сдать)недвижимость\n/buy - купить(взять) недвижимость")


@dp.message_handler(commands=["sell"])
async def sell(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    try:
        cur.execute(f"CREATE TABLE Sellers(ID INTEGER UNIQUE, Name TEXT, Username TEXT, State TEXT, Status TEXT, Type TEXT, Price TEXT, Size TEXT, Rooms TEXT, Place TEXT, Description Text, Image BLOB, Phone TEXT)")
    except:
        pass
    try:
        cur.execute(f"INSERT INTO Sellers (ID, Name, Username, State)"
                    f"Values({user_id}, '{name}', '@{username}', 'status')")
        con.commit()
    except:
        pass
    seller_state = cur.execute(f"SELECT State FROM Sellers WHERE ID = {user_id}").fetchone()[0]
    if seller_state == "status":
        await message.answer("Что вы хотите сделать?", reply_markup=sell_keyboard)
    else:
        await message.answer("🔹Вы ещё не закончили заполнение предыдущей заявки!!!", reply_markup=continue_keyboard)


@dp.message_handler(commands=["buy"])
async def sell(message: types.Message):
    await message.answer("DDDDD")


@dp.message_handler(content_types=ContentType.ANY)
async def echo(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text
    name = message.from_user.full_name
    username = message.from_user.username
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    try:
        cur.execute(f"CREATE TABLE Sellers(ID INTEGER UNIQUE, Name TEXT, Username TEXT, State TEXT, Status TEXT, Type TEXT, Price TEXT, Size TEXT, Rooms TEXT, Place TEXT, Description Text, Image BLOB, Phone TEXT, URL TEXT)")
    except:
        pass
    try:
        cur.execute(f"INSERT INTO Sellers (ID, Name, Username, State)"
                    f"Values({user_id}, '{name}', '@{username}', 'status')")
        con.commit()
    except:
        pass
    seller_state = cur.execute(f"SELECT State FROM Sellers WHERE ID = {user_id}").fetchone()[0]
    try:
        if seller_state == "status":
            if user_message == "🎰Продать":
                cur.execute(f"UPDATE Sellers SET State='type', status = '🎰Продаётся' WHERE ID = {user_id}")
                await message.answer("🏠Выберите тип недвижимасти", reply_markup=type_keyboard)
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("Что вы хотите сделать?", reply_markup=sell_keyboard)
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            elif user_message == "💳Сдать":
                cur.execute(f"UPDATE Sellers SET state='type', status = '🎰Сдаётся в аренду' WHERE ID = {user_id}")
                await message.answer("🏠Выберите тип недвижимасти", reply_markup=type_keyboard)
            else:
                await message.answer("🔸Пожалуйста, выберите то, что хотите сделать из списка!!!")

        elif seller_state == "type":
            if user_message == "🏡Участок":
                cur.execute(f"UPDATE Sellers SET state='price', type = '🏡Участок' WHERE ID = {user_id}")
                await message.answer("💵Отправьте цену в долларах($)", reply_markup=ReplyKeyboardRemove())
            elif user_message == "🏢Квартира":
                cur.execute(f"UPDATE Sellers SET state='price', type = '🏢Квартира' WHERE ID = {user_id}")
                await message.answer("💵Отправьте цену в долларах($)", reply_markup=ReplyKeyboardRemove())
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("🏠Выберите тип недвижимасти:", reply_markup=type_keyboard)
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            else:
                await message.answer("🔸Пожалуйста, выберите тип недвижимости из списка!!!")

        elif seller_state == "price":
            if user_message and user_message.isnumeric():
                cur.execute(f"UPDATE Sellers SET state='size', price = '{user_message}$' WHERE ID = {user_id}")
                await message.answer("🏠Отправьте площадь жилья в квадратных метрах(м²)")
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("💵Отправьте цену в долларах($)", reply_markup=ReplyKeyboardRemove())
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            else:
                await message.answer("🔸Пожалуйста, отправьте цену без никаких знаков в цифрах!!!")

        elif seller_state == "size":
            if user_message and user_message.isnumeric():
                cur.execute(f"UPDATE Sellers SET state='rooms', size = '{user_message}м²' WHERE ID = {user_id}")
                await message.answer("🛏️Отправьте количество комнат")
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("🏠Отправьте площадь жилья в квадратных метрах(м²)")
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            else:
                await message.answer("🔸Пожалуйста, отправьте размер без никаких знаков в цифрах!!!")

        elif seller_state == "rooms":
            if user_message and user_message.isnumeric():
                cur.execute(f"UPDATE Sellers SET state='place', rooms = '{user_message}' WHERE ID = {user_id}")
                await message.answer("🌆Выберите район", reply_markup=place_keyboard)
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("🛏️Отправьте количество комнат:")
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            else:
                await message.answer("🔸Пожалуйста, отправьте количество комнат без никаких знаков в цифрах!!!")

        elif seller_state == "place":
            if user_message in ["🌆Алмазарский", "🌆Бектемирский", "🌆Мирабадский", "🌆Мирзо-Улугбекский", "🌆Сергелийский", "🌆Учтепинский", "🌆Чиланзарский", "🌆Шайхантахурский", "🌆Юнусабадский", "🌆Яккасарайский", "🌆Янгихаётский", "🌆Яшнабадский"]:
                cur.execute(f"UPDATE Sellers SET state='description', place = '{user_message}' WHERE ID = {user_id}")
                await message.answer("📝Отправьте дополнительную информацию о недвижимости\n🔹Например, точное местоположение или состояние жилища.", reply_markup=ReplyKeyboardRemove())
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("🌆Выберите район", reply_markup=place_keyboard)
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            else:
                await message.answer("🔸Пожалуйста, выберите район из списка!!!")

        elif seller_state == "description":
            if user_message:
                cur.execute(f"UPDATE Sellers SET state='phone', description = '{user_message}' WHERE ID = {user_id}")
                await message.answer("📞Отправьте свой номер", reply_markup=phone_keyboard)
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("📝Отправьте дополнительную информацию о недвижимости\n🔹Например, точное местоположение или состояние жилища.", reply_markup=ReplyKeyboardRemove())
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")

        elif seller_state == "phone":
            if message.content_type == ContentType.CONTACT:
                phone_number = message["contact"]["phone_number"]
                cur.execute(f"UPDATE Sellers SET state='image', phone = '{phone_number}' WHERE ID = {user_id}")
                await message.answer("🖼️Отправьте 1 фото недвижимости", reply_markup=ReplyKeyboardRemove())
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            # elif message == re("^[\+]?[(]?[8-9]{3}[)]?[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{2}[-\s\.]?[0-9]{2}$"):
            #     cur.execute(f"UPDATE Sellers SET state='image', phone = '{message}' WHERE ID = {user_id}")
            #     await message.answer("🖼️Отправьте 1 фото недвижимости", reply_markup=ReplyKeyboardRemove())
            elif user_message == "📝Продолжить заполнение заявки":
                await message.answer("📞Отправьте свой номер", reply_markup=phone_keyboard)

        elif seller_state == "image":
            if message.content_type == 'photo':
                    photo_id = message["photo"][0]["file_id"]
                    cur.execute(f"UPDATE Sellers SET state = 'submit', image = '{photo_id}' WHERE ID = {user_id}")
                    seller_data = cur.execute(f"SELECT * FROM Sellers WHERE ID = {user_id}")
                    seller_data =seller_data.fetchall()[0]
                    photo = seller_data[11]
                    caption = f"📣@metarieltor_bot📣\n{seller_data[4]}\n{seller_data[5]}\n💵Цена: {seller_data[6]}\n🏠Площадь: {seller_data[7]}\n🛏️Количество комнат: {seller_data[8]}\n🌆Местоположение:  {seller_data[9]}\n📝Описание: {seller_data[10]}\n📞Контакт: {seller_data[12]}"
                    await message.answer_photo(photo=photo, caption=caption, reply_markup=submit_keyboard)
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")
            else:
                await message.answer("🔸Отправьте только 1 фото недвижимости")

        elif seller_state == "submit":
            if user_message == "✅Подтвердить":
                seller_data = cur.execute(f"SELECT * FROM Sellers WHERE ID = {user_id}")
                seller_data = seller_data.fetchall()[0]
                photo = seller_data[11]
                caption = f"📣{seller_data[4]}\n{seller_data[5]}\n💵Цена: {seller_data[6]}\n🏠Площадь: {seller_data[7]}\nКоличество комнат: {seller_data[8]}\n📍Местоположение: {seller_data[9]}\n📝Описание: {seller_data[10]}\n📞Контакт: {seller_data[12]}"
                await bot.send_photo(chat_id=ADMINS[0], photo=photo, caption=caption)
            elif user_message == "❌Отмена":
                cur.execute(f"DELETE FROM Sellers WHERE ID = {user_id}")

    except:
        await message.answer("Ошибка!!!")
    con.commit()
    con.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)