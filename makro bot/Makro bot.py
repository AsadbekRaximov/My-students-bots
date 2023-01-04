import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, InlineKeyboardButton, InlineKeyboardMarkup
import makro_kp as mk

API_TOKEN = '5685410019:AAG8j3gz3v_ClFbnjwBCrehTcthXESH3epc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_start(message: types.Message):
    await message.answer(
        f'Assalomu alaykum {message.from_user.full_name}.\nBu makro bot,bu bot yordamida siz bizning mahsulotlarimiznig bilib olishingiz mumkun',
        reply_markup=mk.mainMenu)


@dp.message_handler(text="🥩 Mol goshti")
async def all2(message: types.Message):
    await message.answer('🥩 Mol goshti')
    await message.delete()
    photo = InputFile('./images/mol go`shti.jpg')
    await message.answer_photo(photo=photo)


@dp.message_handler(text="🥩 Qo`y goshti")
async def all2(message: types.Message):
    await message.answer('🥩 Qo`y goshti')
    await message.delete()
    photo = InputFile('./images/qoy go`shti.jpg')
    await message.answer_photo(photo=photo)


@dp.message_handler(text="Qiyma")
async def all2(message: types.Message):
    await message.answer('Qiyma')
    await message.delete()
    photo = InputFile('./images/qiyma.jpg')
    await message.answer_photo(photo=photo)


@dp.message_handler(text="🥩 Laxm gosht")
async def all2(message: types.Message):
    await message.answer('🥩 Laxm gosht')
    await message.delete()
    photo = InputFile('./images/laxm.jpg')
    await message.answer_photo(photo=photo,caption="🥩 Laxm gosht 1kg 89.990 so'm")


@dp.message_handler(text='🍚 Tvorog')
async def all2(message: types.Message):
    await message.answer('🍚 Tvorog')
    await message.delete()
    photo = InputFile('./images/medium_1513165848502020401-00118.jpg')
    await message.answer_photo(photo=photo,caption="Tvorog Kamilka 5% 200g narxi 10.490 so'm")


@dp.message_handler(text="🍶 Qaymoq")
async def all2(message: types.Message):
    await message.answer('🍶 Qaymoq')
    await message.delete()
    photo = InputFile('./images/medium_1615876865540_MG_7630-1.jpg')
    await message.answer_photo(photo=photo,caption="Qaymoq Dobroye derevenskoe utro 35%200g narxi 9.990 so'm")


@dp.message_handler(text="🥛 Sut")
async def all2(message: types.Message):
    await message.answer('🥛 Sut')
    await message.delete()
    photo = InputFile('./images/medium_164962632545632.jpg')
    await message.answer_photo(photo=photo,caption="Sut Lactel 3,2% tetra 1L narxi 10.490 so'm")


@dp.message_handler(text="🧀 Sir")
async def all2(message: types.Message):
    await message.answer('🧀 Sir')
    await message.delete()
    photo = InputFile('./images/hanskiy sir.jpg')
    await message.answer_photo(photo=photo,caption="Hanskiy sir narxi 27.890 so'm")


@dp.message_handler(text="🧈 Saryog'")
async def all2(message: types.Message):
    await message.answer("🧈 Saryog'")
    await message.delete()
    photo = InputFile('./images/saryog`.jpg')
    await message.answer_photo(photo=photo,caption="Sariyog' Prezident 82% 125g narxi 19.990")


pepsikb = InlineKeyboardMarkup(row_width=4)
pepsiButton1 = InlineKeyboardButton(text='Pepsi 0.5L', callback_data='Pepsi 0.5L')
pepsiButton2 = InlineKeyboardButton(text='Pepsi 1L', callback_data='Pepsi 1L')
pepsiButton3 = InlineKeyboardButton(text='Pepsi 1.5L', callback_data='Pepsi 1.5L')
pepsiButton4 = InlineKeyboardButton(text='Pepsi 2L', callback_data='Pepsi 2L')
pepsikb.add(pepsiButton1, pepsiButton2, pepsiButton3,pepsiButton4)


colakb = InlineKeyboardMarkup(row_width=3)
colaButton1 = InlineKeyboardButton(text='Coca-Cola 0.5L', callback_data='Coca-Cola 0.5L')
colaButton2 = InlineKeyboardButton(text='Coca-Cola 1L', callback_data='Coca-Cola 1L')
colaButton3 = InlineKeyboardButton(text='Coca-Cola 1.5L', callback_data='Coca-Cola 1.5L')
colakb.add(colaButton1, colaButton2, colaButton3)


fantakb = InlineKeyboardMarkup(row_width=3)
fantaButton1 = InlineKeyboardButton(text='Fanta 0.5L', callback_data='Fanta 0.5L')
fantaButton2 = InlineKeyboardButton(text='Fanta 1L', callback_data='Fanta 1L')
fantaButton3 = InlineKeyboardButton(text='Fanta 1.5L', callback_data='Fanta 1.5L')
fantakb.add(fantaButton1, fantaButton2, fantaButton3)


liptonkb = InlineKeyboardMarkup(row_width=2)
liptonButton1 = InlineKeyboardButton(text='Lipton 0.5L', callback_data='Lipton 0.5L')
liptonButton2 = InlineKeyboardButton(text='Lipton 1L', callback_data='Lipton 1L')
liptonkb.add(liptonButton1,liptonButton2)

@dp.message_handler(text="Pepsi")
async def all2(message: types.Message):
    await message.delete()
    photo = InputFile('./images/pepsi 1.5l.jpg')
    await message.answer_photo(photo=photo)
    await message.answer('Pepsi', reply_markup=pepsikb)


@dp.callback_query_handler(text="Pepsi 0.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/pepsi 0.5l.jpg')
    await callback.message.answer_photo(photo,caption="Pepsi 0.5L narxi 4.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Pepsi 1L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/pepsi 1l.jpg')
    await callback.message.answer_photo(photo,caption="Pepsi 1L narxi 7.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Pepsi 1.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/pepsi 1.5l.jpg')
    await callback.message.answer_photo(photo,caption="Pepsi 1.5L narxi 9.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Pepsi 2L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/pepsi 2l.jpg')
    await callback.message.answer_photo(photo,caption="Pepsi 2L narxi 12.990 so'm")
    await callback.answer()


@dp.message_handler(text="Coca-Cola")
async def all2(message: types.Message):
    await message.answer('Coca-Cola')
    await message.delete()
    photo = InputFile('./images/CocaCola1.5.jpg')
    await message.answer_photo(photo=photo,reply_markup=colakb)

@dp.callback_query_handler(text="Coca-Cola 0.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/CocaCola0.5.jpg')
    await callback.message.answer_photo(photo,caption="Coca-Cola 0.5L narxi 4.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Coca-Cola 1L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/CocaCola1l.jpg')
    await callback.message.answer_photo(photo,caption="Coca-Cola 1L narxi 7.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Coca-Cola 1.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/CocaCola1.5.jpg')
    await callback.message.answer_photo(photo,caption="Coca-Cola 1.5L narxi 9.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Lipton 0.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/lipton 0.5l.jpg')
    await callback.message.answer_photo(photo,caption="Lipton 0.5L narxi 3.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Lipton 1L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/lipton 1l.jpg')
    await callback.message.answer_photo(photo,caption="Lipton 1L narxi 7.490 so'm")
    await callback.answer()


@dp.message_handler(text="Lipton")
async def all2(message: types.Message):
    await message.answer('Lipton')
    await message.delete()
    photo = InputFile('./images/lipton 1l.jpg')
    await message.answer_photo(photo=photo,reply_markup=liptonkb)


@dp.message_handler(text="Mojito")
async def all2(message: types.Message):
    await message.answer('Mojito')
    await message.delete()
    photo = InputFile('./images/moxito.jpg')
    await message.answer_photo(photo=photo,caption="Mojito 0.5L narxi 5.990 s'om")


@dp.message_handler(text="Fanta")
async def all2(message: types.Message):
    await message.answer('Fanta')
    await message.delete()
    photo = InputFile('./images/Fanta 1.5.jpg')
    await message.answer_photo(photo=photo,reply_markup=fantakb)


@dp.callback_query_handler(text="Fanta 0.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/Fanta 0.5.jpg')
    await callback.message.answer_photo(photo,caption="Fanta 0.5L narxi 4.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Fanta 1L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/Fanta 1l.jpg')
    await callback.message.answer_photo(photo,caption="Fanta 1L narxi 7.990 so'm")
    await callback.answer()


@dp.callback_query_handler(text="Fanta 1.5L")
async def all2(callback: types.CallbackQuery):
    photo =  InputFile('./images/Fanta 1.5.jpg')
    await callback.message.answer_photo(photo,caption="Fanta 1.5L narxi 9.990 so'm")
    await callback.answer()


@dp.message_handler(text="🥐 Rogalik")
async def all2(message: types.Message):
    await message.answer('🥐 Rogalik')
    await message.delete()
    photo = InputFile('./images/Rogalik .jpg')
    await message.answer_photo(photo=photo,caption="Rogalik 'Gde tort?' kuraga &yong'oq 300g narxi 20.990 so'm")


@dp.message_handler(text="🧁 Pirojni")
async def all2(message: types.Message):
    await message.answer('🧁 Pirojni')
    await message.delete()
    photo = InputFile('./images/Pirojni .jpg')
    await message.answer_photo(photo=photo,caption="Pirojni Gde tort? Yojik 240g narxi 16.990 so'm")


@dp.message_handler(text="🍩 Ponchik")
async def all2(message: types.Message):
    await message.answer('🍩 Ponchik')
    await message.delete()
    photo = InputFile('./images/Ponchik.jpg')
    await message.answer_photo(photo=photo,caption="Ponchiklar Aprel shokoladli qiyom bilan 300g narxi 15.490 so'm")


@dp.message_handler(text="🍿 Popkorn")
async def all2(message: types.Message):
    await message.answer('🍿 Popkorn')
    await message.delete()
    photo = InputFile('./images/Popkorn.jpg')
    await message.answer_photo(photo=photo,caption="Popkorn Amerikancha shokolad bilan 150g narxi 22.990 so'm")


@dp.message_handler(text="🍏 Olma")
async def all2(message: types.Message):
    await message.answer('🍏 Olma')
    await message.delete()
    photo = InputFile('./images/olma.jpg')
    await message.answer_photo(photo=photo,caption="Olma Simirenko 1kg narxi 14.990 so'm")


@dp.message_handler(text="🍐 Nok")
async def all2(message: types.Message):
    await message.answer('🍐 Nok')
    await message.delete()
    photo = InputFile('./images/nok.jpg')
    await message.answer_photo(photo=photo,caption="Nok 1kg narxi 29.990 so'm")


@dp.message_handler(text="🍋 Limon")
async def all2(message: types.Message):
    await message.answer('🍋 Limon')
    await message.delete()
    photo = InputFile('./images/limon.jpg')
    await message.answer_photo(photo=photo,caption="Limon 1kg narxi 42.990 so'm")


@dp.message_handler(text="🍌 Banan")
async def all2(message: types.Message):
    await message.answer('🍌 Banan')
    await message.delete()
    photo = InputFile('./images/banan.jpg')
    await message.answer_photo(photo=photo,caption="Banan 1kg narxi 17.990 so'm")


@dp.message_handler(text="🍊 Apelsin")
async def all2(message: types.Message):
    await message.answer('🍊 Apelsin')
    await message.delete()
    photo = InputFile('./images/apelsin.jpg')
    await message.answer_photo(photo=photo,caption="Apelsin Egipet 1kg narxi 21.990 so'm")


@dp.message_handler(text="🥕 Sabzi")
async def all2(message: types.Message):
    await message.answer('🥕 Sabzi')
    await message.delete()
    photo = InputFile('./images/sabzi.jpg')
    await message.answer_photo(photo=photo,caption="Sariq sabzi 1kg narxi 5.990 so'm")


@dp.message_handler(text="🥔 Kartoshka")
async def all2(message: types.Message):
    await message.answer('🥔 Kartoshka')
    await message.delete()
    photo = InputFile('./images/kartoshka.jpg')
    await message.answer_photo(photo=photo,caption="Oq kartoshka 1kg narxi 5.990 so'm")


@dp.message_handler(text="🧅 Piyoz")
async def all2(message: types.Message):
    await message.answer('🧅 Piyoz')
    await message.delete()
    photo = InputFile('./images/piyoz.jpg')
    await message.answer_photo(photo=photo,caption="Piyoz 1kg narxi 4.990 so'm")


@dp.message_handler(text="🍆 Baqlajon")
async def all2(message: types.Message):
    await message.answer('🍆 Baqlajon')
    await message.delete()
    photo = InputFile('./images/baqlajon.jpg')
    await message.answer_photo(photo=photo,caption="Baqlajon issiqhonadan 1kg narxi 8.990 so'm")


@dp.message_handler(text="🥬 Karam")
async def all2(message: types.Message):
    await message.answer('🥬 Karam')
    await message.delete()
    photo = InputFile('./images/Karam.jpg')
    await message.answer_photo(photo=photo,caption="Karam 1kg narxi 3.990 so'm")


@dp.message_handler()
async def all(message: types.Message):
    if message.text == '🥩 Go`sht mahsulotlari':
        await message.answer('🥩 Go`sht mahsulotlari', reply_markup=mk.Goshtlar)
        await message.delete()
    elif message.text == '🍶 Sut mahsulotlari':
        await message.answer('🍶 Sut mahsulotlari', reply_markup=mk.Sut_mahsulotlari)
        await message.delete()
    elif message.text == '🍹 Ichimliklar':
        await message.answer('🍹 Ichimliklar', reply_markup=mk.Ichimliklar)
        await message.delete()
    elif message.text == '🍰 Shirinliklar':
        await message.answer('🍰 Shirinliklar', reply_markup=mk.Shirinliklar)
        await message.delete()
    elif message.text == '🍏🍇🍋 Mevalar':
        await message.answer('🍏🍇🍋 Mevalar', reply_markup=mk.Mevalar)
        await message.delete()
    elif message.text == '🥒🥕🫑 Sabzavotlar':
        await message.answer('🥒🥕🫑 Sabzavotlar', reply_markup=mk.Sabzavotlat)
        await message.delete()
    elif message.text == '⬅️ Orqaga':
        await message.answer('Orqaga', reply_markup=mk.mainMenu)
        await message.delete()
    else:
        await message.answer('Nomalum buyruq')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
