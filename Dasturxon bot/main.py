import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = ''


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


from keyboards import *


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("""Tilni tanglang
Выберите язык""",reply_markup=menu_keyboard)


@dp.message_handler(text='Uzb')
async def send_welcome(message: types.Message):
    await message.reply("""Assalomu alaykum! Dasturxon botimizga xush kelibsiz.
Bugun bizning menumizda:
1.Norin🍝
2.Сhuchvara
3.Yupqa
4.Somsa🥟
5.Manti🦪
6.Lapsha hamiri🍜
7.Somsa hamiri
8.Muraveynik
9.Rogaliklar🥐
10.Paxlava🧇
11.Xolodes🍮
12.Chak-Chak
""", reply_markup=menu_uz_keyboard)


@dp.message_handler(text='Rus')
async def send_welcome(message: types.Message):
    await message.reply("""Здравствуйте!Добро пожаловать на Дастурхон бота.
Сегодня в нашем меню:
1.Нарын🍝
2.Пельмени
3.Юпка
4.Самса🥟
5.Манты🦪
6.Тесто для лапши🍜
7.Тесто для самсы
8.Муравейник
9.Рогалики🥐
10.Пахлава🧇
11.Холодец🍮
12.Чак-Чак
""", reply_markup=menu_ru_keyboard,)



@dp.message_handler(text='Rogaliklar🥐')
@dp.message_handler(text='Rogaliklar')
async def send_welcome(message: types.Message):
    await message.answer("""Rogaliklar🥐:
so'm/kg""")
    await message.answer_photo('https://imgur.com/hRRM1DR')


@dp.message_handler(text='Chak-Chak')
async def send_welcome(message: types.Message):
    await message.answer("""Chak-Chak:
- 25 000 so'm/tarelka""")
    await message.answer_photo('https://imgur.com/YWmZqYv')


@dp.message_handler(text='Norin🍝')
@dp.message_handler(text='Norin')
async def send_welcome(message: types.Message):
    await message.answer("""Norin:
- To'g'ralgan hamir go'shtsiz - 30 000 so'm/kg
- To'g'ralgan hamir go'shti bilan - 85 000 so'm/kg
""")
    await message.answer_photo('https://imgur.com/f6bwXHs')

@dp.message_handler(text='Somsa hamiri')
async def send_welcome(message: types.Message):
    await message.answer("""Somsa Hamiri:
- 35 000 so'm/kg""")
    await message.answer_photo('https://imgur.com/SDL4qnA')


@dp.message_handler(text='Somsa🥟')
@dp.message_handler(text='Somsa')
async def send_welcome(message: types.Message):
    await message.answer("""Somsa:
- Qovoqli 3 500 so'm/dona
- Go'shtli 6  000 so'm/dona
""")
    await message.answer_photo('https://imgur.com/3r02QSm')

@dp.message_handler(text='Paxlava🧇')
@dp.message_handler(text='Paxlava')
async def send_welcome(message: types.Message):
    await message.answer("""Paxlava:
- 30 000 so'm/upakovka (500 gramm)
(konteynerga alohida to'lanadi)""")
    await message.answer_photo('https://imgur.com/uIoaORu')

@dp.message_handler(text='Muraveynik')
async def send_welcome(message: types.Message):
    await message.answer("""Muraveynik:
- 6 000 so'm/dona""")
    await message.answer_photo('https://imgur.com/UdPXhUY')

@dp.message_handler(text='Yupqa')
async def send_welcome(message: types.Message):
    await message.answer("""Yupqa:
- 7 000 so'm/dona""")
    await message.answer_photo('https://imgur.com/oJCv3DN')


@dp.message_handler(text='Сhuchvara')
async def send_welcome(message: types.Message):
    await message.answer("""Chuchvara:
- 55 so'm/kg
Qo'virilgan chuchvara:
- 65 000 so'm/kg""")
    await message.answer_photo('https://imgur.com/sKV5vzp')

@dp.message_handler(text='Lapsha hamiri🍜')
@dp.message_handler(text='Lapsha hamiri')
async def send_welcome(message: types.Message):
    await message.answer("""Lapsha hamiri:
- Pachkasi 5 000 so'm/150 gramm""")
    await message.answer_photo('https://imgur.com/OxBASuV')

@dp.message_handler(text='Xolodes🍮')
@dp.message_handler(text='Xolodes')
async def send_welcome(message: types.Message):
    await message.answer("""Xolodes:
- 60 000 so'm/1000 gramm
- 30 000 so'm/500 gramm
(konteynerga alohida to'lanadi)""")
    await message.answer_photo('https://imgur.com/vydI0ig')


@dp.message_handler(text='Manti🦪')
@dp.message_handler(text='Manti')
async def send_welcome(message: types.Message):
    await message.answer("""Manti:
- Pishirilmagan 60 000 so'm/kg
- Tayor 4 000 so'm/dona""")
    await message.answer_photo('https://imgur.com/nBNCn4s')

@dp.message_handler(text='Buyurtma qilish')
async def send_welcome(message: types.Message):
    await message.answer("""Buyurtma qilish uchun raqam: +998 91-788-08-69,+998 90-109-15-18 yoki bizga yozing @zafarovich87,@ShaxnozaBekova""")


@dp.message_handler(text='Рогалики🥐')
@dp.message_handler(text='Рогалики')
async def send_welcome(message: types.Message):
    await message.answer("""Рогалики 
- сум/кг""")
    await message.answer_photo('https://imgur.com/hRRM1DR')


@dp.message_handler(text='Чак-Чак')
async def send_welcome(message: types.Message):
    await message.answer("""Чак-Чак:
- 25 000 сум/тарелка""")
    await message.answer_photo('https://imgur.com/YWmZqYv')


@dp.message_handler(text='Нарын🍝')
@dp.message_handler(text='Нарын')
async def send_welcome(message: types.Message):
    await message.answer("""Нарын:
- Нарезанное тесто 30 000 сум/кг 
- С мясом 85 000 сум/кг
""")
    await message.answer_photo('https://imgur.com/f6bwXHs')

@dp.message_handler(text='Тесто для самсы')
async def send_welcome(message: types.Message):
    await message.answer("""Тесто для самсы:
- 35 000 сум/кг""")
    await message.answer_photo('https://imgur.com/SDL4qnA')


@dp.message_handler(text='Юпка')
async def send_welcome(message: types.Message):
    await message.answer("""Юпка:
- 7 000 сум/шт""")
    await message.answer_photo('https://imgur.com/oJCv3DN')

@dp.message_handler(text='Самса🥟')
@dp.message_handler(text='Самса')
async def send_welcome(message: types.Message):
    await message.answer("""Самса:
- С тыквой 3 500 сум/шт
- С мясом 6 000 сум/шт""")
    await message.answer_photo('https://imgur.com/3r02QSm')

@dp.message_handler(text='Пахлава🧇')
@dp.message_handler(text='Пахлава')
async def send_welcome(message: types.Message):
    await message.answer("""Пахлава 
- 30 000 сум/упаковка (примерно 500 грамм)
(контейнеры оплачиваются отдельно)""")
    await message.answer_photo('https://imgur.com/uIoaORu')

@dp.message_handler(text='Муравейник')
async def send_welcome(message: types.Message):
    await message.answer("""Муравейник:
- 6 000 сум/шт""")
    await message.answer_photo('https://imgur.com/UdPXhUY')

@dp.message_handler(text='Пельмени')
async def send_welcome(message: types.Message):
    await message.answer("""Сырые пельмени:
- 55 000 сум/кг
Жаренные пельмени:
- 65 000 сум/1 кг
""")
    await message.answer_photo('https://imgur.com/sKV5vzp')

@dp.message_handler(text='Тесто для лапши🍜')
@dp.message_handler(text='Тесто для лапши')
async def send_welcome(message: types.Message):
    await message.answer("""Теста для лапши: 
- Пачка 5000 сум/150 грамм""")
    await message.answer_photo('https://imgur.com/OxBASuV')

@dp.message_handler(text='Холодец🍮')
@dp.message_handler(text='Холодец')
async def send_welcome(message: types.Message):
    await message.answer("""Холодец:
- 60 000 сум/кг
- 30 000 сум/500 грамм
(контейнеры оплачиваются отдельно)""")
    await message.answer_photo('https://imgur.com/vydI0ig')


@dp.message_handler(text='Манты🦪')
@dp.message_handler(text='Манты')
async def send_welcome(message: types.Message):
    await message.answer("""Манты:
- Сырые 60 000 сум/кг
- Приготовленные 4 000 сум/шт""")
    await message.answer_photo('https://imgur.com/nBNCn4s')

@dp.message_handler(text='Сделать заказ')
async def send_welcome(message: types.Message):
    await message.answer("""Чтобы сделать заказ позвоните номеру +998 91-788-08-69,+998 90-109-15-18 или напишите нам @zafarovich87,@ShaxnozaBekova""")


@dp.message_handler(commands=['stop'])
async def send_welcome(message: types.Message):
    await message.answer("""Действие прекрашено.Чтобы начать нажмите на команду /start
Mashq to'xtatildi.Boshlash uchun /start komandasini bo'sing""",reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Noto\'g\'ri buyruq berdingiz!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)