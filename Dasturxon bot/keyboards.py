from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Uzb"),KeyboardButton("Rus")
        ],
    ],
    resize_keyboard=True
)


menu_uz_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Norin🍝"),KeyboardButton("Сhuchvara")
        ],
        [
            KeyboardButton("""Yupqa"""),KeyboardButton("Somsa🥟")
        ],
        [
            KeyboardButton("Manti🦪"),KeyboardButton("Lapsha hamiri🍜")
        ],
        [
            KeyboardButton("Somsa hamiri"),KeyboardButton("Muraveynik")
        ],
        [
            KeyboardButton("Rogaliklar🥐"), KeyboardButton("Paxlava🧇")
        ],
        [
            KeyboardButton("Xolodes🍮"),KeyboardButton("Chak-Chak")
        ],
        [
            KeyboardButton("Buyurtma qilish")
        ]
    ],
    resize_keyboard=True
)


menu_ru_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Нарын🍝"),KeyboardButton("Пельмени")
        ],
        [
            KeyboardButton("Юпка"),KeyboardButton("Самса🥟")
        ],
        [
            KeyboardButton("Манты🦪"),KeyboardButton("Тесто для лапши🍜")
        ],
        [
            KeyboardButton("Тесто для самсы"),KeyboardButton("Муравейник")
        ],
        [
            KeyboardButton("Рогалики🥐"), KeyboardButton("Пахлава🧇")
        ],
        [
            KeyboardButton("Холодец🍮"),KeyboardButton("Чак-Чак")
        ],
        [
            KeyboardButton("Сделать заказ")
        ]
    ],
    resize_keyboard=True
)


