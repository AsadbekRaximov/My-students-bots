from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

home = KeyboardButton('⬅️ Orqaga')

gosht = KeyboardButton('🥩 Go`sht mahsulotlari')
sut_mahsulotlari = KeyboardButton('🍶 Sut mahsulotlari')
ichimliklar = KeyboardButton('🍹 Ichimliklar')
shirinliklar = KeyboardButton('🍰 Shirinliklar')
mevalar = KeyboardButton('🍏🍇🍋 Mevalar')
sabzavotlar = KeyboardButton('🥒🥕🫑 Sabzavotlar')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(gosht, sut_mahsulotlari, ichimliklar, shirinliklar, mevalar,
                                                         sabzavotlar)

mol = KeyboardButton('🥩 Mol goshti')
qoy = KeyboardButton('🥩 Qo`y goshti')
qiyma = KeyboardButton('Qiyma')
laxm = KeyboardButton('🥩 Laxm gosht')
Goshtlar = ReplyKeyboardMarkup(resize_keyboard=True).add(mol, qoy, qiyma, laxm, home)

tvorog = KeyboardButton('🍚 Tvorog')
qaymoq = KeyboardButton('🍶 Qaymoq')
sut = KeyboardButton('🥛 Sut')
sir = KeyboardButton('🧀 Sir')
saryog = KeyboardButton("🧈 Saryog'")
Sut_mahsulotlari = ReplyKeyboardMarkup(resize_keyboard=True).add(tvorog, qaymoq, sir, sut, saryog, home)

pepsi = KeyboardButton('Pepsi')
cola = KeyboardButton('Coca-Cola')
lipton = KeyboardButton('Lipton')
moxito = KeyboardButton('Mojito')
fanta = KeyboardButton('Fanta')
Ichimliklar = ReplyKeyboardMarkup(resize_keyboard=True).add(pepsi, fanta, cola, lipton, moxito, home)

tort = KeyboardButton('🥐 Rogalik')
disert = KeyboardButton('🍮 Medovik')
pirojni = KeyboardButton('🧁 Pirojni')
ponchik = KeyboardButton('🍩 Ponchik')
bodiroq = KeyboardButton('🍿 Popkorn')
Shirinliklar = ReplyKeyboardMarkup(resize_keyboard=True).add(tort, disert, pirojni, ponchik, bodiroq, home)

olma = KeyboardButton('🍏 Olma')
nok = KeyboardButton('🍐 Nok')
limon = KeyboardButton('🍋 Limon')
banan = KeyboardButton('🍌 Banan')
uzun = KeyboardButton('🍊 Apelsin')
Mevalar = ReplyKeyboardMarkup(resize_keyboard=True).add(olma, nok, limon, banan, uzun, home)

sabzi = KeyboardButton('🥕 Sabzi')
bodiring = KeyboardButton('🥔 Kartoshka')
piyoz = KeyboardButton('🧅 Piyoz')
baqlajon = KeyboardButton('🍆 Baqlajon')
pamidor = KeyboardButton('🥬 Karam')
Sabzavotlat = ReplyKeyboardMarkup(resize_keyboard=True).add(sabzi,bodiring,baqlajon,piyoz,pamidor,home)



