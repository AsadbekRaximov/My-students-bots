import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Viloyatlar botiga xush kelibsiz!", reply_markup=start_keyboard)


@dp.message_handler(text='Toshkent📍')
async def echo(message: types.Message):
    await message.answer("Bu Toshkent shaxrining tumanlari ", reply_markup=Toshkent_keyboard)


@dp.message_handler(text='Orqaga🔙')
async def echo(message: types.Message):
    await message.answer("🏠Bosh menu", reply_markup=start_keyboard)


@dp.message_handler(text='Toshkent.vil📍')
async def echo(message: types.Message):
    await message.answer("Bu Toshkent viloyatining tumanlari ", reply_markup=Toshkentvil_keyboard)


@dp.message_handler(text='Namangan📍')
async def echo(message: types.Message):
    await message.answer("Bu Namangan viloyatining tumanlari ", reply_markup=Namangan_keyboard)


@dp.message_handler(text='Andijon📍')
async def echo(message: types.Message):
    await message.answer("Bu Andijon viloyatining tumanlari ", reply_markup=andijon_keyboard)


@dp.message_handler(text='Sirdaryo📍')
async def echo(message: types.Message):
    await message.answer("Bu Sirdaryo viloyatining tumanlari ", reply_markup=sirdaryo_keyboard)


@dp.message_handler(text='Jizzax📍')
async def echo(message: types.Message):
    await message.answer("Bu Jizzax viloyatining tumanlari ", reply_markup=Jizzax_keyboard)


@dp.message_handler(text='Samarqand📍')
async def echo(message: types.Message):
    await message.answer("Bu Samarqand viloyatining tumanlari ", reply_markup=samarqand_keyboard)


@dp.message_handler(text='Surxondaryo📍')
async def echo(message: types.Message):
    await message.answer("Bu Surxondaryo viloyatining tumanlari ", reply_markup=surxondaryo_keyboard)


@dp.message_handler(text='Navoiy📍')
async def echo(message: types.Message):
    await message.answer("Bu Navoiy viloyatining tumanlari ", reply_markup=Navoiy_keyboard)


@dp.message_handler(text='Buxoro📍')
async def echo(message: types.Message):
    await message.answer("Bu Buxoro viloyatining tumanlari ", reply_markup=Buxoro_keyboard)


@dp.message_handler(text='Xorazm📍')
async def echo(message: types.Message):
    await message.answer("Bu Xorazm viloyatining tumanlari ", reply_markup=Xorazm_keyboard)


@dp.message_handler(text='Qoraqalpog`iston📍')
async def echo(message: types.Message):
    await message.answer("Bu Qoraqalpog`iston Respublikasning tumanlari ", reply_markup=Qoraqalpoq_keyboart)


@dp.message_handler(text='Farg`ona📍')
async def echo(message: types.Message):
    await message.answer("Bu Farg`ona viloyatining tumanlari ", reply_markup= fargona_keyboard)


@dp.message_handler(text='Qashqadaryo📍')
async def echo(message: types.Message):
    await message.answer("Bu Qashqadaryo viloyatining tumanlari ", reply_markup=qashqadaryo_ketboard)


@dp.message_handler(text='Bektemir')
async def echo(message: types.Message):
    text = """Bektemir tumani (1990-yil gacha Narimonov) — Toshkentdagi maʼmuriy-hududiy birlik. 1960–81 yillar Bektemir shaharchasi: 1973–90 yillarda shahar, 1981–90 yillarda davlat va jamoat arbobi, yozuvchi Narimon Kerbalay Najaf ugli Narimonov (1870–1925) nomi bilan yuritilgan. 1990-yildan Toshkent shahri tarkibidagi tuman, hokimi Saidjamol Sultonov[1]. Chirchiq daryosining chap sohilida. Bu daryo Bektemir tumanini boshqa tumanlardan ajratib turadi. Maydoni 1,83 ming ga, shu jumladan koʻkalamzorlashtirilgan hududi 0,012 ming ga. Aholisi 29,9 ming kishi (2004). Koʻchalar soni 45 ta."""
    await message.answer_photo("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Tashkent_city_%28Uzbekistan%29_Bektemir_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Bektemir_district_%282018%29.png")
    await message.answer(text)

@dp.message_handler(text='Mirobod')
async def echo(message: types.Message):
    text = """Mirobod tumani (1992-yilgacha Lenin tumani) — Toshkentdagi maʼmuriy-hududiy birlik. 1929-yil Shayxontohur tumani bilan birgalikda tashkil etilgan. Hozirgi chegarasi 1977-yildan buyen oʻzgarmagan. Tuman T.ning janubiy qismida joylashgan. Shimoliyda Amir Temur xiyobonidan halqa yoʻligacha choʻzilgan. Maydoni 1,71 ming ga, shu jumladan koʻkalamzorlashtirilgan hududi —0,356 ming ga. Aholisi 123,8 ming kishi (2004). Koʻchalar soni 103 ta, shundan 8 tasi markaziy koʻcha hisoblanadi. Bularga Fitrat, Movarounnahr, Nukus, Kosmonavtlar koʻchasi, T. Shevchenko, Fargʻona yoʻli va boshqa kiradi. 39 ta mahalla mavjud. Mirobod tumani janubdan Bektemir, sharqdan Hamza, shimolidan Yunusobod, shimoli-gʻarbdan Yakkasaroy, janubi-gʻarbdan Sergeli tumanlari bilan chegaradosh. Tuman chegaralari Sharof Rashidov, Istiqlol, Oxunboboyev, Fargʻona yoʻli, Toshkent Katta halqa yoʻli, Beshkent, Fitrat, Turgʻunboyeva,. Oq yoʻl, Kichik Beshyogʻoch, Nukus, Kunayev koʻchalaridan oʻtadi. Toshkent metropolitenining "Oybek", "Toshkent" stansiyalari Mirobod tumani hududidadir. Tuman hududidan 4 ta kanal (Baratxoʻja, Qorasuv, Salor, Tolariq) oqib oʻtadi."""
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Tashkent_city_%28Uzbekistan%29_Mirobod_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Mirobod_district_%282018%29.png')
    await message.answer(text)

@dp.message_handler(text='Mirzo Ulugbek')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Tashkent_city_%28Uzbekistan%29_Mirzo_Ulugbek_district_%282018%29.png/300px-Tashkent_city_%28Uzbekistan%29_Mirzo_Ulugbek_district_%282018%29.png')
    text = """Mirzo Ulugʻbek tumani (1935-yilgacha — Proletar tumani, 1992-yilgacha Kuybishev tumani; 1992-yil maydan Mirzo Ulugʻbek tumani) — Toshkentdagi maʼmuriy-hududiy birlik. 1929 i. tashkil qilingan. Hozirgi chegarasi 1978-yildan buyen oʻzgarmagan. T.ning shimoli-sharqiy qismida joylashgan. T. markazi (Amir Temur xiyoboni)dan boshlanib, shimoli-sharqiy tomonga, Toshkent avtomobil halqa yoʻligacha boradi. Feruza mavzesi, Toshkent traktor zavodi, Ulugʻbek shaharchasi gʻam tuman hududiga kiradi. Maydoni 3,2 ming km², shu jumladan, koʻkalamzorlashtirilgan hudud — 0,579 ming ga. Aholisi 247,6 ming kishi (2004). Tuman hududida tarixiy va madaniy yodgorliklardan Kirxa (1892) saklangan. Koʻchalar soni 532 ta. Asosiy magistrallari: Pushkin, Parkent, Temur Malik, Oqqoʻrgʻon koʻchalari, Buyuk ipak yoʻli shohkoʻchasi, Habib Abdullayev koʻchasi, Kichik halqa yoʻl. 49 ta mahalla mavjud. Tuman hududida 377 yirik korxona, shundan 28 sanoat korxonasi (shu jumladan, "Toshkentkabel", traktor zavodlari, "Oʻzbekiston paxtachilik mashinasozligi", lokboʻyoq zavodlari.), 3119 kichik va oʻrta biznes subʼyektlari bor. 27 ilmiy tadqiqot instituta, 10 loyiha instituti, 4 oliy oʻquv yurti (Madaniyat instituti, Jahon iktisodiyoti va diplomatiya universiteti va boshqalar) xamda umumqoʻshin qoʻmondonlik bilim yurti, harbiy akademiya, Ichki ishlar vazirligi akademiyasi, Toshkent vrachlar malakasini oshirish instituti, yozuvchilar, kompozitorlar, meʼmorlar ijodiy uyushmalari va teatr jamiyati, 33 umumiy taʼlim maktabi, 12 kasbxunar kolleji, 4 bolalar musiqa maktabi va sanʼat maktabi, 10 kasalxona va dispanser, "Ona va bola" markazi, 11 oilaviy poliklinika, 2 tibbiysanitariya qismi ishlab turibdi."""
    await message.answer(text)


@dp.message_handler(text='Olmazor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Tashkent_city_%28Uzbekistan%29_Olmazar_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Olmazar_district_%282018%29.png')
    text = """Olmazor tumani – O‘zSSR Oliy Soveti Prezidiumining 1970 yil 7 dekabrdagi 1812-sonli Farmoniga asosan Sobir Rahimov nomi berilgan.
2010 yil 4 dekabr – O‘zbekiston Respublikasi Oliy Majlisi Senatining “Toshkent shahar Sobir Rahimov tumanining nomini o‘zgartirish to‘g‘risida”gi 133-II-sonli qarori asosida Sobir Rahimov tumani nomi o‘zgartirilib, unga Olmazor tumani nomi berildi.
“Yoshlik” talabalar shaharchasi – O‘zbekiston Respublikasi Vazirlar Mahkamasining 1992 yil 11 fevraldagi 60-sonli qarori bilan Sobir Rahimov, hozirgi Olmazor tumani hududida tashkil etilgan."""
    await message.answer(text)


@dp.message_handler(text='Uchtepa')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tashkent_city_%28Uzbekistan%29_Uchtepa_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Uchtepa_district_%282018%29.png')
    text = """UCHTEPA TUMANI (Farhod ko‘chasi, 21) – Toshkentdagi ma’muriy-hududiy birlik (6.05.2005 yil 6 maygacha Akmal Ikromov). 1977 yil 15 sentyabrda Chilonzor va Oktyabr (hozirgi Shayxontohur) tumanlarini ixchamlashtirish maqsadida, ular hududida tashkil etilgan. Janubi va janubi-sharqdan Zargarlik va Guliston ko‘chasi bilan boshlanib, g‘arb va shimoli-g‘arbda Toshkent avtomobil halqa yo‘li orqali Qoraqamish kanaliga tutashadi. Maydoni 2400 gektar, jumladan, ko‘kalamzor yerlari – 486 gektar. Aholisi 237,6 ming kishi (2009). Ko‘chalar soni 481 ta. Asosiy ko‘chalari: Lutfiy, Mannon Uyg‘ur, Farhod, Istirohat, Foziltepa, Nazarbek, Beshqayrag‘och va Kichik halqa yo‘li. Tumanda 53 ta mahalla va Chilonzor 9a, 11-15, 21-26 mavzelari mavjud. Tuman hududidan Bo‘zsuv va Qoraqamish kanallari oqib o‘tadi."""
    await message.answer(text)


@dp.message_handler(text='Shayxontohur')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Tashkent_city_%28Uzbekistan%29_Shaykhontohur_district_%282018%29.png/250px-Tashkent_city_%28Uzbekistan%29_Shaykhontohur_district_%282018%29.png')
    text = """Shayxontohur tumani — Toshkentdagi maʼmuriy-hududiy birlik. 1929-yil Oktabr tumani nomi bilan tuzilgan. 1992-yilda Shayxontohur (Shayx Xovandi Tohur) tumani deb oʻzgartirilgan. 1978-yildan hozirgi chegarada. Shimoli-gʻarbda Zangiota tumani, shimolida Uchtepa tumani (sobiq Sobir Rahimov)[1], shimoli-sharqda va sharqda Yunusobod, janubda Chilonzor va Yakkasaroy, gʻarbda Olmazor tumani (sobiq Akmal Ikromov)[1] tumanlari bilan chegaradosh. Maydoni 2,73 ming ga, shu jumladan koʻkalamzorlashtirilgan maydonlar 0,832 ming ga. Aholisi 263,1 ming kishi (2004). Koʻchalar soni 622 ta. Asosiy magistrallari: Abdulla Qodiriy, Navoiy, Uzbekistan, Beruniy shohkoʻchalari, Furqat, Uygʻur, Samarqand darvoza koʻchalari. Xalqlar doʻstligi, Xadra, Chorsu, Otstepa maydonlari, 48 ta mahalla bor."""
    await message.answer(text)


@dp.message_handler(text='Yashnobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Tashkent_city_%28Uzbekistan%29_Yashnobod_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Yashnobod_district_%282018%29.png')
    text = """Yashnobod tumani (avvalgi nomi Hamza) — Toshkentdagi maʼmuriyhududiy birlik. 1968 yilda tashkil qilingan. Hamza nomiga qoʻyilgan. Gʻarbda Amir Temur xiyoboni va Yoʻldosh Oxunboboyev koʻchasidan boshlab sharqda Ohangaron yoʻligacha davom etadi. Xududi 3,46 ming ga shu jumladan, koʻkalamzorlar — 172 ga. Aholisi 208,7 ming kishi (2004). Kuchalar soni 220 ta. Asosiy magistrallari: Jarqoʻrgʻon, Lisunov, Hamza, Yoʻldosh Oxunboboyev kuchalari va Fargona, Ohangaron yoʻllari. Hamza tumanida 50 ta mahalla mavjud."""
    await message.answer(text)


@dp.message_handler(text='Chilonzor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Tashkent_city_%28Uzbekistan%29_Chilanzar_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Chilanzar_district_%282018%29.png')
    text = """Chilonzor Toshkent shahrining janubi-gʻarbiy tumanidir. 1963-yilda rasman tashkil etilgan. Maydoni — 2 530 gektar. Uchtepa, Shayxontoxur, Yakkasaroy, Sirgʻali tumanlari bilan chegaradosh. Toshkent chekkasidagi Chilonzorda 1956-yildan boshlab zamonaviy binolar qurila boshlandi. 1966-yilgi zilziladan soʻng tumanda keng miqyosda qurilish ishlari boshlab yuborildi. Hozirda Chilonzor infratuzilmasi eng yaxshi rivojlangan tumanlardan biridir.
Chilonzorning eng birinchi gʻishtin uylaridan biri (Arnasoy va Muqimiy koʻchalari kesishmasi). Sentabr, 2007-yil.
Chilonzor tumani — T.dagi maʼmuriy-hududiy birlik. 1963-yilda tashkil kilingan. Toponimistlarning fikricha tuman nomi chilon (jiyda) oʻsimligidan olingan. T. zilzilasi (1966) dan keyin tumanda qurilish ishlari avj oldi. T.ning janubiy gʻarbiy qismida joylashgan. Shimoliyda Oktepa kanali, sharqda Boʻrijar kanali, janubi-gʻarbda Oʻrta Osiyo temir yoʻl boʻylab T. avtomobil halqa yoʻli va Bobur koʻchasigacha davom etgan. Maydoni 2994 ga, shu jumladan, koʻkalamzorlashtirilgan maydonlar 1,334 ming ga. Aholisi 217,1 ming kishi (2004). Koʻchalar soni 262 ta. 45 ta mahalla mavjud. Tumandagi baʼzi joylar T. tarixi bilan bogʻliq. Chilonzor Oktepasi arxeologik yodgorligi (4—8-asrlar, 10— 11-asrlar), Abulqosim Shayx madrasasi, Xayrobod Eshon meʼmoriy majmuasi kabi meʼmoriy yodgorliklar shu tuman xududida joylashgan."""
    await message.answer(text)


@dp.message_handler(text='Yunusobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tashkent_city_%28Uzbekistan%29_Yunusabad_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Yunusabad_district_%282018%29.png')
    text = """Yunusobod tumani — Toshkentdagi maʼmuriy-hududiy birlik. 1936 yilda Kirov tumani nomi bilan tashkil qilingan. 1992 yil may oyidan Yunusobod tumani deb ataladi.
Yunusobod nomining kelib chiqishi haqida turlicha fikrlar bor. Ayrim tadqiqotchilar (akademik A. Muhammadjonov) fikricha, joyning nomi juda qad. boʻlib, asli "Yunusrabot" deb atalgan. Bu oʻrinda "rabot" karvonsaroy maʼnosida qoʻllangan (qarang Rabot). Shimoliy tomondan shaharga kiruvchilar shu joyda qoʻnib oʻtishgan. Mahalliy ziyolilarning fikricha, joyning nomi sebzorlik tadbirkor Yunushoji Nodirhoji oʻgʻli (19-asr, Yunusobod Oktepasida bogʻrogʻlari boʻlgan) haqidagi rivoyatlar bilan bogʻliq.
Maydon 4,14 ming ga, shu jumladan, koʻkalamzorlashtirilgan maydon 1,073 ming ga. Aholisi 289,0 ming kishi (2004). Koʻchalar soni 441 ta. Asosiy magistral koʻchalari: Sharof Rashidov, Amir Temur, Ahmad Donish, Xurshid, Gʻani Mavlonov, Jahon Obidova, Gvardiya polkovnigi Xoʻjayev. 50 ta mahalla mavjud. Tuman hududida 3547 korxona va tashkilot boʻlib, kichik va oʻrta biznes subʼyektlarining sanoat ishlab chiqarishdagi ulushi 36,3%, qurilishda 64,2%, savdo va umumiy ovqatlanish sohasida 50,9% ni tashkil etadi. Ular orasida 155 ta qoʻshma korxona faoliyati ishlab chiqarish va aholiga xizmat koʻrsatishga yoʻnaltirilgan."""
    await message.answer(text)


@dp.message_handler(text='Yakkasaroy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Tashkent_city_%28Uzbekistan%29_Yakkasaray_district_%282018%29.png/1024px-Tashkent_city_%28Uzbekistan%29_Yakkasaray_district_%282018%29.png')
    text = """Yakkasaroy tumani yoki Yakkasaroy — Toshkentdagi maʼmuriy-hududiy birlik. 1936-yil Frunze tumani nomi bilan tashkil qilingan. 1992-yil maydan Yakkasaroy tumani deb ataldi. Tuman T.ning janubiy va qisman markaziy qismida joylashgan. Shimolida Oʻzbekiston koʻchasidan janubida Urta Osiyo temir yoʻl liniyasigacha choʻzilgan. Maydon 1,39 ming ga, shu jumladan, koʻkalamzorlashtirilgan hududi 0,144 ming ga. Aholisi 112,3 ming kishi (2004). Koʻchalar soni 156. Asosiy magistrallari: Bobur, Usmon Nosir, Nukus, Uzbekistan, Shota Rustaveli, Afrosiyob koʻchalari. 17 ta mahalla mavjud. Tuman hududida 24 sanoat korxonasi va 32 qurilish tashkiloti joylashgan. 3 avtotransport korxonasi, yuk ortishtushirish temir yoʻl styasi, avtovokzal ishlab turibdi. Yirik sanoat korxonalaridan "Toshtoʻqimachi" kombinati, "Toshkent yogʻochni qayta ishlash zdi", Temirbeton mahsulotlari zavodi, "Agama" korxonasi, poyabzal, Sanoatindustriya birlashmalari va b. faoliyat koʻrsatadi. 26 ilmiy tadqiqot instituta, loyihalash tashkilotlari va konstruktorlik byurosi, 4 oliy oʻkuv yurti (Nizomiy nomidagi Pedagogika universiteti, Toʻqimachilik va yengil sanoat instituti, Mannon Uygʻur nomidagi Sanʼat instituti, Toshkent Xoreografiya oliy maktabi), 6 ta kasbhunar kolleji va litseylar, 19 umumiy taʼlim, 2 sport, 2 musiqa maktablari, 8 kutubxona mavjud. Tuman aholisi salomatligi muhofazasini 14 davolash muassasasi va 5 ta oilaviy shifoxona taʼminlaydi. "Toʻqimachi" stadioni, 4 suzish havzasi, 29 sport zali, 89 korxona va muassasalarga qarashli sport maydonchalari, 2 megʻmonxona, 1 kinoteatr, 9 kutubxona, Bobur nomidagi madaniyat va istirohat bogi, Respublika Baynalminal madaniyat markazi, qoʻgʻirchoq teatri, Amaliy sanʼat muzeyi, Oʻzbekiston Badiiy Akademiyasining koʻrgazmalar zali mavjud. Aholiga 97 oziq-ovqat, 60 sanoat mollari doʻkoni, 188 umumiy ovqatlanish korxonasi, 129 maishiy xizmat koʻrsatish shoxobchasi, "Askiya" dehqon bozori xizmat koʻrsatadi."""
    await message.answer(text)


@dp.message_handler(text='Yuqori chirchiq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yuqorichirchiq_tumani.png/1280px-Yuqorichirchiq_tumani.png')
    text = """Yuqori chirchiq tumani — Toshkent viloyatidagi tuman. 1926-yil 29-sentyabrda tashkil etilgan. 1959-yilda Parkent tumani, 1962-yilda Boʻstonliq tumani qoʻshildi. 1964-yildan Boʻstonliq, 1979-yildan Parkent tumani ajralib chiqdi. Shimoli-sharqdan Boʻstonliq va Parkent, janub va janubi-sharqdan Ohangaron, janubi-gʻarbdan Oʻrta Chirchiq, gʻarbdan Toshkent shahri va Qibray tumanlari bilan chegaradosh. Mayd. 0,44 ming km². Aholisi 112,5 ming kishi (2005). Tumanda 1 shaharcha (Yangibozor), 9 qishloq fuqarolari yigʻini (Argʻinchi, Sosbaqa, Bordonkoʻl, Jambul, Oqovul, Navroʻz, Saksonota, Surankent, Tinchlik) bor. Tuman markazi — Yangibozor shaharchasi.
Tabiati. Tuman hududi Chirchiq daryosining chap sohilidagi tekislikda, oʻrtacha 550 m balandlikda joylashgan. Iqlimi kontinental. Sharq va shimoldan Chatqol tizmasi bilan oʻralgan. Qishi birmuncha sovuq, yozi issiq. Yanvarning oʻrtacha temperaturasi —1,5° dan —2° gacha, eng past temperatura — 20°. Iyulniki 25—28°, eng yuqori temperatura 41—42° gacha. Yillik oʻrtacha yogʻin 350–400 mm. Vegetatsiya davri 200 kun. Tuman hududidan oʻtgan Qorasuv, Chirchiq daryolari, Parkent, Hondam kanallari, Oqqulik, Yoyilma, Qizilsoy soylaridan qishloq xoʻjaligi ekinlarini sugʻorishda foydalaniladi. Tuproqlari boʻz tuproq. Yovvoyi oʻsimliklardan shoʻra, qamish, yulgʻun; kiyikoʻt, isiriq, gulxayri, qoraandiz, qizilmiya, ermon singari dorivor giyohlar va boshqalar oʻsadi. Yovvoyi hayvonlardan chiyaboʻri, tulki, ondatra, yumronqoziq, suvilonlar; qushlardan yovvoyi oʻrdak, tustovuq, qirgovul va boshqalar uchraydi."""
    await message.answer(text)


@dp.message_handler(text='O‘rta Chirchiq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/O%27rtachirchiq_tumani.png/1280px-O%27rtachirchiq_tumani.png')
    text = """Oʻrta chirchiq tumani — Toshkent viloyatidagi tuman. Hududining koʻp qismi Chirchiq daryosi bilan Toshkent kanali oraligʻida joylashgan. 1926-yil 29-sentabrda tashkil etilgan. Shim.sharqda Yuqori Chirchiq, sharqda Ohangaron tumanlari, shimolida Toshkent shahri, Zangiota tumani, gʻarbda Quyi Chirchiq, jan. da Oqqoʻrgʻon va Piskent tumanlari bilan chegaradosh. Maydoni 0,51 ming km2. Aholisi 163,4 ming kishi (2004). Tumanda 1 shahar (Nurafshon), 2 shaharcha (Tuyaboʻgʻiz, Yangihayot), 13 qishloq fuqarolari yigʻini (Angor, Doʻstlik, Istiqlol, Navoiy, Oxunboboyev, Oqota, Uyshun, Paxtakor, Paxtaobod, Yunuchqala, Yangiturmush, Oʻrtasaroy, Qorasuv) bor. Tuman markazi — Nurafshon shahri.
Tabiati. Tuman hududi Chirchiq daryosining chap sohilidagi tekislikda joylashgan. Iqlimi kontinental. Qishi sovuq, yozi issiq. Yanv. ning oʻrtacha temperaturasi 0—4°, eng past tra 19°, —20°. Iyulniki 28—30°, eng yuqori temperatura 41—42°. Oʻrtacha yillik yogʻin 450–460 mm. Vegetatsiya davri 300 kun. Tuman hududidan Polvonov nomidagi T°shkent, Qorasuv kanallari, shim.gʻarbidan Chirchiq daryosi oqib oʻtadi. Bir necha kollektor bor. Tuman janubida Tuyaboʻgʻiz suv ombori ("Toshkent dengizi") joylashgan. Tuproqlari boʻz tuproq. Yovvoyi oʻsimliklardan shoʻra, qamish, yulgʻun va boshqalar oʻsadi. Hayvonlardan chiyaboʻri, tulki, yumronqoziq, suvilonlar uchraydi.
Aholisi, asosan, oʻzbeklar, shuningdek, qozoq, tatar, rus, koreys va boshqalar millat vakillari ham yashaydi. Aholining oʻrtacha zichligi 1 km2ga 320,3 kishi (2004). Shahar aholisi 38,7 ming kishi, qishloq aholisi 124,7 ming kishi."""
    await message.answer(text)


@dp.message_handler(text='Bekobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Bekobod_tumani.png/1280px-Bekobod_tumani.png')
    text = """Bekobod tumani — Toshkent viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan (1962-yil 24-dekabrda Sirdaryo viloyati Yangiyer tumaniga qoʻshib yuborilgan, 1963-yil 17-aprelda kayta tuzilgan). Shimolida Toshkent viloyatining Boʻka tumani, gʻarbda Sirdaryo viloyati, sharq va janubida Tojikiston Respublikasi bilan chegaradosh. Maydoni 0,76 ming km². Aholisi 127,7 ming kishi (2000). Bekobod tumanida 1 shaharcha (Zafar) va 12 qishloq kengashi (Bahoriston, Bekobod, Guliston, Dalvarzin, Jumabozor, Madaniyat, Mehnatobod, Oxunboboyev, Pushkin, Chanoq, Yangi hayot, Qiyot) bor. Markazi—Zafar shaharchasi. Tabiati. Tuman xududi Dalvarzin choʻli va qisman Mirzachoʻlda joylashgan. Eng sharqida yer yuzasi bir oz oʻrqir. Tumanning adir qismida jar koʻp. Tuman hududi Sirdaryo tomon qiya. Iqlimi keskin kontinental. Yanvarning oʻrtacha temperaturasi —2,5°, iyulniki 28,5°. Yiliga 227 mm yogʻin tushadi. Vegetatsiya davri 220 kun. Tumanning janubida shamol koʻp boʻladi (qarang Bekobod shamoli). Janubi-sharqdan shimoli-sharqqa tomon Sirdaryo oqib oʻtadi. Sirdaryo sohilida qoldiq koʻllar (Qolgansir, Katta Qolgansir, Yangikoʻl, Haybatkoʻl, Qozon, Shoʻrkoʻl) bor. Dalvarzin (oʻng va soʻl tarmoqlari bilan), Jivali, Oʻrtoqli, Doʻstlik kanallari va Xasyoz arigʻi oqib oʻtadi. Tuprogʻi oʻtloqi va oʻtloqi-botqoq, oqish boʻz tuproq. Botqoq, shoʻr bosgan va eroziyaga uchragan yerlar ham bor. Bekobod tumanida miya, yantoq, qamish, koʻgʻa, yulgʻun, qiyoq kabi oʻsimliklar oʻsadi. Chiyaboʻri, toʻqay mushugi, boʻrsiq, qoʻshoyoq, koʻrsichqon, kaltakesak va ilonlar, qushlardan oʻrdak, loyxoʻrak, qirgʻovul, soʻfitoʻrgʻay, chumchuq va boshqa yashaydi"""
    await message.answer(text)


@dp.message_handler(text='Quyi Chirchiq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Quyichirchiq_tumani.png/1280px-Quyichirchiq_tumani.png')
    text = """Quyi chirchiq tumani - Toshkent viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. 1962-yil dekabrda Oqqoʻrgʻon tumaniga qoʻshib yuborilgan. 1973-yil dekabrda qayta tashkil qilingan, 1978 — 91 yillarda Gʻalaba tumani deb atalgan. Shimolida Chinoz va Yangiyoʻl, sharqda Oʻrta Chirchiq, janubida Oqqoʻrgʻon tumanlari, gʻarbdan Sirdaryo orqali Sirdaryo viloyati bilan chegaradosh. Maydoni 0,56 ming km2. Aholisi 96 ming kishi (2005). Tumanda 1 shahar (Doʻst-obod), 9 qishloq fuqarolari yigʻini (Gul, Istiqlol, Ketmontepa, May-dontol, Toshloq, Toshovul, Yangihayot, Oʻzbekiston, Qoʻrgʻoncha) bor. Markazi — Doʻstobod shahri   
Tabiati. Tuman hududi Chirchiq va Ohangaron daryolari quyi oqimlari oraligʻida joylashgan. Yer yuzasi, asosan, yassi tekislik, sharqdan gʻarbga tomon pasayib boradi. Iqlimi kontinental, qishi nisbatan yumshoq, yozi uzoq davom etadi, issiq va quruq. Yanv. ning oʻrtacha temperaturasi — G dan —1,5° gacha, iyul-niki 26— 27°. Yiliga 250–350 mm yogʻin tushadi. Vegetatsiya davri 200 — 212 kun. Sugʻorish kanallari oʻtkazilgan. tuprogʻi, asosan, boʻz tuproq. Grunt suvlari yer yuzasiga yaqin yerlarda oʻtloqi va oʻtloqi botqoq tuproqlar, daryo sohillarida allyuvial tuproqtar tarqalgan. Yerlar qishloq xoʻjaligi da oʻzlashtirilganidan tabiiy oʻsimliklar kam. Sirdaryo boʻylarida baʼzan toʻqaylar uchraydi. Yulgʻun, turan-gʻil, yovvoyi jiyda va boshqa oʻsadi. Yovvoyi hayvonlardan tulki, yumronqoziq, qoʻshoyoq, koʻrsichqon, toshbaqa, kaltake-sak, toʻqaylarda chiyaboʻri, yovvoyi quyon, qushlardan oʻrdak, qirgʻovul, chumchuq, loyxoʻrak va boshqa uchraydi. Suvlarida suv kalamushi, baqa, suv iloni, baliqlar bor."""
    await message.answer(text)


@dp.message_handler(text='Yangiyo‘l')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Yangiyo%27l_tumani.png/1280px-Yangiyo%27l_tumani.png')
    text = """Yangiyoʻl tumani — Toshkent viloyatidagi tuman. Viloyatning jan. gʻarbida. 1926-yil 29 sentabrda tashkil etilgan. Gʻarb va shim.gʻarbda Qozogʻistonning Janubiy Qozogʻiston viloyati, shim. va shim. sharqda Toshkent viloyatining Zangiota tumani, jan.sharqsa viloyatning Quyi Chirchiq, jan. gʻarbda Chinoz tumanlari bilan chegaradosh. Mayd. 0,42 ming km². Aholisi 157,7 ming kishi (2004). Tumanda 2 shaharcha (Gulbahor va Boʻzsuv), 8 qishloq fuqarolari yigʻini (Abdulla Ortiqov, Navbahor, Niyozboshi, Ubay Musayev, Xalqobod, Shoʻralisoy, Eski Qovunchi, Qoʻshyogʻoch) bor. Tuman markazi — Gulbahor shaharchasi.[1]
Tabiati. Tuman hududi, asosan, tekislikdan iborat boʻlib, adirlar uchraydi. Yer yuzasida Chirchiqning 5 ta terrasasi (koʻhna qayir) ajralib turadi. Tuproklari boʻz, oʻtloqi tuproqlar. Iqlimi kontinental. Yillik oʻrtacha temperatura 12,5° — 13°. Iyulning oʻrtacha temperaturasi 26°, yanvar
niki —1°, —2". Vegetatsiya davri 210 kun. Yiliga 280 – 282 mm yogʻin tushadi. Tuman hududidan Chirchiq daryosi, Kurkuldak, Joʻn, Boʻzsuv, Shimoliy Toshkent kanallari va ariqlar oqib oʻtadi. Yovvoyi oʻsimliklardan qamish, gʻumay, yantoq, shoʻra, pechak, ajriq, kakra va boshqalar oʻsadi. Yovvoyi hayvonlardan chiyaboʻri, tulki, quyon, jayra, boʻrsiq, parrandalardan yovvoyi oʻrdak va boshqalar uchraydi."""
    await message.answer(text)


@dp.message_handler(text='Zangiota')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Zangiota_tumani.png/1280px-Zangiota_tumani.png')
    text = """Zangiota tumani - Toshkent viloyatidagi tuman. 1933-yil 1 dekabrda tashkil etilgan (1992-yil maygacha Kalinin tumani deb atalgan). Hududi Toshkent sh.ning gʻarbi va jan.ga tutash. Shimolida Toshkent tumani, gʻarbda Qozogʻistonning Janubiy Qozogʻiston viloyati, sharqda Qibray, Oʻrta Chirchiq, Yuqori Chirchiq tumanlari, janubida Yangiyoʻl tumani bilan chegaradosh."""
    await message.answer(text)


@dp.message_handler(text='Boʻstonliq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Bo%27stonliq_tumani.png/1280px-Bo%27stonliq_tumani.png')
    text = """Boʻstonliq Toshkent viloyatidagi bir tumandir. Tuman markazi — Gʻazalkent shahri.[1] Boʻstonliq tumani Tyan-Shan tarmoqlarida togʻli joylarda joylashgan. Tuman 1963-yili uning hududida Chorvoq GES qurilishi boshlanishi bilan rivojlana ketdi. Hozirda Boʻstonliq tumani hududida Chimyon, Chorvoq, Burchmulla, Xumson kabi sanatoriy va oromgohlar joylashgan.
Boʻstonliq tumani — Toshkent viloyati tarkibidagi tuman. 1955 yil 19 aprelda tashkil etilgan (1962 yil 24 dekabr da Yuqori Chirchiq tumaniga qoʻshib yuborilgan, 1968 yil 25 dekabr da qayta tuzilgan). B. t. shimolida Qozogʻiston Respublikasining Janubiy Qozogʻiston viloyati, sharqda Qirgʻiziston Respublika sining Talas viloyati, janubi-sharda Oʻzbekiston Respublikasi Namangan viloyatining Pop tumani, shimoli-gʻarbda Toshkent viloyatining Qibray, janubida Yuqori Chirchiq, Parkent, Ohangaron tumanlari bilan chegaradosh. Maydon 4,93 ming km2. Aholisi 142,9 ming kishi (2000). B. t.da tumanga boʻysunuvchi 1 shahar (Gʻazalkent), 18 qishloq fuqarolari yigʻini (Bogʻiston, Boʻstonliq, Dumaloq, Jahonobod, Ozodbosh, Pargos, Sijjak, Soyliq, Toshpoʻlat Dadaboyev, Ugom, Xumson, Chimboyliq, Chimyon, Yangiovul, Qoramanas, Qoʻshqoʻrgʻon, Gʻalaba, Hondayliq) bor. Markazi — Gʻazalkent shahri (Toshkent sh.gacha 58 km)."""
    await message.answer(text)


@dp.message_handler(text='Boʻka')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Bo%27ka_tumani.png/1280px-Bo%27ka_tumani.png')
    text = """Boʻka tumani — Toshkent viloyati tarkibidagi tuman. Viloyatning jan.gʻarbiy qismida joylashgan. 1943-yil 18-mayda tashkil etilgan. Shim.gʻarbda viloyatning Oqqoʻrgʻon, shim.sharqda Piskent, jan.da Bekobod tumanlari bilan, gʻarbda Sirdaryo viloyatining Oqoltin va Guliston tumanlari, sharqda Tojikiston Respublikasi bilan chegaradosh. Maydoni 0,59 ming km². Aholisi 111,8 ming kishi (2001). Boʻka tumani da 1 shahar (Boʻka), 8 qishloq fuqarolari yigʻini (Boʻston, Koʻkorol, Namuna, Ravot, Turon, Chigʻatoy, Qoraqoʻyli, Qoʻshtepa) bor. Markazi — Boʻka shahri.[1]
Tabiati. Boʻka tumani hududi jan. va jan.gʻarbga tomon Sirdaryoga qiya tushgan togʻ oldi tekisligidan iborat. Iqlimi keskin kontinental, quruq iqliim. Yanvarning oʻrtacha temperaturasi —1" dan —1,5" gacha, iyulniki 27°. Vegetatsiya davri 210—215 kun. Yiliga 250–350 mm yogʻin tushadi. Boʻz tuproqlar bilan qoplangan,unumdor tekisliklarning koʻp qismi o'zlashtirilgan. Daryo bo'ylarida qumloq tuproqlar, Sirdaryo sohillarida toʻqayzorlar bor. Ularda chiyaboʻri,tulki,to'ng'iz, quyon, tustovuq uchraydi."""
    await message.answer(text)


@dp.message_handler(text='Chinoz')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Chinoz_tumani.png/1280px-Chinoz_tumani.png')
    text = """Chinoz tumani - Toshkent viloyatidagi tuman. 1935-yil 9-fevralda tashkil etilgan. 1962-yil 24 dekabrda Yangiyoʻl tumaniga qoʻshilgan. 1973-yil 12-aprel da qayta tuzilgan. Shimoliy va shim.sharqsan Yangiyoʻl, sharq va jan.sharqdan Quyi Chirchiq tumanlari, jan. va gʻarbdan Sirdaryo, shim.gʻarbdan Qozogʻiston Respublikasi bilan chegaradosh. Maydoni 0,34 ming km². Aholisi 116 ming kishi (2004). Tumanda 1 shahar (Chinoz), 2 shaharcha (Olmazor, Yangi Chinoz), 8 qishloq fuqarolari yigʻini (Islohot, Ittifoq, Koʻtarma, Turkiston, Chinoz, Eski Toshkent, Yallama, Uzbekistan) bor. Markazi — Chinoz shahriChinoz tumani - Toshkent viloyatidagi tuman. 1935-yil 9-fevralda tashkil etilgan. 1962-yil 24 dekabrda Yangiyoʻl tumaniga qoʻshilgan. 1973-yil 12-aprel da qayta tuzilgan. Shimoliy va shim.sharqsan Yangiyoʻl, sharq va jan.sharqdan Quyi Chirchiq tumanlari, jan. va gʻarbdan Sirdaryo, shim.gʻarbdan Qozogʻiston Respublikasi bilan chegaradosh. Maydoni 0,34 ming km². Aholisi 116 ming kishi (2004). Tumanda 1 shahar (Chinoz), 2 shaharcha (Olmazor, Yangi Chinoz), 8 qishloq fuqarolari yigʻini (Islohot, Ittifoq, Koʻtarma, Turkiston, Chinoz, Eski Toshkent, Yallama, Uzbekistan) bor. Markazi — Chinoz shahri"""
    await message.answer(text)


@dp.message_handler(text='Qibray')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/b/b3/Qibray_tumani.png')
    text = """Qibray tumani — Toshkent viloyatidagi tuman. 1933-yil 1-dekabrda tashkil etilgan. 1962-yil 24-dekabrda Kalinin (hozirgi Zangiota) tumani bilan birlashtirildi. 1964-yil 31-dekabrda qaytadan tuzildi. 1933 — 91 yillarda Orjonikidze tumani. Janubiy gʻarbdan Toshkent shahri, janubidan Yuqori Chirchiq, sharqdan Boʻstonliq, gʻarbdan Toshkent tumanlari, shimolidan Qozogʻiston Respublikasi bilan chegaradosh. Maydoni 0,56 ming km2. Aholisi 159,6 ming kishi (2004). Tumanda 2 shaharcha (Qibray, Salor), 11 qishloq fuqarolari yigʻini (Baytqoʻrgʻon, Yonariq, May, Matqobulov, Oqqovoq, Tuzel, Chinobod, Yangiobod, Oʻnqoʻrgʻon, Qiziltu, Qipchoq) bor. Tuman markazi — Qibray shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Ohangaron')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Ohangaron_tumani.png/1280px-Ohangaron_tumani.png')
    text = """Ohangaron tumani (1939-yilgacha Qurama tumani) — Toshkent viloyatidagi tuman. 1929-yil 29-sentabrda tashkil etilgan. 1957-yilda Oʻrta Chirchiq va Toshkent tumanlari tarkibiga qoʻshilgan. 1971-yil 31-avgustda qayta tashkil etildi. Shimolida Yuqori Chirchiq, Parkent, Boʻstonliq tumanlari, sharqdan Namangan viloyati, janubidan Tojikiston Respublikasi, janubi-gʻarbdan Piskent tumani va gʻarbdan Oʻrta Chirchiq tumani bilan chega-radosh. Maydoni 3,19 mingkm². Aholisi 78,1 ming kishi (2002). Ohangaron tumanida 1 shahar (Ohangaron), 8 qishloq fuqarolari yigʻini (Birlik, Doʻstlik, Ozodlik, Susam, Telov, Uvak, Qoraxitoy, Qurama) bor. Markazi — Ohangaron shahri"""
    await message.answer(text)


@dp.message_handler(text='Oqqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Oqqo%27rg%27on_tumani.png/1280px-Oqqo%27rg%27on_tumani.png')
    text = """Oqqoʻrgʻon tumani - Toshkent viloyatidagi tuman. 1935-yil 28-iyulda tashkil qilingan. Shimoliy va shimoli-gʻarbda Quyi Chirchiq tumani, gʻarb va janubi-gʻarbda Sirdaryo viloyati, shimoli-sharqda Oʻrta Chirchiq tumani, janub va janubi-sharqda Boʻka tumani, sharqda Piskent tumani bilan chegaradosh. Maydoni 0,40 ming km². Aholisi 86,8 ming kishi (2003). Tumanda 1 shahar (Oqqoʻrgʻon), 1 shaharcha (Alimkent), 10 qishloq fuqarolari yigʻini (Sultonobod, Achchi, Doʻstlik, Zarbdor, Zafar, Oytamgʻali, Oqqoʻrgʻon, Toshtoʻgʻon, Shohruxiya, Eltamgʻali, Erkinlik) bor. Tuman markazi — Oqqoʻrgʻon shahri"""
    await message.answer(text)


@dp.message_handler(text='Parkent')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Parkent_tumani.png/1280px-Parkent_tumani.png')
    text = """Parkent tumani - Toshkent viloyatidagi tuman. Hokimi Shohruh Shoahmedov (2021-yil 17-mart kuni tayinlangan)[1]. 1926-yil sentabrda tashkil etilgan. Shim., sharq va janubida Boʻstonliq, Ohangaron, gʻarbdan Yuqori Chirchiq va jan.-gʻarbdan Oʻrta Chirchiq tumanlari bilan chegaradosh. Maydoni 1,08 ming km². Aholisi 115 ming kishi (2003). Tumanda 1 shahar (Parkent), 9 qishloq fuqarolari yigʻini (Boshqizilsoy, Boʻston, Zarkent, Nomdanak, Parkent, Soʻqoq, Hisarak, Changi, Koraqalpoq) bor. Tuman markazi — Parkent shahri"""
    await message.answer(text)


@dp.message_handler(text='Piskent')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Piskent_tumani.png/300px-Piskent_tumani.png')
    text = """Piskent tumani - Toshkent viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Shimoliy va shim.-sharqsan Ohangaron va Oʻrta Chirchiq, gʻarbdan Oqqoʻrgʻon, jan.-gʻarbdan Boʻka tumanlari, jan.dan Tojikiston Respubli-kasining Sugʻd viloyati bilan chegaradosh. Maydoni 0,79 ming km². Aholisi 86,3 ming kishi (2003). Piskent tumanida 1 shahar (Piskent), 6 qishloq fuqarolari yigʻini (Doʻngqoʻrgʻon, Kerovchi, Murotali, Koriz, Oqtepa, Sayd) bor. Tuman markazi — Piskent shahri"""
    await message.answer(text)


@dp.message_handler(text='Chortoq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Chortoq_tumani.png/1280px-Chortoq_tumani.png')
    text = """Chortoq — Namangan viloyatidagi tuman. 1950-yil 15-aprelda tashkil etilgan. Gʻarbdan Yangiqoʻrgʻon, janubiy, janubi-sharqdan Uychi tumanlari, shimoliy va sharqda Qirgʻiziston Respublikasi bilan chegaradosh. Maydoni 0,36 ming km2. Aholisi 199.8 ming kishi (2020). Tumanda 1 shahar (Chortoq), 9 qishloq fuqarolari yigʻini (Alixon, Bogʻiston, Gulshan, Koroskon, Muchum, Oyqiron, Peshqoʻrgʻon, Saroy, Hazratishoh) bor. Markazi Chortoq shahri"""
    await message.answer(text)


@dp.message_handler(text='Norin')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Norin_tumani.png/1280px-Norin_tumani.png')
    text = """Norin tumani — Namangan viloyatining janubi-sharqiy qismida joylashgan tuman. 1926-yil 29-sentabrda tashkil etilgan. 1962—1973-yillarda va 1988—89 yillarda Uchqoʻrgʻon tumani tarkibida boʻlgan. Norin tumani (Oʻzbekiston) gʻarbdan viloyatning Namangan va Uychi, shimolidan Uchqoʻrgʻon tumanlari, janubiy va sharqdan Andijon viloyatining Baliqchi va Izboskan tumanlari bilan chegaradosh. Maydoni 207,1 km². Axrlisi 158,3 ming kishi (2019). Norin tumani (Oʻzbekiston)da 1 shahar (Haqqulobod) va 57 ta mahalla fuqarolar yigʻinidan tashkil topgan(2020). Markazi — Haqqulobod shahri Tabiati. Norin tumani (Oʻzbekiston) viloyatning sharqiy qismida, Fargʻona tizmasining etaklarida joylashgan, gʻarbiy chegaralari boʻylab Qoradaryo oʻtadi. Relyefi past-baland tekislikdan iborat (balandligi 600– 800 m). Togʻ etaklari paleogen davrining gil, ohaktosh, mergel jinslaridan tarkib topgan. Norin havzasi yoppasiga konglomeratdan iborat. Qo-radaryo havzasida konglomerat ustupi oʻnlab metr qalinlikda qoplab yotgan lyoss katta maydonda tekislik hosil qilgan. Norinning qayir tekisligi Uchqoʻrgʻon qishlogʻidan boshlab 2–3 km ga kengayadi; bu yerda qumoq hamda qum-loq jinslar keng tarqalgan"""
    await message.answer(text)


@dp.message_handler(text='Uchqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Uchqorg%27on_tumani.png/300px-Uchqorg%27on_tumani.png')
    text = """Uchqoʻrgʻon tumani (maʼnosi: Uchta qoʻrgʻon) — Namangan viloyatining shimoli-sharqiy qismida joylashgan va Norin daryosi bilan qoʻshni Qirgʻiziston Respublikasi bilan chegaradosh tuman hisoblanadi. Uchqoʻrgʻon tumanining markazi — Uchqoʻrgʻon shahridir. Tarixi Uchqoʻrgʻon tumani — 1935-yil 28-iyul oyida tashkil etiladi va Namangan viloyatiga qarashli tuman deb eʼlon qilinadi. 1988-1989-yillarda esa Norin tumani bilan birlashadi. 1940-yilgacha Fargʻona viloyati, 1941-yil 6-martdan Namangan viloyati, 1960-yildan 1967-yilgacha Andijon viloyati 1968-yildan esa yana Namangan viloyati tarkibiga qaytadi."""
    await message.answer(text)


@dp.message_handler(text='Chust')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chust_tumani.png/300px-Chust_tumani.png')
    text = """Chust tumani — Namangan viloyatidagi tuman. 1926-yil 29- sentabrda tashkil etilgan. Sharqdan Toʻraqoʻrgʻon, shimoli-sharqdan Kosonsoy, janub va gʻarbdan Pop, janubi-sharqdan Mingbuloq tumanlari, shimoldan Qirgʻiziston Respublikasi bilan chegaradosh. Maydoni 0,92 ming km². Aholisi 198,9 ming kishi (2004). Tumanda 1 shahar (Chust), 11 qishloq fuqarolari yigʻini (Axcha, Boymoq, Varziq, Karkidon, Karnon, Olmos, Ogʻasaroy, Shoyon, Shoʻrkent, Gʻova, Hisorak) bor. Markazi — Chust shahri."""
    await message.answer(text)


@dp.message_handler(text='Pop')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Pop_tumani.png/300px-Pop_tumani.png')
    text = """Pop tumani — Namangan viloyatidagi tuman. 1926-yil 28-sentabrda tashkil etilgan. 1930-yildan Chust-Pop tumani nomi bilan atalgan. 1931-yilda, Chust tumani ajralib chiqqanidan keyin, Pop tumani deb atalib kelinmoqda. 1947—60 yillarda Namangan viloyati tarkibida, 1960—67 yillarda Fargona viloyatida, 1967-yil dekabrdan yana Namangan viloyati tarkibida."""
    await message.answer(text)


@dp.message_handler(text='Uychi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Uychi_tumani.png/1280px-Uychi_tumani.png')
    text = """Uychi tumani 1935-yil iyun oyida tashkil topgan. Tumanning umumiy maydoni 309,8 kv km. Aholisi 184 ming 47 nafar. Tuman markazi Uychi shaharchasi boʻlib, u Namangan-Uchqoʻrgʻon avtomagistral yoʻlida joylashgan.
Tabiati. Relyefi, asosan, tekislik. Shimoli-sharqiy qismi adirlardan iborat. Iklimi kontinental. Yanvarning oʻrtacha harorati — 2,3°, eng past temperatura — 26°. Iyul oyining oʻrtacha temperaturasi 26,3°, eng yuqori temperatura 42°. Yillik yogʻin 188 mm, vegetatsiya davri 280—290 kun. Tuman hududidan Norin daryosi, Shimoliy Fargʻona va Katta Namangan kanallari oqib oʻtadi. Tuproklari, asosan, och tusli boʻz va allyuvial tuproqlar. Yovvoyi oʻsimliklardan qamish, ajriq, pechak, shoʻra, adirlarda shuvoq oʻsadi. Qushlardan qaldirgʻoch, bulbul, bedana, gʻurrak, qargʻa, sassiqpopishak; sudraluvchilardan kaltakesak, toshbaqa, ilon, kemiruvchilardan yumronqoziq, kalamush, sichqon va boshqa bor."""
    await message.answer(text)


@dp.message_handler(text='Kosonsoy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Kosonsoy_tumani.png/300px-Kosonsoy_tumani.png')
    text = """Kosonsoy tumani - Namangan viloyatidagi tuman. 1926-yil 29-sentabrda tashqil etilgan. 1962-yil 24-dekabrda Chust tumani bilan birlashtirilgan. 1973-yil 28-dekabrda yana qaytadan tuzilgan. Kosonsoy tumani viloyatning shimoliy qismida, Qoratogʻ etaqlarida, oʻrtacha 790 m balandlikda joylashgan. Janubidan Namangan shahri, sharqdan viloyatning Yangiqoʻrgʻon, janubi-gʻarbdan Chust tumanlari, shimoliy va gʻarbdan Qirgʻiziston Respublikasi bilan chegaradosh. Maydoni 0,51 ming km². Aholisi 141,5 ming kishi (2002). Tumanda 1 shahar (Kosonsoy), 7 qishloq fuqarolar yigʻini (Yoshlik, Koson, Tergachi, Chinovul, Shirin, Qorasuv, Koʻkumboy) bor. Markazi — Kosonsoy shahri"""
    await message.answer(text)


@dp.message_handler(text='Toʻraqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/To%27raqo%27rg%27on_tumani.png/1280px-To%27raqo%27rg%27on_tumani.png')
    text = """Toʻraqoʻrgʻon tumani - Namangan viloyatidagi tuman. Viloyatning gʻarbida joylashgan. 1936-yil 17-fevralda tashkil etilgan. 1962-yil 24-dekabrda Namangan tumani bn birlashtirilgan[1]. 1970-yil 7-dekabrda qayta tuzildi. Sharqdan Namangan tumani va qismanNamangan shahri, janubdanMingbuloq, gʻarbdanChust, shimoldan Kosonsoy tumanlari bilan chegaradosh. Maydoni 0,33 ming km2. Aholisi 193 ming kishi (2011). Toʻraqoʻrgʻon tumanida 1 shahar (Toʻraqoʻrgʻon), 1 shaharcha (Oqtosh), 8 qishloq fuqarolari yigʻini (Axsi, Buramatut, Yortepa, Qatagʻonsaroy, Sayram, Xolmatov, Xoʻjand,Shahand) bor. Markazi — Toʻraqoʻrgʻon shahri."""
    await message.answer(text)


@dp.message_handler(text='Yangiqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Yangiqo%27rg%27on_tumani.png/300px-Yangiqo%27rg%27on_tumani.png')
    text = """Yangiqoʻrgʻon tumani — Namangan viloyatidagi tuman. 1926 yil 29 sentyabr da tashkil etilgan. Gʻarbdan Kosonsoy, janubidan Namangan va Uychi tumanlari, shimoliy gʻarb, shimoliy va sharqda Qirgʻiziston Respublikasi, Chortoq tumani bilan chegaradosh. Maydon 0,54 ming km². Aholisi 166,7 ming kishidan ziyod (2005). Tumanda 1 shaharcha (Yangiqoʻrgʻon), 11 qishloq fuqarolari yigʻini (Bekobod, Birlashgan, Zarbdor, Zarkent, Istiqlol, Navkent, Navroʻzobod, Nanay, Paromon, Sharq Yulduzi, Qorapolvon) bor. Markazi — Yangiqoʻrgʻon shaharchasi. Tuman aholisi 149,6 ming nafarni tashkil etib, Namangan shahar aholisining 23,8 foizini qamrab oladi. Mazkur hudud istiqbolda zamonaviy ko‘p qavatli uylar qurilishi hisobiga urbanizatsiya jarayoni jadallashishiga, shuningdek, yangi infratuzilma obyektlari barpo etilishi va aholiga xizmat ko‘rsatish tizimi yanada rivojlanishiga xizmat qilishi kutilmoqda.  """
    await message.answer(text)


@dp.message_handler(text='Davlatobod')
async def echo(message: types.Message):
    text = """Namangan shahri tarkibida yangidan tashkil etilgan tuman hududida 25 ta mahalla fuqarolari yig‘ini, 33850 ta xonadon, 421 ta ko‘p qavatli uy, 3 ta kasb-hunar kolleji, 18 ta umumta’lim maktabi, 24 ta maktabgacha ta’lim muassasasi, 5 ta tibbiyot muassasasi, 1280 gektar qishloq xo‘jaligi yerlari, 698 ta xizmat ko‘rsatish ob’ekti, 429 ta sanoat korxonasi hamda 2 ta madaniy meros obyekti mavjud."""
    await message.answer(text)


@dp.message_handler(text='Mingbuloq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Mingbuloq_tumani.png/300px-Mingbuloq_tumani.png')
    text = """Mingbuloq tumani (1994-yilgacha Zadaryo tumani) — Namangan viloyatidagi tuman. Markazi Jomashoʻy shaharchasi. Ushbu tuman 1952-yil 29-sentabrda tashkil etilgan. Sirdaryoning chap sohilida, Markaziy Fargʻonaning qoʻriq va boʻz yerlarida. Shimolidan viloyatning Chust va Toʻraqurgʻon, Shimoli-sharqdan Namangan, shimoli-gʻarbdan Pop tumanlari, janubi-sharqdan Andijon viloyatining Ulugʻnor, janubiy va janubi-gʻarbdan Fargʻona viloyati tumanlari bilan chegaradosh. Maydoni 0,74 ming km². Aholisi 91,6 ming kishi (2002). Tumanda 1 shaharcha (Jomashoʻy), 7 qishloq fuqarolar yigʻini (Boʻston, Gulbogʻ, Goʻrtepa, Dovduq, Oltinkoʻl, Mehnatobod, Momoxon) bor. Tuman markazi Jomashuy shaharchasi. 2018-yilda tumanda "MINGBULOQ" nomli telegram kanal ish boshlagan. Hozirda ushbu kanalda tumanga oid yangiliklar, dolzarb xabarlar, tanqidiy maqolalar va aholi murojaatlari berib boriladi"""
    await message.answer(text)


@dp.message_handler(text='Namangan')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Namangan_tumani.png/300px-Namangan_tumani.png')
    text = """Namangan tumani — Namangan viloyatidat tuman. 1926-yil 29-sentabrda tashkil etilgan. Sharqdan Uychi, Norin, shimoldan Kosonsoy, Yangiqoʻrgʻon, Chortoq, gʻarbdan Toʻraqoʻrgʻon, janubdan Mingbuloq, Andijon viloyatining Baliqchi tumanlari bilan chegaradosh. Maydoni 0,25 ming km². Aholisi 170,9 ming kishiga yaqin (2003). Namangan tumanida 1 shaharcha (Toshbuloq), 12 qishloq fuqarolari yigʻini (Bogʻishamol, Ibrohim Rahmatov, Irvadon, Mirishkor, Oxunboboyev, Tepaqoʻrgʻon, Xonobod, Shoʻrqishloq, Oʻzbekistan, Qumqoʻrgʻon, Gʻalcha, Gʻirvon) bor (2003). Markazi — Toshbuloq shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Asaka')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Asaka_tumani.png/1280px-Asaka_tumani.png')
    text = """Asaka tumani – Andijon viloyatidagi tuman. Viloyatning markaziy qismida joylashgan. 1926-yil 29-sentabrda tashkil etilgan (1962-yil 24-dekabrda Marhamat tumani bilan birlashtirilgan, 1970-yil 7-dekabrda qayta tuzilgan). Andijon viloyatining Shahrixon, Marhamat, Andijon, Xoʻjaobod tumanlari va Fargʻona viloyatining Quva tumani bilan chegaradosh. Maydoni 0,26 ming km² (1995). Aholisi 174,9 ming kishi (2000). Asaka tumanida 1 shahar (Asaka) va 8 qishloq yigʻini (Zarbdor, Ilgʻor, Kujgan, Mustahkam, Niyozbotir, Oʻzbekiston, Qadim, Qoratepa) bor. Markazi – Asaka shahri"""
    await message.answer(text)


@dp.message_handler(text='Boʻston')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Location_of_Bo%E2%80%99z_District_in_Andijon_Province.png/300px-Location_of_Bo%E2%80%99z_District_in_Andijon_Province.png')
    text = """Boʻz tumani — (1950-2019 yillarda — Boʻz tumani) Andijon viloyatidagi tuman. 1950-yil 5-aprelda tashkil etilgan. 1962-yil 24-dekabrda Shahrixon tumaniga qoʻshib yuborilgan. 1964-yil 31-dekabrda qayta tuzilgan. 2019-yil 30-sentyabrda tuman nomi Boʻston tumani deb oʻzgartirilgan[2]Boʻz tumani shimol, shimoli-gʻarbda viloyatning Ulugʻnor tumani, shimolda Baliqchi tumani, sharqda Shahrixon tumani, janubi-gʻarbda Fargʻona viloyatining Yozyovon, janubda Qoʻshtepa tumani, janubi-sharqda Quva tumani bilan chegaradosh. Maydoni — 0,20 ming km2. Aholisi — 54 mingdan ziyod kishi. Boʻz tumanida 1 shaharcha (Boʻz) va 3 ta qishloq fuqarolar yigʻini (Mannop Jalolov, Xovos, Xoldеvonbеk) bor. Markazi — Boʻz shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Buloqboshi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Location_of_Bo%E2%80%99z_District_in_Andijon_Province.png/300px-Location_of_Bo%E2%80%99z_District_in_Andijon_Province.png')
    text = """Buloqboshi tumani — Andijon viloyatidagi tuman. Viloyatning janubida 1992-yil 3-aprelda tashkil etilgan. Buloqboshi tumani shimoliy va sharqda Andijon va Xoʻjaobod tumanlari, gʻarbda Asaka va Marhamat tumanlari, janubida va janubi-gʻarbda Qirgʻiziston Respublikasining Oʻsh viloyati Aravon tumani bilan chegaradosh. Maydoni 0,18 ming km2. Aholisi 110 ming kishi (2010). Markazi — Buloqboshi shahri"""
    await message.answer(text)


@dp.message_handler(text='Andijon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Location_of_Andijon_District_in_Andijon_Province.png/300px-Location_of_Andijon_District_in_Andijon_Province.png')
    text = """Andijon tumani – Andijon viloyatidagi tuman, viloyatning markazida joylashgan. 1926-yil 29-sentabrda tashkil etilgan. Viloyatning Jalaquduq, Xoʻjaobod, Asaka, Oltinkoʻl, Baliqchi, Izboskan va Paxtaobod tumanlari bilan chegaradosh. Maydoni – 0,4 ming kv. km. Aholisi – 198,4 ming kishi. Maʼmuriy markazi – Kuyganyor shaharchasi. Andijon tumani – Andijon viloyati markaziy qismida joylashgan tuman. 1926-yil 29-sentabrda tashkil etilgan. Jalaquduq, Xoʻjaobod, Asaka, Oltinkoʻl, Baliqchi, Izboskan va Paxtaobod tumanlari bilan chegaradosh. Maydoni 0,38 ming km². Aholisi 177,3 ming kishi (2000). Andijon (tuman)da 1 shaharcha (Kuyganyor) va 9 qishloq fuqarolari yigʻini (Boʻtaqora, Yorboshi, Kunji, Nayman, Orol, Oqyor, Xaqan, Hartum, Harabek) bor (2000). Markazi – Kuyganyor shaharchasi.Tabiati. Andijon (tuman) relefi pasttekislik, qir va adirlardan iborat. Shimoli-sharqida Andijon – Otchopar, Teshiktosh adirlari va Harabek, Boʻtaqora, Yorboshi kirlari mavjud"""
    await message.answer(text)


@dp.message_handler(text='Izboskan')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/9/9f/Izboskan_tumani.png')
    text = """Izboskan tumani - Andijon viloyatidagi tuman; viloyatning shimolida joylashgan. 1926-yilning 29-sentabrida tashkil etilgan. Maʼmuriy markazi - Poytugʻ shahri. Andijon viloyatining Paxtaobod, Andijon, Baliqchi, Oltinkoʻl tumanlari, Naman­gan viloyati, Qirgʻiziston Rеspubli­kasi bilan chеgaradosh. Maydoni 0,28 ming kvadrat kilometr.
Izboskan tumanida 1ta shahar (Poytug) va 9ta qishloq fuqarolari yigʻini bor."""
    await message.answer(text)


@dp.message_handler(text='Jalaquduq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Jalolquduq_tumani.png/1280px-Jalolquduq_tumani.png')
    text = """Jalaquduq — Andijon viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan (1962-yil 24-dekabrda Xoʻjaobod tumani bilan birlashtirilgan. 1973-yil 12-aprelda qayta tuzildi).
Tuman viloyatning Qoʻrgʻontepa, Xoʻjaobod, Andijon tumanlari hamda Qirgʻiziston Respublikasi bilan chegaradosh. Maydoni — 0,37ming kv. km. Aholisi — 146,5 ming kishi.
Jalaquduq tumanida 1ta shahar (Jalaquduq), 2ta shaharcha (Janubiy Olamushuk, Qo'shtepa ) 8ta qishloq fuqarolar yigʻini (Abdullabiy, Beshtol, Yorqishloq, Jalaquduq, Kolxozqishloq, Oyim, Teshiktosh, Qatortol) bor. Markazi — Oxunboboyev shahri."""
    await message.answer(text)


@dp.message_handler(text='Marhamat')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Marhamat_tumani.png/300px-Marhamat_tumani.png')
    text = """Marhamat tumani - Andijon viloyatidagi tuman, viloyatning janubiy qismida joylashgan. 1926-yil 29-sentabrda tashkil etilgan. 1963-yilda Marhamat tumani yondosh tuman bilan birlashtirilib tuman markazi Marhamat tumanidagi Russkoye selo posyolkasiga koʻchirilgan. 1965-yil 15-fevralda tuman nomi oʻzgartirilib tuman markazi hozirgi Asaka shahriga ko'chirilgan. 1970-yil 7 - dekabrda Marhamat tumani nomi bilan qayta tashkil etilgan. Marhamat tumani shimolda viloyatning Asaka, Buloqboshi tumanlari, sharq va janubda Qirgʻiziston Respublikasi Oʻsh viloyatining Aravon tumani, gʻarbda Fargʻona viloyatining Quva tumani bilan chegaradosh. Maydoni 0,32 ming km², aholisi 175,7 ming kishi (2020). Marhamat tumanida 1 shahar (Marhamat), 1 shaharcha (Polvontosh), 5 qishloq fuqarolari yigʻini (Marhamat, Qorabogʻish, Shukurmergan, Qoraqoʻrgʻon, Koʻtarma, Mirishkor) bor. Markazi — Marhamat shahri"""
    await message.answer(text)


@dp.message_handler(text='Oltinkoʻl')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/5/50/Oltinko%27l_tumani.png')
    text = """Oltinkoʻl tumani - Andijon viloyatidagi tuman. 1939-yilda tashkil etilgan. Maʼmuriy markazi - Oltinkoʻl (qilshloq). Andijon viloyatidagi Oltinkoʻl tumani 1939-yilda tashkil etilgan. 1963-yilda viloyatning Andijon tumaniga qoʻshib yuborilgan. 1978-yilda qaytadan tashkil etilgan. Oltinkoʻl tumani Andijon viloyatining Andijon, Asaka, Shahrixon va Baliqchi tumanlari bilan chegaradosh"""
    await message.answer(text)


@dp.message_handler(text='Paxtaobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Paxtaobod_tumani.png/300px-Paxtaobod_tumani.png')
    text = """Paxtaobod tumani Andijon viloyatining shimoliy sharqida joylashgan. Paxtaobod tumani viloyat markazi Andijon shahridan 24 km shimoliy-sharqda boʻlib dengiz sathidan 300 metr balandlikda joylashgan. Iqlimi moʻtadil. Aholisi 165 ming kishi (2009-yil). Paxtaobod tumanini Qoradaryo, Tentaksoy, Chirtaksoy daryolari kesib oʻtadi. Tuman markaziga 1975-yilda Pahtaobod shahri maqomi berilgan. Umumiy er maydoni 26 ming 33 gektar."""
    await message.answer(text)


@dp.message_handler(text='Shahrixon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Shahrixon_tumani.png/300px-Shahrixon_tumani.png')
    text = """Shahrixon tumani - Andijon viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Gʻarbdan Boʻz, shim.dan Baliqchi, Oltinkoʻl, sharqdan Asaka, jandan Fargʻona viloyatining Quva tumanlari bilan chegaradosh. Maydoni 0,33 ming km². Aholisi 215,3 ming kishi (2004). Tumanda 1 shahar (Shahrixon), 12 qishloq fuqarolari yigʻini (Abdubiy, Guliston, Nazarmahram, Naynavo, Paxtaobod, Toshtepa, Choʻja, Yuqori Shahrixon, Yangiyoʻl, Oʻzbekiston, Oʻrta Shahrixon, Haqiqat) bor. Markazi — Shahrixon shahri."""
    await message.answer(text)


@dp.message_handler(text='Ulugʻnor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Ulug%27nor_tumani.png/1280px-Ulug%27nor_tumani.png')
    text = """Ulugʻnor — Andijon viloyatidagi tuman. 1973-yil 26-dekabrda tashkil etilgan. Shimoldan Baliqchi, janubi-sharqdan Boʻz, gʻarb va shimoli-gʻarbdan Namangan viloyatining Namangan, Mingbuloq tumanlari, janubdan Fargʻona viloyati bilan chegaradosh. Tuman markazi — Oqoltin qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Xoʻjaobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Xo%27jaobod_tumani.png/300px-Xo%27jaobod_tumani.png')
    text = """Xoʻjaobod tumani — Andijon viloyatidati tuman. 1926-yil 29-sentyabrda tashkil topgan. 1973-yilda tuman tarkibidan Jalaquduq tumani, 1992-yilda Buloqboshi tumani ajralib chiqqan. Xoʻjaobod tumani shimoliy-sharqdan Jalaquduq, shimoliy-gʻarbdan Andijon, gʻarbdan Buloqboshi tumanlari, sharq, janub va janubiy-gʻarbdan Qirgʻiziston bilan chegaroadosh. Maydoni 0,23 ming km². Aholisi 82,1 ming kishidan ziyod (2004). Tumanda 4 kishloq fuqarolari yigʻini (Birlashgan, Manak, Oltin Vodiy, Xoʻjaobod), 1 shahar (Xoʻjaobod) bor. Markazi — Xoʻjaobod shahri."""
    await message.answer(text)


@dp.message_handler(text='Sirdaryo')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Sirdaryo_tumani.png/1280px-Sirdaryo_tumani.png')
    text = """Sirdaryo tumani — Sirdaryo viloyatidagi tuman. 1939-yil 10 fevralda tashkil etilgan. Shim.sharkdan Toshkent viloyati, jan.sharkdan Sayxunobod, janubidan Guliston tumanlari, gʻarbdan Qozogʻiston Respublikasi bilan chegaradosh. Maydoni 0,55 ming km². Aholisi 110,5 ming kishi (2003). Tumanda 2 shahar (Sirdaryo, Baxt), 4 shahrcha (Ziyokor (Sirdaryo tumani), Quyosh (Sirdaryo tumani), Malik (Sirdaryo tumani), J. Mamanov), 8 qishloq fuqarolari yigʻini (Paxtazor, Sirdaryo, Turon, Usmon Yusupov, Xalqobod, Choltoʻqay, Sholikor, Haqiqat) bor. Markazi — Sirdaryo shahri."""
    await message.answer(text)


@dp.message_handler(text='Guliston')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Guliston_tumani.png/300px-Guliston_tumani.png')
    text = """Guliston tumani - Sirdaryo viloyatidagi tuman. 1952 yil 16 aprelda tashkil etilgan. Viloyatning Sirdaryo, Boyovut, Sayxunobod, Mirzaobod, Sharof Rashidov tumanlari, Toshkent viloyatining Bekobod tumani bilan chegaradosh. Maydon 0,35 ming km2. Aholisi 50,1 ming kishi (2000). Guliston tumanida 1 shaharcha (Dehqonobod), 9 qishloq fuqarolari yigʻini (Beshbuloq, Zarbdor, Koʻnchi, Oltintepa, Oltin Oʻrda, Soibobod, Sohilobod, Chortoq, Humo) bor. Markazi — Dehqonobod shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Boyovut')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Boyovut_tumani.png/1280px-Boyovut_tumani.png')
    text = """Boyovut tumani — Sirdaryo viloyatidagi tuman. 1955-yil 19-aprelda Toshkent viloyati tarkibida tashkil etilgan. 1960-yilda Yangiyer tumaniga qoʻshilgan. 1963-yil Sirdaryo viloyati tarkibida qayta tashkil etildi. Boyovut tumani Sirdaryo viloyatining sharqida joylashgan. Sharqda Toshkent viloyatining Bekobod tumani, jan.gʻarbda Xovos tumani, shim.da Guliston tumani, g'arbda Mirzaobod tumani va jan.da Tojikiston Respublikasi bilan chegaradosh. Maydoni 0,435 ming km². Aholisi 80,2 ming kishi (1999). Boyovut tumani da 1 shahar (Boyovut) va I qishloq fuqarolari yigʻini (Boyovut, Dehqonobod, Darvozaqir, Doʻstlik, Laylakkoʻl, Madaniyat, Mingchinor, Olmazor(shaharcha), Tinchlik, Usmonobod, Gʻallakor) bor. Markazi — Boyovut shahar"""
    await message.answer(text)


@dp.message_handler(text='Xovos')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Xovos_tumani.png/300px-Xovos_tumani.png')
    text = """Xovos tumani — Sirdaryo viloyatidagi tuman. 1926-yil dekabrda tashkil qilingan. 1955-yildan 1966-yilgacha Boyovut tumani, 1966-yil 25 avgustdan 1975-yil 6 martgacha Yangiyer tumani deb atalgan. 2004-yil 11 maydan Xovos tumaniga Mehnatobod tumani qoʻshildi. Tuman markazi Farhod 5 qishlogʻidan Xovos shaharchasiga koʻchirildi. Shim.sharqdan Boyovut, janubiy sharqdan Toshkent viloyatining Bekobod tumani, januniy da Tojikiston Respublikasi, gʻarbdan Jizzax viloyatining Zomin, shim.gʻarbdan viloyatning Sardoba, Mirzaobod tumanlari bilan chegaradosh. Maydoni 621 km². Aholisi 74,1 ming kishidan ziyod (2004). Tumanda 1 shaharcha (Xovos), 11 qishloq fuqarolari yigʻini (Binokor, Gulbahor, Zafarobod, Paxtakor, Sohibkor, Chamanzor, Qaxramon, Turkiston, Farhod, Havotag , Husnobod) bor. Markazi — Xovos shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Sayxunobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Sayhunobod_tumani.png/1280px-Sayhunobod_tumani.png')
    text = """'Sayxunobod tumani' - Sirdaryo viloyatidagi tuman. 1952 y Verxnevolinskoye tumani nomi bilan tashkil qilingan. 1959 y Sirdaryo va Guliston tumanlari tarkibiga qoʻshilgan. 1970 y 7-dekabrda Voroshilov tumani nomi bilan qayta tashkil etildi. 1984-yildan Sayxunobod nomi bilan yuritiladi. Shimolda Toshkent viloyatining Quyi Chirchiq, Oqqoʻrgʻon, sharqda Boʻka tumanlari, shimoliy gʻarb va gʻarbda viloyatning Sirdaryo, januba Guliston tumanlari bilan chegaradosh. Maydoni 0,55 ming km². Axoli 61,9 ming kishi (2003). Tumanda 1 shaharcha (Sayxun), 7 qishloq fuqarolari yigʻini (Guliston, Istiqlol, Ittifoq, Nurota, Shoʻrazak, Yangihayot, Oʻzbekiston) bor. Tuman markazi — Sayxun shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Oqoltin')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Oqoltin_tumani.png/1280px-Oqoltin_tumani.png')
    text = """Oqoltin tumani - Sirdaryo viloyatidagi tuman. 1971-yil 29 avgustda tashkil etilgan. Shim.dan Krzogʻiston Respublikasi, shim.-gʻarbdan Jizzax viloyatining Mirzachoʻl, jan.-gʻarbdan Doʻstlik tumanlari, jan.dan viloyatning Sharof Rashidov, shim.-sharq, jan.-sharkdan Mirzaobod va Mehnatobod tumanlari bilan chegaradosh. Maydoni 0,57 ming km². Aholisi 51,3 ming kishi (2003).[1]
Oqoltin tumanida 6 qishloq fuqarolar yigʻini (Andijon, Boʻston, Sardoba, Fargʻona, Shodlik, Gʻalaba) bor (2003). Markazi — Sardoba qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Mirzaobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Mirzaobod_tumani.png/1280px-Mirzaobod_tumani.png')
    text = """Mirzaobod tumani - Sirdaryo viloyatidagi tuman. 1988-yil 2-sentabrda tashkil etilgan. Dastlab Komsomol, 1992-yil 22 oktabrdan Mirzaobod deb nomlangan. Viloyatning Sirdaryo, Guliston, Sayxunobod, Boyovut, Mehnat-obod, Sharof Rashidov va Oqoltin tumanlari hamda bir qismi Qozogʻiston bilan chegaradosh. Maydoni 0,44 ming km². Aholisi 41,5 ming kishi (2000). Mirzaobod tumanida 7 qishloq fuqarolari yigʻini (Birlashgan, Mehnatobod, Mirzachoʻl, Navbahor, Nurafshon, Oqoltin, Toshkent) bor. Markazi Navroʻz qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Arnasoy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Arnasoy_tumani.png/1280px-Arnasoy_tumani.png')
    text = """Arnasoy tumani – Jizzax viloyatidagi tuman, 1975-yil 26-noyabrda tashkil etilgan. Shimoliy va shimoli-gʻarbda Forish, janubida Zafarobod, janubi-sharqda Paxtakor, sharqda Doʻstlik, shimoli-sharqda Mirzachoʻl tumanlari bilan chegaradosh. Maydoni 0,49 ming km². Aholisi 40,0 mingdan ortiq kishi (1999). Arnasoy tumanida 6 Qishloq fuqarolari yigʻini (Doʻstlik, Zarafshon, Usmon Yusupov, Choʻlquvar, Yangiboʻston, Gʻalaba) bor. Markazi – Gʻoliblar"""
    await message.answer(text)


@dp.message_handler(text='Baxmal')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/uz/thumb/e/e1/Baxmal_tumani.png/300px-Baxmal_tumani.png')
    text = """Baxmal tumani, Oʻzbekistonning Jizzax viloyatidagi tuman. 1943-yil 8-mayda tashkil etilgan (1957-yil 12-oktabrda Gʻallaorol tu-mani bilan birlashtirilgan edi, 1971-yil 31-avgustda qayta tuzildi). Baxmal tumani Gʻallaorol, Zomin tumanlari, Samarqand viloyati va Tojikiston Respublikasi bilan chegaradosh. Maydoni 1,86 ming km². Aholisi 112,500 ming kishi.[manba kerak] Baxmal tumanida 1 shaharcha (Usmat) va 11 qishloq fuqarolari yigʻini (Barlos, Baxmal, Bogʻishamol, Gulbuloq, Mugʻol, Novqa, Oyqor, Oqtosh, Sangzor, Tongotar, Uzunbulok) bor. Markazi — Usmat shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Doʻstlik')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Do%27stlik_tumani.png/300px-Do%27stlik_tumani.png')
    text = """Doʻstlik tumani — Jizzax viloyatidagi tuman. 1970-yil 16-oktabrda tashkil etilgan. Doʻstlik tumani viloyatning Arnasoy, Mirzachoʻl, Paxtakor, Sirdaryo viloyatining Oq oltin tumanlari bilan chegaradosh. Mayd. 0,45 ming km2. Aholisi 67 ming kishi (2022). Doʻstlik tumanida 1 shahar (Doʻstlik) va 12 ta mahalla fuqarolari yigʻini (Chinobod, Alisher Navoiy, Gʻafur Gʻulom, Sanoatchilar, Bogʻzor, Bunyodkor, Manas, Mevazor, Navroʻz, Saritepa, Oltin vodiy, Qahramon) mavjud.[manba kerak] Markazi — Doʻstlik shahri."""
    await message.answer(text)


@dp.message_handler(text='Forish')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Forish_tumani.png/1280px-Forish_tumani.png')
    text = """Forish tumani — Jizzax viloyatidagi tuman. 1935-yil 9-fevralda tashkil etilgan. 1962-yilda Nurota va Jizzax tumanlari tarkibiga qoʻshib yuborilgan. 1964-yilda qayta tashkil etilgan. Forish tumani dastlab Samarqand, 1964-yil Sirdaryo, 1974-yil Jizzax viloyatlari tarkibiga kiritilgan. Shimoliy va shimoli-sharqdan Qozogʻiston, sharqdan Jizzax, Zafarobod, Arnasoy, Doʻstlik, Mirzachoʻl tumanlari, janubidan Gʻallaorol tumani, gʻarbdan Samarkand, Navoiy viloyatlarining Qoʻshrabot, Nurota tumanlari bilan chegaradosh. Maydoni 9,53 ming km². Aholisi 93,500 kishi (2020)."""
    await message.answer(text)


@dp.message_handler(text='Gʻallaorol')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/G%27allaorol_tumani.png/1280px-G%27allaorol_tumani.png')
    text = """Gʻallaorol tumani – Jizzax viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. 1931-yilgacha Yangiqoʻrgʻon tumani deb atalgan. Viloyatning gʻarbiy, janubi-gʻarbiy qismida joylashgan. Shimolidan Forish, sharqdan Jizzax, janubidan Baxmal tumanlari, janubi-gʻarb va gʻarbdan Samarqand viloyati bilan chegaradosh. Maydoni 2,0 ming km². Aholisi 128,1 ming kishi (2005). 1 shahar (Gʻallaorol), 2 shaharcha (Mar-jonbuloq, Qoʻytosh), 11 qishloq fu-qarolari yigʻini ( 1-may qishlogʻi ya'ni Gʻallakor Buloqboshi, Guliston, Ittifoq, Koʻkbuloq, Madaniyat, Mirzabuloq, Moʻltob, Mulkush, tozaurugʻ, Qipchoqsoy, Gʻoʻbdin) bor. Markazi – Gʻallaorol shahri."""
    await message.answer(text)


@dp.message_handler(text='Sharof Rashidov')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Jizzax_tumani.png/300px-Jizzax_tumani.png')
    text = """Sharof Rashidov tumani (Sobiq nomi Jizzax tumani) — Jizzax viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Shim.da viloyatning Forish, Zafarobod, Paxtakor tumanlari, gʻarbda Gʻallaorol tumani, sharqda Zarbdor, Zomin tumanlari, janubida Baxmal tumani bilan chegaradosh. Mayd. 1,44 ming km2. Aholisi 142,3 ming kishi (2001). J. t.da 13 qishloq fuqarolari yigʻini (Gandumtosh, Ittifoq, Oxunboboyev, Oqoltin, Paxtaobod, Ravot, Samarqandquduq, Tokchilik, Uchtepa, Xayrobod, Qulama, Qoʻshbarmoq, Hamzaobod) bor. Markazi — Uchtepa qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Mirzachoʻl')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Mirzacho%27l_tumani.png/1280px-Mirzacho%27l_tumani.png')
    text = """Mirzachoʻl tumani - Jizzax viloyatidagi tuman. 1967-yil 9-yanvarda tashkil etilgan. Shim.dan Qozogʻiston, shimoli-sharqdan Sirdaryo viloyati, janubiy dan Jizzax viloyatining Doʻstlik, gʻarbdan Forish, Arnasoy tumanlari bilan chegaradosh. Maydoni 0,42 ming km². Aholisi 52 ming 400 kishi (2020). Mirzachoʻl tumanida 1 shahar (Gagarin), 8 qishloq fuqarolari yigʻini (Bogʻbon, Ipakyoʻli, Mirzadala, Paxtazor, Toshkent, Yangidala, Oʻzbekiston, Gulzor) bor. Markazi Gagarin shahri"""
    await message.answer(text)


@dp.message_handler(text='Paxtakor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Paxtakor_tumani.png/300px-Paxtakor_tumani.png')
    text = """Paxtakor tumani - Jizzax viloyati tarkibidagi tuman. 1967-yil 9-yanvarda Mirzachoʻl janubi-gʻarbidagi oʻzlashtirilgan yerlar negizida Sirdaryo viloyati tarkibida tashkil etilgan. 1974-yil Jizzax viloyati tashkil etilishi munosabati bilan ushbu viloyat tarkibiga oʻtkazilgan. Gʻarbda Zafaro-bod va Arnasoy, shimolida Doʻstlik, sharqda Sirdaryo viloyati Sharof Rashidov tumanlari va viloyatning Zarbdor, janubida Jizzax tumanlari bilan che-garadosh. Maydoni 0,38 ming km². Aholisi 57,9 ming kishi (2003). Paxtakor tumanida 1 shahar (Paxtakor), 7 qishloq fuqarolari yigʻini (Akmal Ikromov, Mingchinor, Olmazor, Oqbuloq, Paxtakor, Samarqand, Chamanzor) bor. Markazi — Paxtakor shahri"""
    await message.answer(text)


@dp.message_handler(text='Yangiobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Yangiobod_tumani.png/300px-Yangiobod_tumani.png')
    text = """Yangiobod tumani — Jizzax viloyatidagi tuman. 1999-yil 30 aprelda tashkil qilingan. Gʻarbdan Zomin tumani, janubiy, sharq, shimolidan Tojikiston Respublikasi bilan chegaradosh. Maydon 0,72 ming km². Aholisi 22,7 ming kishi (2005). Tumanda 5 qishloq fuqarolari yigʻini (Xovos, Sarmich, Xoʻjamushkent, Sovot, Xavotogʻ) mavjud. Markazi — Balandchaqir qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Zomin')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Zomin_tumani.png/300px-Zomin_tumani.png')
    text = """Zomin tumani — Jizzax viloyatidagi tuman. 1926 yil 29 sentabrda tashkil etilgan (1962 yil 24 dekabrda Jizzax tumani bilan birlashtirilgan, 1964 yil 31 dekabrda qayta tuzilgan. Shimolda viloyatning Zarbdor tumani, gʻarbda Baxmal va Jizzax tumanlari, sharqda, shimoliy-sharqda Yangiobod tumani, janubiy-sharqda Tojikston Respublikasi bilan chegaradosh. Maydoni 2,87 ming km2. Aholisi 150 ming kishi (2010). Zomin tumanida 2 shaharcha (Dashtobod, Zomin) va 11 qishloq fuqarolari yigʻini (Beshkubi, Gulshan, Duoba, Navoiy, Obihayot, Tinchlik, Toshkesgan, Chorvador, Shirin, Yangi-hayot, Gʻallakor) bor. Markazi — Zomin shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Zafarobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Zafarobod_tumani.png/300px-Zafarobod_tumani.png')
    text = """Zafarobod tumani - Jizzax viloyatitsat tuman. 1973-yil 12 aprelda tashkil etilgan. Jan.da Jizzax tumani, shimoli.gʻarbda Arnasoy va Doʻstlik tumanlari, shimolida Forish tumani, sharkda Paxtakor tumani bilan chegaradosh. Maydon 0,47 ming km2. Aholisi 40,3 ming kishi (2000). Zafarobod tumanida 1 shaharcha (Zafarobod), 7 qishloq fuqarolari yigʻini (Birlik, Yorqin, Lolazor, Timiryazev, Uchqahramon, Chimqoʻrgʻon, Hulkar) bor. Markazi — Zafarobod shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Zarbdor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Zarbdor_tumani.png/300px-Zarbdor_tumani.png')
    text = """Zarbdor tumani Jizzax viloyatidagi tumandir. 1979-yil 4-dekabrda tashkil etilgan. Shimoli-sharqda Sirdaryo viloyati, gʻarbda Sharof Rashidov tumani, sharqda Yangiobod tumani, janubida Zomin tumani bilan chegaradosh. Maydoni 0,56 ming km2. Aholisi 81,7 ming kishi (2020). Bu tumanda 4 qishloq fuqarolari yigʻini (Adirobod, Andijon,Kerz, Sharq Yulduzi, Yangikent) va 1 ta shahar, 2 ta shaharcha (Boʻston, Sharq yulduzi) bor. Markazi — Zarbdor shahri."""
    await message.answer(text)


@dp.message_handler(text='Bulungʻur')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Bulung%27ur_tumani.png/300px-Bulung%27ur_tumani.png')
    text = """Bulungʻur tumani — Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 29-sentabr da tashkil etilgan. Shimolida Jizzax viloyatining Gʻallaorol tumani, sharqda Baxmal tumani, gʻarbda Samarqand viloyatining Jomboy tumani, janubi-garbda Toyloq tumani, jan.da Urgut tumani va jan.sharqda Tojikiston bilan chegaradosh. Maydoni 0,76 ming km². Aholisi 116,8 ming kishi (2000). Bulungʻur tumani da 1 shahar (Bulungʻur) va 7 qishloq fuqarolari yigʻini (Beshqoʻton, Kulchabiy, Navoiy, Sohibkor, Fozil Yoʻldosh, Oʻrtabuloq, Kildon) bor. Markazi — Bulungʻur shahr"""
    await message.answer(text)


@dp.message_handler(text='Ishtixon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/1/12/Ishtixon_tumani.png')
    text = """Ishtixon tumani — Oʻzbekiston Respublikasi Samarkand viloyatidagi tuman. Samarqand shahridan 68 km. Viloyatning Qoʻshrabot, Payariq, Kattaqoʻrgʻon, Pastdargʻom tumanlari, bilan chegaradosh. Markazi - Ishtihon shahri. Umumiy yer maydoni 0,72 ming kv.km.
Aholisi: 218,431 ming kishi (2013.01.01.). Shundan shahar joylarda 64,447 kishi, qishloq joylarda 154,043 kishi yashaydi. Aholisi asosan oʻzbeklar shuningdek rus, tojik, koreys, ukrain, tatar, arman va boshqa millatlar yashaydi. Aholining oʻrtacha zichligi 1 km.kv ga 303.3 kishi."""
    await message.answer(text)


@dp.message_handler(text='Jomboy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/e/eb/Jomboy_tumani.png')
    text = """Jomboy — Oʻzbekiston Respublikasi Samarqand viloyatidagi qishloq tumani va tuman markazi nomi. Toponimning jom yoki yom „bekat, istehkom“ soʻzi bilan aloqasi yoʻq. Ye.Koychibayevning aytishicha, Jomboy nomli toponim Qozogʻistonning Guryev oblastida ham boʻlib, etnik nom asosida vujudga kelgan. Jomboy qozoqlarning bir urugʻi nomi. Markazi — Jomboy shahri"""
    await message.answer(text)


@dp.message_handler(text='Kattaqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Kattaqo%27rg%27on_tumani.png/1024px-Kattaqo%27rg%27on_tumani.png')
    text = """Kattaqoʻrgʻon tumani — Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 28 -sentabrda tashkil etilgan. Shim.dan viloyatning Ishtixon, janubi-sharqdan Nurobod, gʻarbdan Narpay, sharqdan Pastdargʻom, shimoli-gʻarbdan Navoiy viloyatining Xatirchi tumanlari bilan chegaradosh. Mayd. 1,47 ming km2. Aholisi 189 ming kishi (2002). Tumanda 2 shaharcha (Suv Ombori, Payshanba) va 17 qishloq fuqarolar yigʻini (Abulqosim, Alijon, Girdiqoʻrgʻon, Durbesh, Kattakoʻrpa, Kattaming , Kiikmindon, Jumaboy, Moybuloq, Omonboy, Saroyqoʻrgʻon, Yangiqoʻrgʻoncha, Qoʻshtepa, Uyshun, Shoʻrak, Murtak, Zarafshon) bor. Markazi Payshanba shaharchasi"""
    await message.answer(text)


@dp.message_handler(text='Qoʻshrabot')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Qo%27shrabot_tumani.png/300px-Qo%27shrabot_tumani.png')
    text = """Qoʻshrabot tumani - Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1978-yil 3-aprelda tashkil etilgan. Sharqdan Payariq, jan.dan Ishtixon, Kattaqoʻrgʻon tumanlari, gʻarb va shim.dan Navoiy viloyatining Nurota, jan.-gʻarbdan xatirchi tumanlari, shim.sharqdan Jiz-zax viloyati bilan chegaradosh. Maydoni 1,11 ming km2. Aholisi 93,3 ming kishi (2004). Tumanda 7 ta qishloq fuqarolari yigʻini (Pichot, Joʻsh, Zarmitan, Oxun-boboyev nomidagi, Oqtepa, Pangat, Urganji, Qoʻshrabot) bor. Markazi — Qoʻshrabot qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Narpay')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Narpay_tumani.png/300px-Narpay_tumani.png')
    text = """Narpay tumani - Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Viloyatning janubida joylashgan. Sharq va gʻarbdan viloyatning Kattaqoʻrgʻon, Paxtachi, shimolidan Navoiy viloyatining Xatirchi tumani, janubidan Nurobod tumani, Qashqadaryo viloyati bilan chegaradosh. Maydoni 0,44 ming km². Aholisi 152 ming kishi (2003). Tumanda 1 shahar (Oqtosh), 1 shaharcha (Mirbozor), 9 qishloq fuqarolar yigʻini (Islomshoir, Kosagaron, Olti-oʻgʻil, Chaqar, Yangirabot, Yangiqoʻrgʻon, Qadim, Qorakoʻl, Qorasiyrak) bor. Markazi — Oqtosh shahri"""
    await message.answer(text)


@dp.message_handler(text='Nurobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Nurobod_tumani.png/300px-Nurobod_tumani.png')
    text = """Nurobod tumani - Samarqand viloyatitt tuman. 1975-yil 26 noyab.da tashkil etilgan. Shim.dan Kattaqoʻrgʻon, Narpay, Paxtachi tumanlari, gʻarbdan Navoiy viloyati, sharkdan Samarqand, Pastdargʻom tumanlari, jan. dan Qashqadaryo viloyati bilan chegaradosh. Maydoni 4,79 ming km². Aholisi 98,7 ming kishi (2003). Tumanda 1 shahar (Nurobod), 7 qishloq fuqarolar yigʻini (Jarquduq, Jam, Nurbuloq, Sazagʻon, Tim, Tutli, Ulus) bor. Markazi — Nurobod shahri"""
    await message.answer(text)


@dp.message_handler(text='Oqdaryo')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Oqdaryo_tumani.png/300px-Oqdaryo_tumani.png')
    text = """Oqdaryo tumani — Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 29-sentabrdatashkil etilgan. Ishtixon, Pastdargʻom, Samarqand, Jomboy, Payariq tumanlari bilan chegaradosh. Maydoni 0,37 ming km². Aholisi 101,7 ming kishi (2000). O.t,da 2 shaharcha (Dahbed, Loyish), 6 kish-lok fukarolari yigʻini (Zarafshon, Primkent, Yangikent, Yangikoʻrgʻon, Qorateri, Qurilish) bor (2000). Markazi — Loyish shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Paxtachi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Paxtachi_tumani.png/300px-Paxtachi_tumani.png')
    text = """Paxtachi tumani - Oʻzbekiston Respublikasi Samarqand viloyati tarkibidagi tuman. 1935-yil 9-fevralda Narpay tumani hududining bir qismida Paxtakor tumani nomi bilan tashkil qilingan. 1963-yilda yana Narpay tumaniga qoʻshilgan. 1973-yil 12-aprelda Paxtachi tumani nomi bilan yana Narpay tuma-nidan alohida tuman qilib ajratildi. Sharkdan Narpay tumani, shim, shim. -gʻarb va gʻarbdan Navoiy viloya-tining Xatirchi, Navoiy, Navbahor tumanlari, jan.dan Nurobod tumani bilan chegaradosh. Maydoni 1,37 ming km². Aholisi 114,6 ming kishi (2003). Paxtachi tumanida 1 shaharcha (Ziyovuddin), 8 qishloq fuqarolari yigʻini (Misit, Poʻlatchi, Sultonobod, Xayrobod, Xumor, Qarnob, Quyiboq, Gʻalaba) bor. Markazi — Ziyovuddin shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Urgut')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/c/c7/Urgut_tumani.png')
    text = """Urgut tumani — Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Viloyatning janubiy sharqiy qismida joylashgan. Shimoliy sharqda Zarafshon daryosi orqali Bulungʻur tumani, shimolda Toyloq, shimoliy gʻarbda va gʻarbda Samarqand tumanlari, sharqda Tojikiston Respublikasi, janubda Qashqadaryo viloyati bilan chegaradosh. Maydoni 1120,3 km². Aholisi 564 ming kishi (2022). Tumanda bitta shahar (Urgut), 13 qishloq fuqarolari yigʻini (Baxrin, Beshbuloq, Jartepa, Ilonli, Ispanza, Mirzaqishloq, Pochvon, Sanchiqul,Uramas, Yangiariq, Qoratepa, Gʻo's, Buloqboshi) Quyiqishloq bor.
Markazi — Urgut shahri."""
    await message.answer(text)


@dp.message_handler(text='Payariq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Payariq_tumani.png/300px-Payariq_tumani.png')
    text = """Payariq tumani - Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan (markazi Chelak qishlogʻi boʻlgan). 1953-yil Payariq tumanining bir qismidan Narimonov tumani tuzilgan. 1959-yilda Narimonov tumani Payariq tumaniga qoʻshilgan (markazi Narimonov qishlogʻi). 1991-yilda Payariq tumanidan Chelak tumani ajralib chiqqan. 2001-yilda yana Payariq tumani bilan Chelak tumanlari birlashtirilib, ular negizida Payariq tumani tashkil qilindi (markazi Payariqsh.). Payariq tumani oʻrtacha 610 m balandlikda. Shim.-gʻarbdan viloyatning Qoʻshrabot, gʻarbdan Ishtixon, jan.dan Oqdaryo va Jomboy tumanlari, shim.dan Jizzax viloyatining Forish, shim.-sharqdan Gʻallaorol tumanlari bilan chegaradosh. Maydoni 1,29 ming km². Axrlisi 182,9 ming kishi (2003). Tumanda 2 shahar (Payariq, Chelak), 6 qishloq fuqarolari yigʻini (Guliston, Koʻkdala, Koʻltoʻsin, Sanoat, Choshtepa, Qorasuv) bor. Tuman markazi — Payariq shahri"""
    await message.answer(text)


@dp.message_handler(text='Pastdargʻom')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Pastdarg%27om_tumani.png/300px-Pastdarg%27om_tumani.png')
    text = """Pastdargʻom tumani - Oʻzbekiston Respublikasi Samarqand viloyatilagi tuman. 1926-yil 29-sentabrida tashkil etilgan. 1929—38 yillarda Akmal Ikromov tumani deb atalgan. 2001-yilda Pastdargʻom tumaniga Goʻzalkent tumani qoʻshildi. Shim.dan Oqdaryo va Ish-tixon, gʻarbdan Kattaqoʻrgʻon, Nurobod tumanlari, jan.dan Qashqadaryo viloya-ti va sharkdan Samarqand tumani bilan chegaradosh. Maydoni 0,87 ming km². Aholisi 325 251 kishi (2019). Pastdargʻom tumanida 1 shahar (Juma), 12 shaharcha, 107 mahalla fuqarolari yigʻini, 151 qishloq aholi punktlari bor. Markazi — Juma shahri."""
    await message.answer(text)


@dp.message_handler(text='Samarqand')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Samarqand_tumani.png/300px-Samarqand_tumani.png')
    text = """Samarqand tumani — Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1926-yil 29 sentabrda Yuqori Dargom nomi bilan tashkil etilgan. Shim.dan Oqdaryo, shim.sharqdan Jomboy, sharqdan Bulungʻur, jan.dan Urgut, gʻarbdan Nurobod, Pastdargʻom tumanlari bilan chegaradosh. Maydoni 500 km². Aholisi 305,9 ming kishi (2012)[1]. Tumanda 8 qishloq fuqarolari yigʻini (Bogʻibaland, Dashtakibolo, Kattaqoʻrgʻonariq, Kulbapoyon, Oxunboboyev, Ogʻaliq, Ulugʻbek, Qaynama) bor (2004). Markazi — Gulobod qishlogʻi"""
    await message.answer(text)


@dp.message_handler(text='Toyloq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Toyloq_tumani.png/300px-Toyloq_tumani.png')
    text = """Toyloq tumani - Oʻzbekiston Respublikasi Samarqand viloyatidagi tuman. 1992-yil 9 aprelda tashkil etilgan. Viloyatning jan.sharqiy qismida. Shim.dan Jomboy va Bulungʻur, jan. va sharqdan Urgut, gʻarbdan Samarqand tumanlari bilan chegaradosh. Maydoni 0,28 ming km². Aholisi 134,3 ming kishi (2003). T.da 9 qishloq fuqarolari yigʻini (Adas, Bogʻizagʻon, Jumabozor, Gʻulba, Madaniyat, Sochakibolo, Tepaqishloq, Toyloq, Qoʻrgʻoncha) bor. Markazi — Toyloq qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Angor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Angor_tumani.png/300px-Angor_tumani.png')
    text = """Angor tumani 1952-yil 16-aprelda tashkil tashkil etilgan edi. 1962-yil dekabridan Termiz tumani tarkibiga qoʻshib yuborildi. 1979-yili dekabrda qayta tashkil etildi. Umumiy maydoni 387,3 kv .km. Aholisi 82,1 ming kishi (1996). Tuman markazi – Angor shaharchasi Termiz shahridan 33 km shimoli – gʻarbda joylashgan. Tumanda 7 qishloq bor (Birinchi may, Doʻstlik, Zang, Navoiy, Tallimaron, Yangiobod, Qayron). Toshkent – Termiz avtomobil yoʻli yoqasida, yaqin temir yoʻl bekati (Navshahar) – 14 km. Angor tumanida 8 jamoa xoʻjaligi bor. Tuman gʻalla, paxta va sabzavot – poliz ekinlariga ixtisoslashgan. Bogʻ va tokzor bor ."""
    await message.answer(text)


@dp.message_handler(text='Boysun')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Boysun_tumani.png/300px-Boysun_tumani.png')
    text = """Boysun tumani — Surxondaryo viloyatitsat tuman. 1926-yil 29-sentabrda tashkil etilgan (1962-yil 24-dekabrda Sherobod tumani bilan birlashtirilgan. 1965-yil 29-dekabrda qayta tuziddi). Boysun tumani viloyatning gʻarbida joylashgan. Shimoli-sharqda Sariosiyo, sharqda Qumqoʻrgʻon, janubida Qiziriq, Bandixon tumanlari, janubi-gʻarbda Sherobod tumani bilan, shimoli-gʻarbda Qashqadaryo viloyatining Qamashi va gʻarbda Dehqonobod tumanlari bilan chegaradosh. Maydoni 3,72 ming km². Aholisi 79 ming kishi (2000). Boysun tumanida 1 ta tumanga boʻysunuvchi shahar (Boysun), 7 qishloq fuqarolari yigʻini (Avlod, Boysun, Darband, Machay, Rabot, Sayrob, Qurgʻoncha) bor. Markazi — Boysun shahri."""
    await message.answer(text)


@dp.message_handler(text='Denov')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Denov_tumani.png/1280px-Denov_tumani.png')
    text = """Denov tumani – Surxondaryo viloyatidagi tuman. 1926-yil 2-sentabrda tashkil etilgan. Denov tumani viloyatning Shoʻrchi, Sariosiyo, Uzun, Oltinsoy tumanlari bilan chegaradosh. Maydon. 0,75 ming km2. Aholisi 399,9 ming kishi (2022). Denov tumanida 1 shahar (Denov), 2 shaharcha (Doʻstlik va Xayrabod), 18 qishloq fuqarolari yigʻini (Anbarsoy, Binokor, Dahana, Denov, Kenagas, Navroʻz, Pistamozor, Sina, Tortuvli, Xayrobod, Xolchayon, Fargʻona, Yurchi, Yangibogʻ, Yangizamon, Yangiobod, Kiziljar, Hazorbogʻ) bor. Markazi — Denov shahri."""
    await message.answer(text)


@dp.message_handler(text='Jarqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Jarqo%27rg%27on_tumani.png/300px-Jarqo%27rg%27on_tumani.png')
    text = """Jarqoʻrgʻon tumani - Surxondaryo viloyatidagi tuman. 1926 yil 29 sentabrda tashkil etilgan (1962 yil 24 dekabrda Shoʻrchi tumani bilan birlashtirilgan, 1964 yil 31 dekabrda qayta tuzilgan). Shimoliy da viloyatning Qiziriq va Bandixon tumanlari, sharqda Qumqoʻrgʻon tumani, janubi-gʻarbda Termiz va Angor tumanlari, sharqda Tojikiston Respublikasi bilan chegaradosh. Maydon 1,14 ming km2. Aholisi 142,2 ming kishi (2000). Yaqin temir yoʻl stansiyasi — Jarqoʻrgʻon. J. t.da 1 shahar (Jarqoʻrgʻon), 1 shaharcha (Kakaydi) va 7 qishloq fuqarolari yigʻini (Dehqonobod, Jarqoʻrgʻon, Minor, Oqqoʻrgʻon, Surxon, Chorjoʻy, Sharq Yulduzi) bor. Markazi — Jarqoʻrgʻon sh"""
    await message.answer(text)


@dp.message_handler(text='Qiziriq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Qiziriq_tumani.png/1280px-Qiziriq_tumani.png')
    text = """Qiziriq tumani — Surxondaryo viloyatidagi tuman. 1975-yil 6-martda tashkil etilgan. Gʻarbdan Sherobod, janubidan Angor, shimolidan Bandixon, sharqdan Jarqoʻrgʻon, Shimoli-sharqdan Qumqoʻrgʻon, shimoli-gʻarbda Muzrabot tumanlari bilan chegaradosh. Maydoni 0,33 ming km2. Aholisi 350 ming kishi (2022). Tarkibida 1 shaharcha (Sariq), 5 qishloq fuqarolari yigʻini (Boʻston, Mehnatobod, Paxtakor, Yangiyoʻl, Yangi Hayot) bor. Markazi – Sariq shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Qumqoʻrgʻon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Qumqo%27rg%27on_tumani.png/300px-Qumqo%27rg%27on_tumani.png')
    text = """Qumqoʻrgʻon tumani - Surxondaryo viloyatidagi tuman. Viloyatning markaziy qismida joylashgan. 1977-yil 24 martda tashkil etilgan. Shim.dan Sariosiyo, jan. va jan.-gʻarbdan Jarqoʻrgʻon, sharqdan Oltinsoy, Shoʻrchi, Uzun, shim.-sharqdan Denov, gʻarbdan Bandixon va Boysun tumanlari, jan.sharqdan Tojikiston Respublikasi bilan chegaradosh. Maydoni 2,2 ming km2. Aholisi 158,3 ming kishi (2005). Tumanda 1 shahar (Qumqoʻrgʻon), 1 shaharcha (Hurriyat), 8 qishloq fu-qarolari yigʻini (Arslonboyli, jaloyir, Ketmon, Oqjar, Oqqapchi-gʻay, Yuqori Kakaydi, Oʻzbekiston, Qumqoʻrgʻon) bor. Tuman markazi — Qumqoʻrgʻon shahri """
    await message.answer(text)


@dp.message_handler(text='Muzrabot')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Muzrabot_tumani.png/300px-Muzrabot_tumani.png')
    text = """Muzrabot tumani - Surxondaryo viloyatidagi tuman. 1968-yil 25-dekabrda tashkil etilgan. 1994-yilgacha Gagarin tumani deb atalgan. Viloyat hududining eng janubiy qismini egallaydi. Shimolida viloyatning Sherobod va Qiziriq, sharqda Angor tumanlari, janubi-sharqda Termiz tumani, janubida Amudaryo orqali Afgʻoniston, gʻarbda Turkmaniston bilan chegaradosh. Maydoni 740 km². Aholisi 99,1 ming kishi (2002). Tumanda 9 qishloq fuqarolar yigʻini (Beshqoʻton, Boldir, Guliston, Muzrabot, Navbahor, Obodon, Xalqobod, Shoʻrob, Qorakamar) bor. Tuman markazi — Xalqobod qo'rg'oni."""
    await message.answer(text)


@dp.message_handler(text='Oltinsoy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Oltinsoy_tumani.png/300px-Oltinsoy_tumani.png')
    text = """Oltinsoy tumani, Surxondaryo viloyatidagi tuman. 1981-yil 23-noyabrda Shoʻrchi va Denov tumani qismlaridan tuzilgan. Viloyatning Denov, Boysun, Shoʻrchi, Qumqoʻrgʻon tumanlari bilan chegaradosh. Maydoni 0,56 ming km². Aholisi 116,9 ming kishi (2003). Tumanda 9 qish-loq fuqarolar yigʻini (Vaxshivor, Dugʻoba, Mirshodi, Oltinsoy, Oqarbuloq, Oqoltin, Xoʻjasoat, Chep, Qarluq) bor. Tuman markazi — Qarluq qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Sariosiyo')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Sariosiyo_tumani.png/1280px-Sariosiyo_tumani.png')
    text = """Sariosiyo tumani - Surxondaryo viloyatidagi tuman. 1926-yil 29 sentabrda tashkil etilgan. 1959-yildan Denov, 1962-yildan Uzun tumanlari tarkibida, 1964-yil 22 fevraldan Sariosiyo tumani nomi bilan qaytadan tuzilgan. Jan.sharqsan Uzun, janubi-gʻarbdan Boysun, jan.dan Denov, Qumqoʻrgʻon tumanlari, shimoliy va sharqdan Tojikiston Respublikasi, shim.gʻarb va gʻarbdan Qashqadaryo viloyati bilan chegaradosh. Maydoni 3,15 ming km². Aholisi 217,7 ming kishi (2022). Tumanda 1 shaharcha (Sariosiyo), 1 shahar (Shargʻun), 9 qishloq fuqarolari yigʻini (Boʻston, Dashnobod, Navroʻz, Sangardak, Sariosiyo, Soʻfiyon, Toqchiyon, Xufar, Oʻzbekiston) bor. Markazi — Sariosiyo shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Bandixon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Surxondaryo_districts.png/1280px-Surxondaryo_districts.png')
    text = """Bandixon tumani — Surxondaryo viloyatidagi tuman. 1992-yil 18-mayda tashkil etilgan. 2010-yil moliyaviy kamchiliklar tufayli tugatilgan. 18-oktabr 2019-yilda qayta tashkil etilgan. Bandixon tumani viloyatning Qumqoʻrgʻon, Qiziriq, Jarqoʻrgʻon, Sherobod, Boysun tumanlari bilan chegaradosh. Maydoni 0,20 ming km2. Aholisi 75,0 mingdan ortiq kishi (2019). Bandixon tumanida 5 qishloq fuqarolari yigʻini (Bandixon, Kirshak, Olmazor, Chorvador, Qiziriq) bor. Markazi — Bandixon qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Sherobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Sherobod_tumani.png/300px-Sherobod_tumani.png')
    text = """Sherobod tumani — Surxondaryo viloyatidagi tuman. 1926-yil 29 sentyabrda tashkil etilgan. Gʻarb tomondan Turkmaniston bilan chegaradosh. Tuman shimolidan Boysun, shimoli-sharqsan Bandixon, sharqdan Qiziriq, jan.dan Muzrabot, janubi-shardan Angor tumanlari, shim.gʻarbdan Qashqadaryo viloyati, gʻarbdan Turkmaniston bilan chegaradosh. Maydoni 2,73 ming km². Aholisi 173.2 ming kishi (2018). Sherobod tumanida 1 shahar (Sherobod), 9 qishloq fuqarolari yigʻini (Boʻston, Zarabogʻ, Oqqoʻrgʻon, Rabotak, Sariqamish, Seplon, Talashqon, Ko'hitang, Yangiturmush) bor. Markazi – Sherobod shahri."""
    await message.answer(text)


@dp.message_handler(text='Shoʻrchi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Sho%27rchi_tumani.png/300px-Sho%27rchi_tumani.png')
    text = """Shoʻrchi tumani — Surxondaryo viloyatidagi tuman. 1935-yil 9 fevralda tashkil etilgan. Shimolidan Oltinsoy, Denov, janubiy va gʻarbdan Qumqoʻrgʻon, sharqdan Uzun tumanlari bilan chegaradosh. Maydoni 0,85 ming km². Aholisi 152,3 ming kishi (2004). Tumanda 1 shahar (Shoʻrchi), 1 shaharcha (Elbayon bekati), 10 qishloq fuqarolari yigʻini (Baxtlitepa, Dalvarzin, Jaloyir, Kichik Savur, Oxunboboyev, Oqtumshuq, Sohibkor, Shoʻrchi, Elobod, Yangibozor) bor. Tuman markazi — Shoʻrchi shahri. Aholisi, asosan, oʻzbeklar, shuningdek, tojik, rus, tatar va boshqalar millat vakillari ham yashaydi. Aholining oʻrtacha zichligi 1 km²ga 179,2 kishi (2004)"""
    await message.answer(text)


@dp.message_handler(text='Termiz')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Termiz_tumani.png/300px-Termiz_tumani.png')
    text = """Termiz tumani — Surxondaryo viloyatidagi tuman. 1926-yil 29 sentabrda tashkil etilgan. Janubiy va gʻarbdan Afgʻoniston, sharqdan Tojikiston, shimolidan viloyatning Angor va Jarqoʻrgʻon, shimoli-gʻarbdan Muzrabot tumanlari bilan chegaradosh. Maydoni 0,86 ming km². Aholisi 78,6 ming kishi (2004). Tumanda 5 qishloq fuqarolar yigʻini (Pattakesar, Paxtaobod, Uchqizil, Xotinrabot, Yangiariq) bor. Markazi — Uchqizil qishlogʻi.["""
    await message.answer(text)


@dp.message_handler(text='Uzun')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Uzun_tumani.png/300px-Uzun_tumani.png')
    text = """Uzun tumani — Surxondaryo viloyatidagi tuman, 1942-yil 12 yanvarda tashkil etilgan. 1959-yil 15 oktabrda Sariosiyo tumaniga qoʻshib yuborilgan, 1991-yil 29 martda qayta tuzildi. Uzun tumani shimoli-gʻarbdan Sariosiyo tumani, sharq, janubiy, shimolidan Tojikiston, janubi-gʻarbdan Qumqoʻrgʻon, gʻarbdan Denov, Shoʻrchi tumanlari bilan chegaradosh. Maydoni 2,33 ming km². Aholisi 128,0 ming kishi (2004). Tumanda 7 qishloq fuqarolari yigʻini (Bobotogʻ, Joncheka, Oqostona, Telpakchinor, Uzun, Fayzova, Xondiza) bor. Markazi — Uzun shahri."""
    await message.answer(text)


@dp.message_handler(text='Gʻijduvon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/G%27ijduvon_tumani.png/1280px-G%27ijduvon_tumani.png')
    text = """Gʻijduvon — Oʻzbekiston Respublikasining Buxoro viloyati Gʻijduvon tumanidagi shahar (1972-yildan), tuman markazi. Buxoro shahridan 49 km shimoli-sharqda, Buxoro vohasining yuqori qismida joylashgan. Yaqin temir yoʻl stansiyasi — Qiziltepa (17 km). Aholisi 38,6 ming kishi (2003). Gʻijduvon toponimining kelib chiqishi haqida mahalliy aholi orasida turli rivoyatlar mavjud. Shulardan „Kish tuvon“ („kish“ tojikcha ekin ekuvchi, „tuvon“ — manzil), yaʼni ekin ekadigan dehqonlar manzili yoki „Gʻujudehon“ — koʻp qishloklardan tashkil topgan joy maʼnosida izohlaydilar. Shahar hududi va uning atrofi qad.dan dehqonchilik rivojlangan hudud hisoblangan"""
    await message.answer(text)


@dp.message_handler(text='Jondor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Jondor_tumani.png/1280px-Jondor_tumani.png')
    text = """Jondor tumani - Oʻzbekiston Respublikasi Buxoro viloyatidagi tuman. 1935-yil 17 yanvarda tashkil etilgan. 1962-yil 24 dekabrdan Buxoro va Romitan tumanlari tarkibida boʻlgan. 1967-yil 9 yanvarda qayta tuzilgan. Jondor tumani janubiy-gʻarbdan Olot, Qorakoʻl tumanlari, sharq va shimoliy-sharqdan Buxoro, Romitan, Peshku tumanlari bilan chegaradosh. Maydoni 5,17 ming km2. Aholisi 123,7 ming kishi (2001). Jondor tumanida 1 shaharcha (Jondor), 13 qishloq fuqarolari yigʻini (Aleli, Dalmun, Lolo, Mirzayon, Navrabot, Oqshix, Romish, Poʻloti, Samonchuq, Sepatta, Xumdanak, Xumin, Qorali) bor. Markazi — Jondor shaharchasi. """
    await message.answer(text)


@dp.message_handler(text='Kogon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Kogon_tumani.png/300px-Kogon_tumani.png')
    text = """Kogon (1935-yilgacha Yangi Buxoro) — Oʻzbekiston Respublikasi Buxoro viloyatida oʻzining xoʻjalik-maʼmuriy potensiali jihatidan viloyat markazi boʻlmish Buxorodan keyingi ikkinchi yirik shahar. Buxorodan 12 kilometr janubi-sharqda, Buxoro — Qarshi avtomobil yoʻli yoqasida, Kanpir devor qoldiqlari ichkarisidagi obod yerda joylashgan.
Kogon tumanining maʼmuriy markazi. Kogon shahri va Kogon tumani hokimiyatlari shahar markazida yonma-yon joylashgan.
Temir yoʻl tuguni. Shaharda Buxoro viloyatining eng katta temir yoʻl stansiyasi va viloyatda yagona boʻlgan vokzal joylashgan.
Shahar 220 m balandlikdagi tekis yerda joylashgan. Yanvarning oʻrtacha temperaturasi —0,6°, iyulniki 29,6°. Yillik yogʻin 125 mm. Hargush kanalidan suv oladi. Maydoni 14,7 km². Aholisi 53,3 ming kishi (2002), asosan, oʻzbeklar, shuningdek, tojik, rus, tatar va boshqa millat vakillari ham yashaydi. Aholisining aksari qismi temir yoʻl transportida ishlaydi."""
    await message.answer(text)


@dp.message_handler(text='Olot')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Olot_tumani.png/300px-Olot_tumani.png')
    text = """Olot tumani — Oʻzbekiston Respublikasi Buxoro viloyatidagi tuman. 1943-yil 14-fevralda tashkil etilgan. 1960-yil Qorakoʻl tumaniga qoʻshilgan. 1973-yil 26-dekabrda qayta tashkil etilgan. 1983-yildan yana Qorakoʻl tuman i tarkibida. 1989-yildan Olot tumani yana aloxida tuman maqo-miga ega boʻldi. Buxoro viloyatining janubi-gʻarbida joylashgan. Jan., janubi-sharqdan Qashqadaryo viloyati, janubi-gʻarbdan eng katta masofada (75 km) Turkmanistonning Lebap viloyati (Amudaryo orqali), shimoli-gʻarb va Shimoli-sharqtomondan Buxoro viloyatining Jondor, Qo-rakoʻl, Buxoro, Qorovulbozor tumanlari bilan chegaradosh. Maydoni 3,22 ming km². Aholisi 77,9 ming kishi (2003). Tumanda 1 shahar (Olot), 10 qishloq fuqarolari yigʻini (Bahoriston, Guliston, Denov, Jumabozor, Kirlishon, Paxtakor, Soyinqorovul, Tolqonsayot, Chandir, Chorbogʻ) bor. Markazi — Olot shahri"""
    await message.answer(text)


@dp.message_handler(text='Peshkoʻ')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Peshku_tumani.png/300px-Peshku_tumani.png')
    text = """Peshkoʻ tumani — Oʻzbekiston Respublikasi Buxoro viloyatidagi tuman. 1950-yil 15-aprelda tashkil etilgan. Maydoni 8,72 ming km2. Aholisi 107,5 ming kishi (2013). Aholi zichligi 1 km2.ga 13,1 kishi toʻgʻri keladi. Peshkoʻ tumanida 10 qishloq fuqarolari yigʻini (Abu Ali ibn Sino, Bogʻimuso, Varaxsha, Jongeldi, Zandoni, Peshkoʻ, Chibogʻani, Yangibozor, Qalʼaimirishkor, Qoraqalpoq) bor[5]. Markazi — Yangibozor shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Qorakoʻl')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Qorako%27l_tumani.png/300px-Qorako%27l_tumani.png')
    text = """Qorakoʻl tumani — Oʻzbekiston Respublikasi Buxoro viloyatidagi tuman. Shimoliy va Shimoli-sharqdan Jondor tumani, janubi-sharqdan Olot tumani, janubiy va gʻarbdan Turkmanistonning Lebap viloyati, shimoli-gʻarbdan Romitan tumani bilan chegaradosh. Maydoni 9,84 ming km². Aholisi 145,3 ming kishi (2013). Tumanda 8 ta shaharcha (shahar tipidagi pasolka), 42 ta qishloq fuqarolar yigʻini (Sayot, Joʻrobod, Qulonchi, Qorakoʻl, Qozon, Dargʻali, Quyi Yangibozor, Quvvacha, Chandirobod, Jigʻachi, Qoraxoji, Qoraun, Chovli, Mallaishayx, Ziyorat, Bandboshi),  50 ta mahalla fuqarolar yigʻini bor. Markazi — Qorakoʻl shahri."""
    await message.answer(text)


@dp.message_handler(text='Qorovulbozor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Qorovulbozor_tumani.png/300px-Qorovulbozor_tumani.png')
    text = """Qorovulbozor tumani — Oʻzbekiston Respublikasi Buxoro viloyatidagi tuman.
1993-yil 12 yanvarda tashkil etilgan. Janubidan Qashqadaryo viloyatining Muborak tumani, gʻarbdan Olot, shimolidan Buxoro tumani, sharqdan Navoiy viloyatining Qiziltepa tumani bilan chegaradosh. Transport yoʻli stansiyasi. Maydoni 2,2 ming km2. Aholisi 13,9 ming kishi (2005). Tumanda 1 shahar (Qorovulbozor), 3 qishloq fuqarolari yigʻini (Boʻzachi, Jarqoq, Navbahor) bor. Tuman markazi — Qorovulbozor shahri"""
    await message.answer(text)


@dp.message_handler(text='Romitan')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Qorovulbozor_tumani.png/1280px-Qorovulbozor_tumani.png')
    text = """Romitan — Oʻzbekiston Respublikasi Buxoro viloyati Romitan tumanidagi shahar (1981-yildan), tumanning maʼmuriy markazi.
Yaqin temir yoʻl stansiyasi—Kogon (30 km). Viloyat markazi (Buxoro)dan 17 km. Aholisi 15 ming kishi (2003), asosan, oʻzbeklar, shuningdek, tojik, qozoq, tatar, rus va boshqa ham yashaydi. Romitan Oʻzbekistonning qad. shaharlaridan biri. Romitan nomi mahalliy rivoyatga koʻra, "Romitan" — "Tan oromi" dan deyiladi. "Romitan" atamasi turkiy mitan urugʻi nomidan kelib chiqqan degan taxminlar ham mavjud."""
    await message.answer(text)


@dp.message_handler(text='Shofirkon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Shofirkon_tumani.png/1280px-Shofirkon_tumani.png')
    text = """Shofirkon tumani - Oʻzbekiston Respublikasi Buxoro viloyati tarkibidagi tuman boʻlib, viloyatning shimolida joylashgan. 1926-yil 29 sentyabrda tashkil etilgan. Janubdan Vobkent, janubi-gʻarbdan Romitan, gʻarbdan Peshku, sharqdan Gʻijduvon tumanlari, shimoldan Navoiy viloyatining Konimex tumani bilan chegaradosh. Maydoni 3,72 ming km². Aholisi 136 ming kishi (2004). Tumanda 1 shahar (Shofirkon), 13 ta qishloq fuqarolari yigʻini (Bogʻiafzal, Vardonze, Denov, Doʻrmon, Iskogare, Joʻynov, Joʻyrabot, Sulton Joʻra, Tezguzar, Chandir, Sharofbobo Hamroyev, Qarmoqon, Savrak) mavjud. Markazi — Shofirkon shahri."""
    await message.answer(text)


@dp.message_handler(text='Vobkent')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Vobkent_tumani.png/300px-Vobkent_tumani.png')
    text = """Vobkent — Oʻzbekiston Respublikasi Buxoro viloyatidagi shahar (1981 yildan). Vobkent tumaninint maʼmuriy markazi. Vobkent — koʻhna shaharlardan biri.
Vobkent - (oʻgʻuz shevasidagi "vob" yoki "vahobkent" — "boʻz, qoʻriqaagi qishloq" maʼnosida). Oʻrta asrlarda Vobkent atrofida bir necha qishloq-qoʻrgʻonlar boʻlgan. Vobkentning gʻarbida joylashgan Narshax qishlogʻi shulardan biri. 10-asrda yashagan tarixchi olim Narshaxiy shu qishloqda tavallud topgan. Narshax qishlogʻi Muqanna qoʻzgʻoloni markazlaridan biri boʻlgan"""
    await message.answer(text)


@dp.message_handler(text='Buxoro')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Buxoro_tumani.png/300px-Buxoro_tumani.png')
    text = """Buxoro viloyati — Oʻzbekiston Respublikasining 12 viloyatlaridan biri. Oʻzbekiston viloyatlari ichida, chegasining kattaligi boʻyicha Navoiydan keyin ikkinchi oʻrinda turadi. 1938-yil 15-yanvarda tashkil etilgan. Buxoro viloyati hududi asosan Qizilqum choʻlida joylashgan. Janubi-sharqini Zarafshon vodiysi egallagan. Shimoli-gʻarbda Xorazm viloyati va Qoraqalpogʻiston Respublikasi, shimol va sharqdan Navoiy viloyati, janubi-sharqda Qashqadaryo viloyati, janubi-gʻarbda Turkmaniston bilan chegaradosh. Maydoni 39,4 ming km2. Aholisi 1443 mingdan ziyod kishi (2001). Buxoro viloyati tarkibida 11 qishloq tumani: Buxoro, Vobkent, Jondor, Kogon, Olot, Peshku, Romitan, Shofirkon, Qorovulbozor, Qorakoʻl, Gʻijduvon, 11 shahar (Buxoro, Galaosiyo, Vobkent, Gazli, Kogon, Olot, Romitan, Shofirkon, Qorakoʻl, Qorovulbozor, Gʻijduvon), 3 shaharcha (Jondor, Zafarobod, Yangibozor), 121 qishloq fuqarolari yigʻini bor. Buxoro shahar aholisining etnik tarkibi asosan Uzbek, Rus, Fors (Eroniylar), Turkman, tojik, Ukrain, koreys, tatar va boshqalar tashkil etadi.Markazi-Buxoro"""
    await message.answer(text)


@dp.message_handler(text='Gurlan')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Gurlan_tumani.png/300px-Gurlan_tumani.png')
    text = """Gurlan tumani — Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Janubda viloyatning Shovot tumani, janubi-sharqda Urganch, Yangibozor tumanlari va shimoli-sharqda Qoraqalpogʻiston Respublikasi, janubi-gʻarbda Turkmaniston bilan chegaradosh. Hududi 447,4 kv.km ni tashkil qiladi. Gurlan tumani viloyat hududining 7,3 foizini egallaydi. Mahalla fuqarolari yigʻinlari soni 50 ta, qishloq aholi punktlari soni 31 ta, shaharchalar soni 9 ta. Aholisi 152 ming kishi kishi (2022-yil 1-yanvar).[2].Gurlan tumanida 1 shaharcha (Gurlan), 11 qishloq fuqarolari yigʻini (Birlashgan, Vazir, Guliston, Dehqonobod, Doʻsimbiy, Olgʻa, Saxtiyon, Xizireli, Sholikor, Eshimjiyron, Oʻzbekistan) bor. Markazi — Gurlan shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Xonqa')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Xonqa_tumani.png/300px-Xonqa_tumani.png')
    text = """Xonqa tumani — Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1926-yil 29-sentyabrda tashkil etilgan. 1962-yil 24-dekabrda Yangiariq tumani gaqoʻshilgan. 1973-yil 26-dekabrda qayta tuzilgan. Tuman viloyatning shimoli-gʻarbiy va gʻarbiy qismida Urganch tumani, janubi-gʻarbda Xiva va Yangiariq tumanlari, janubiy va janubi-sharqda Bogʻot tumani bilan chegaradosh. Maydoni 0,43 ming km2. Aholisi 150,4 ming kishi (2008). Tumanda 1 shaharcha (Xonqa), 10 tuman fuqarolari yigʻini (Amudaryo, Jirmiz, Madir, Navxos, Namuna, Olaja, Sarapoyon, Tomadurgʻodik, Qirqyop, Qoraqosh) bor. Markazi — Xonqa shaharchasi."""
    await message.answer(text)



@dp.message_handler(text='Hazorasp')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Xazorasp_tumani.png/300px-Xazorasp_tumani.png')
    text = """Hazorasp tumani - Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1926 yil 29 sentabrda tashkil etilgan. Janubidan Turkmaniston, janubi-sharqdan Buxoro viloyati, shimolidan Qoraqalpogʻiston Respublikasi, gʻarbdan Bogʻot tumani bilan chegaradosh. Maydoni 2,06 ming km2. Tumanda 1 shahar (Pitnak), 1 shaharcha (Hazorasp), 11 qishloq fuqarolari yigʻini (Beshta, Boʻston, Karvak, Ov-shar, Pichoqchi, Sanoat, Yuqori muhamon, Pitnak, Sarimoy, Tuproqqalʼa, Yangibozor). Markazi — Hazorasp shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Xiva')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Xiva_tumani.png/1280px-Xiva_tumani.png')
    text = """Xiva – Oʻzbekiston Respublikasining Xorazm viloyatidagi shahar. Xiva shahri markazi. Oʻzbekistonning shimoliy gʻarbida, Xorazm viloyatning janubida, Amudaryoning chap sohilida, daryodan 40 km janubida, 95 m balandlikda joylashgan. Shahar yonidan Polvonyop (qadimiy Xeykaniq) kanali oʻtgan. Yaqin temir yoʻl stansiyasi – Urganch (30 km). Maydoni 0,08 ming km². 2022-yil 1-yanvar holatiga Xiva tuman doimiy aholisining soni 149 698 kishi, Xiva shahri – 95 246 kishini tashkil qilgan.[1] Shaharning qadimgi qismidagi juda koʻp arxitektura yodgorliklariga boy boʻlgan Ichan-Qal’a Sharqning ekzotik shahar timsolini oʻzida saqlab qolgan afsonaviy shahardir."""
    await message.answer(text)


@dp.message_handler(text='Qoʻshkoʻpir')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Qo%27shko%27pir_tumani.png/300px-Qo%27shko%27pir_tumani.png')
    text = """Qoʻshkoʻpir tumani – Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1936-yil 17 aprelda tashkil etilgan. 1962-yil 14 dekabr Da Xiva tumaniga qoʻshib yuborilgan. 1966-yil 9 yanvarda qayta tashkil etilgan. Shimoliy dan Shovot, shim.-sharq va sharqdan Urganch tumanlari, janubdan Xiva tumani, gʻarbdan Turkmaniston bilan chegaradosh. Maydoni 0,54 ming km2. Aholisi 128,7 ming kishi (2005). Tumanda 1 shaharcha (Qoʻshkoʻpir), 13 qishloq fuqarolari yigʻini (Shix, Kenagas, Oqdarband, Xonobod, Xosiyon, Shixmashhad, Yangilik, Oʻzbekyop, Oʻrtayop, Qatagʻon, Gʻozovot, Hadra, Hayrobod, Nezaxos) bor. Tuman markazi — Qoʻshkoʻpir shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Shovot')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Shovot_tumani.png/300px-Shovot_tumani.png')
    text = """Shovot tumani — Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Janubidan Qoʻshkoʻpir, janubi-sharqdan Urganch, sharqdan Yangibozor, shimoli-sharqdan Gurlan tumanlari, shimoliy, shimoli-gʻarb va gʻarbdan Turkmaniston bilan chegaradosh. Maydoni 0,46 ming km2. Aholisi 164,300 kishi (2018). Tumanda 1 shaharcha (Shovot), 11 qishloq fuqarolari yigʻini (Beshmertan, Boʻyrachi, Ijtimoiyat, Katqalʼa, Xitoy, Chigʻatoyqalʼa, Choʻqli, Shovotqalʼa, Oʻzbekiston, Qangʻli, Qiyot) bor. Markazi — Shovot shaharchasi"""
    await message.answer(text)


@dp.message_handler(text='Urganch')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Urganch_tumani.png/300px-Urganch_tumani.png')
    text = """Urganch tumani - Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1926-yil 29 sentabrda tashkil etilgan. 1962-yil 24 dekabrda Shovot tumaniga qoʻshilgan, 1964-yil 31 dekabrda qayta tashkil etilgan. Sharkdan Xonqa, gʻarbdan Qoʻshkoʻpir, Shovot va Yangibozor tumanlari, shim.dan Gurlan tumani va Qoraqalpogʻiston Respublikasi, jan.dan Xiva, Yantiariq tumanlari bilan chegaradosh. Maydoni 0,46 ming km². Aholisi 141,1 ming kishi (2004). Tumanda 1 shaharcha (Chalish), 10 qishloq fuqarolar yigʻini (Bekobod, Chakkasholikor, Chandirqiyot, Chatkoʻpir, Yuqoribogʻ, Yuqoridoʻrman, Qoramon, Qorovul, Gʻalaba, Gʻoybu) bor. Tuman markazi — Qorovul qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Yangiariq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Yangiariq_tumani.png/300px-Yangiariq_tumani.png')
    text = """Yangiariq tumani — Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman, 1926-yil 29-sentabrda tashkil etilgan. Shimoldan Xonqa, sharqdan Bogʻot, gʻarbdan Xiva tumanlari, janubdan Turkmaniston bilan chegaradosh. Maydoni 0,40 ming km2. Aholisi 110,5 ming kishi (2018). Tumanda 10 qishloq fuqarolari yigʻini (Gullanbogʻ, Gulobod, Kattabogʻ, Ostona, Oxunboboyev, Tagan, Chigʻirchi, Yangiariq, Quruqtom ,Qorakoʻz) bor. Markazi — Yangiariq qishlogʻi"""
    await message.answer(text)


@dp.message_handler(text='Yangibozor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Yangibozor_tumani.png/1280px-Yangibozor_tumani.png')
    text = """Yangibozor tumani — Oʻzbekiston Respublikasining Xorazm viloyatidagi tuman. 1950-yilda tashkil etilgan. Keyinroq Urganch va Gurlan tumanlariga qoʻshib yuborilgan. Tuman yangidan 1989-yilda tashkil etildi. Shim.gʻarbdan Gurlan, jan.sharqdan Urganch, jan.gʻarb va gʻarbdan Shovot tumanlari, shim. va sharqdan Amudaryo orqali Qoraqalpogʻiston Respublikasi bilan chegaradosh. Mayd. 0,34 ming km².
Aholisi 66,4 ming kishi (2005). Yangibozor tumani da 1 shaharcha (Yangibozor), 8 qishloq fuqarolari yigʻini (Boshqirshix, Bogʻolon, Boʻzqalʼa, Oyoqdoʻrmon, UyGʻUR> Chubalanchi, Shirinqoʻngʻirot, Qalandardoʻrmon) bor. Markazi — Yangibozor shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Tupproqqalʼa')
async def echo(message: types.Message):
    await message.answer_photo('https://telegra.ph/file/108b4d031f35588e2a7e9.png')
    text = """Tuproqqalʼa — Xorazmning qadimgi shaharqalʼa xarobasi; mil. 3—4-asrlardagi xorazmshohlar qarorgohi. Hozirgi Beruniy sh. atrofidagi hududda joylashgan.
1938—50 yillarda S. P. Tolstoye rahbarligidagi Xorazm arxeologiyaetnografiya ekspeditsiyasi tomonidan oʻrganilgan. T. tarhi toʻgʻri burchakli (500×350 m) boʻlib, gumbazsimon yoʻlakli va burjli mudofaa devori bilan oʻralgan. Devorning mustahkam jan. darvozasidan otashkada tomon markaziy koʻcha oʻtgan. Koʻndalang tushgan koʻchalar shaharni 10 ta kvartal (mahalla)ga ajratgan. T.ning madaniy qatlamidan, mil. boshlaridan 6-asrgacha boʻlgan davrga oid ashyoviy materiallar chiqqan. T.ning shim.sharqiy qismida maxsus koʻtarma supa (bal. 14 m, maydoni 80*80 m) ustiga xom gʻishtdan saroy qurilgan. Unga yondosh qilib bal. 25 m li 3 ta minorasi boʻlgan ark binosi (maydoni 40×40 m) bunyod etilgan. Arkka sharq tomonidan kutarma yoʻlak orqali kirilgan. T.da 100 ga yaqin turar joy, xoʻjalik binolari va 8 ta saroy xonalari qazilgan."""
    await message.answer(text)


@dp.message_handler(text='Bogʻot')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Bog%27ot_tumani.png/300px-Bog%27ot_tumani.png')
    text = """Bogʻot tumani — Oʻzbekiston Respublikasining Xorazm viloyati tarkibidagi tuman. 1926-yil 29-sentabrda tashkil etilgan (1930 va 50-yillarda bir necha marta yondosh tumanlarga qoʻshib yuborilgan va qayta tiklangan, 1970-yil 7-dekabrda qayta tashkil etildi). Bogʻot tumani Xorazm viloyatining janubi-sharqiy qismida joylashgan. Gʻarb va shimolda viloyatning Yangiariq va Xonqa tumanlari, Amudaryo bilan, sharqda Hazorasp tumani va janubida Turkmaniston bilan chegaradosh. Maydoni 0,44 ming km2. Aholisi 130 ming kishidan ziyod (2008). Bogʻot tumanida 11 qishloq fuqarolari yigʻini (Beshariq, Bogʻot, Dehqonbozor (Kirov), Madaniyat (Pobeda), Nayman (Leninizm), Xitoy (Jdanov), Xoʻjalik, Qizilravot, Qipchoq, Qorayantoq (Dmitrov), Qulonqorabogʻ (Lenin)) bor. Markazi — Bogʻot shaharchasi"""
    await message.answer(text)


@dp.message_handler(text='Nukus')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/6/64/Location_of_Nukus_District_in_Qoraqalpog%E2%80%99iston.png')
    text = """Nukus tumani — Qoraqalpogʻiston Respublikasidagi tuman. 1968-yil 25-dekabrda tashkil etilgan. Gʻarbda Xoʻjayli, shim.-gʻarbda Amudaryo orqali Qanlikoʻl tumani, sharkda Qoraoʻzak, shim.-sharqda Kegeyli, shimolda Boʻzatov tumanlari, jan.-sharkda Amudaryo tumani bilan chegaradosh. Maydoni 1,0 ming km². Aholisi 43,5 ming kishi (2001). Tumanda 1 shaharcha (Oqmangʻit), 6 ovul fuqarolari yigʻini (Arbashi, Baqanshaqli, Kerder, Samanbay, Taqirkoʻl, Qirontov) bor. Markazi – Oqmangʻit shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Amudaryo')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Amudaryo_tumani.png/1280px-Amudaryo_tumani.png')
    text = """Amudaryo tumani – Qoraqalpogʻiston Respublikasi tarkibidagi tuman. 1957-yil 18-dekabrda tashkil etilgan. Amudaryo tumani shimolida Nukus tumani, sharqda Xorazm viloyatining Gurlan tumani, janubiy hamda gʻarbda Turkmanistonning Gubadogʻ tumani bilan chegaradosh. Maydoni 1,02 ming km². Aholisi 204,7 ming kishidan ziyod (2020). Amudaryo tumanida 1 shahar (Mangʻit), 2 shaharcha (Jumurtov va Qipchoq), 10 ovul fuqarolari yigʻini (Bobur, Doʻrmon, Quyuqqoʻpir, Nazarxon, Xitoy, Choykoʻl, Oʻrta-qalʼa, Qangli, Qilichboy, Qipchoq) bor. Markazi – Mangʻit sh"""
    await message.answer(text)


@dp.message_handler(text='Beruniy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Beruniy_tumani.png/300px-Beruniy_tumani.png')
    text = """Beruniy tumani — Qoraqalpogʻiston Respublikasidagi tuman. 1927 yil 3-iyulda tashkil etilgan (1962-yil 24 dekabrda Toʻrtkoʻl tumaniga qoʻshib yuborilgan, 1964-yil 31-dekabrda qayta tuzilgan). Beruniy tumani Oʻzbekiston Respublikasining shim.gʻarbida, Amudaryoning oʻng sohilida, Beruniy (tuman) shim.sharqda Ellikqalʼa tumani, gʻarbda Amudaryo tumani, shim.gʻarbda Qoraoʻzak va Taxtakoʻpir tumanlari va jan. da Xorazm viloyati. Maydoni 3,94 ming km². Aholisi 94,7 ming kishi (2000). Beruniy (tuman) da 1 shahar (Beruniy) va 11 ovul fuqarolari yigini (Beruniy, Biybozor, Doʻstlik, Navoiy, Ozod, Oltinsoy, Sarkop, Tinchlik, Shabboz, Shimom, Qizilqalʼa) bor. Markazi—Beruniy shahri"""
    await message.answer(text)


@dp.message_handler(text='Qanliko`l')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Qanliko%27l_tumani.png/800px-Qanliko%27l_tumani.png')
    text = """Qanlikoʻl tumani — Qoraqalpogʻiston Respublikasining markaziy qismidagi tuman. 1970-yil 7 dekabrda Qoʻngʻirot va Shumanay tumanlarining qismlaridan tashkil qilingan. Shim.gʻarbdan Qoʻngʻirot, sharqdan Kegeyli, jan.sharqdan Nukus, jan.dan Shumanay tumanlari bilan chegaradosh. Maydoni 0,74-mingkm2. Aholisi 41,2 ming kishi (2005). Tumanda 1 shaharcha (Qanlikoʻl), 4 ovul fuqarolari yigʻini (Beskoʻpir, Kosjop, Navroʻz, Qanlikoʻl) bor. Markazi — Qanlikoʻl shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Qorao`zak')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Qorao%27zak_tumani.png/300px-Qorao%27zak_tumani.png')
    text = """Qoraoʻzak — Qoraqalpogʻiston Respublikasi Qoraoʻzak tumanidagi shaharcha (1984-yildan), tuman markazi. Aholisi 55 ming kishi (2019-yili). Yaqin temir yoʻl stansiyasi va Qoraqalpogʻiston Respublikasi poytaxti Nukus sh.dan (72 km). Paxta tozalash, gʻisht zavodlari, qurilish tashkilotlari, 2 avtokorxona, MTP, savdo, madaniy va maishiy xizmat koʻrsatish shoxobchalari bor. Kichik biznes korxonalari, mikrofirmalar faoliyat koʻrsatadi. 33 Umum taʼlim maktablari, 1 ta bolalar musiqa maktabi, litsey, 2 texnikum, madaniyat uylari, kutubxonalar mavjud."""
    await message.answer(text)


@dp.message_handler(text='Kegeyli')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Kegeyli_tumani.png/300px-Kegeyli_tumani.png')
    text = """Kegeyli tumani - Qoraqalpogʻiston Respublikasidagi tuman. 1928-yil 3 sent.da Chimboy tumanidan ajratib tashkil etilgan. Chimboy, Nukus, Qoraoʻzak, Boʻzatov tumanlari bilan chegaradosh. Mayd. 0,94 ming km2. Aholisi 58,2 ming kishi (2000). K.t.da 1 shahar (Xalq-obod), 1 shaharcha (Kegeyli) va 6 ovul fuqarolari yigʻini (Abat, Janabozor, Jalpaqjap, Kumshunkoʻl, Oqtoʻba, Qiziluy) bor (1998). Markazi — Kegeyli shaharchasi. Kegeyli atamasining kelib chiqishini tuman va Kegeyli shaharchasi hududidan oqib oʻtadigan Kegeyli kanali nomi bilan bogʻlaydilar. Bu kanalning ikki tomoni kegay daraxtlari, turangʻillar bilan burkanib turganligi uchun u Kegeyli nomini olgan deyiladi. Ushbu nom keyinchalik shaharcha va tuman nomiga aylangan"""
    await message.answer(text)


@dp.message_handler(text='Qo`ng`irot')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Qo%27ng%27irot_tumani.png/300px-Qo%27ng%27irot_tumani.png')
    text = """Qoʻngʻirot tumani - Qoraqalpogʻiston Respublikasidagi tuman. 1927-yil 3 iyulda tashkil etilgan. 1963-yil Xoʻjayli tumaniga qoʻshib yuborilgan. 1964-yil 22 fevraldan qayta tuzilgan. Shim -sharqdan Moʻynoq tumani, sharqdan Amudaryo orqali Boʻzatov, jan.-sharkdan Qanlikoʻl, Shumanay tumanlari, jan.dan Turkmanistonning Toshhovuz viloyati, gʻarb va shim.dan Qozogʻiston Respublikasining Aterov va Oqtoʻba viloyatlari bilan chegaradosh. Maydoni 74,49 ming km2. Hududi jihatidan Qoraqalpogʻiston Respublikasi tumanlari ichida eng kattasi. Aholisi 113,2 ming kishi (2005). Tumanda 1 shahar (Qoʻngʻirot), 6 shaharcha (Jasliq, Oltinkoʻl, Oqshoʻlaq, Elobod, Qoraqalpogʻiston, Qubla-Ustyurt), 9 qishloq fu-qarolari yigʻini (Ajiniyoz, Navroʻz, Ornek, Ravshan, Suelli, Ustyurt, Xorazm, Qipchoq. Qoʻngʻirot). Markazi — Qoʻngʻirot shahri"""
    await message.answer(text)


@dp.message_handler(text='Mo`ynoq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mo%27ynoq_tumani.png/300px-Mo%27ynoq_tumani.png')
    text = """Moʻynoq tumani - Qoraqalpogʻiston Respublikasining shimolidagi tuman. 1931-yil 19-sentabrda tashkil etilgan. Amudaryo deltasi, Orol dengizining janubidagi hududlarni egallaydi. Qoraoʻzak, Chimboy, Boʻzatov tumanlari, Krzogʻiston Respublikasining Oqtoʻba, Qiziloʻrda viloyatlari bilan chegaradosh. Maydoni 37,94 ming km². Aholisi 28,8 ming kishi (2003). Tumanda 5 ovul fukarolari yigʻini (Boʻzatov, Madali, Tikoʻzak, Uchsoy, Qozoqdaryo), 1 shahar (Moʻynoq) bor. Markazi — Moʻynoq shahri Tabiati. Tuman hududining aksari qismi Orol dengizining qurigan tubi (Orolqum) va Amudaryo deltasidagi kullardan iborat. Tumanning xoʻjalik va madaniy markazi — Moʻynoq shahri."""
    await message.answer(text)


@dp.message_handler(text='Taxtako`pir')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Taxtako%27pir_tumani.png/300px-Taxtako%27pir_tumani.png')
    text = """Taxtakoʻpir tumani - Qoraqalpogʻiston Respublikasidagi tuman. 1928-yil may oyida tashkil qilingan. 1963-yil Taxtakoʻpir tumani tugatilib, Chimboy tumaniga birlashtirilgan. 1965-yil oʻz nomi bilan Chimboy tumanidan ajralib chiqqan.
Taxtakoʻpir tumani janubdan Beruniy, jan,sharqsan Ellikqalʼa, gʻarbdan Qoraoʻzak, shim.gʻarbdan Moʻynoq tumani, shim.sharqdan Qozogʻiston Respublikasi va sharqsan Navoiy viloyati bilan chegaradosh. Maydoni 21,1 ming km². Aholisi 42,6 ming kishi (2004). Tumanda 1 shaharcha (Taxtakoʻpir), 8 ovul fuqarolar yigʻini (Beltov, Janadaryo, Mulik, Otakoʻl, Taxtakoʻpir, Qoraoy, Qorateran, Qoʻngʻirotkoʻl) bor. Markazi — Taxtakoʻpir shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Ellikqal`a')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Ellikqal%27a_tumani.png/300px-Ellikqal%27a_tumani.png')
    text = """Ellikqalʼa tumani — Qoraqalpogʻistondagi tuman. 1977-yil 23-martda tashkil etilgan. Shim.dan Qozogʻiston Respublikasining Qiziloʻrda viloyati, gʻarbdan Beruniy, Taxtakoʻpir, jan. dan Toʻrtkoʻl tumani, sharqdan Navoiy viloyati, janubi-gʻarbdan Xorazm viloyati bilan chegaradosh. Maydoni 5,4 ming km². Aholisi 119,1 ming kishi (2004). Tumanda 1 shahar (Boʻston), 12 qishloqfuqarolari yigʻini (Amirobod, Guldursun, Guliston, Navoiy, Oqchakoʻl, Saribiy, Tozabogʻ, Sharq Yulduzi, Ellikqalʼa, Qizilqum, Qilchinoq, Qirqqiz) bor. Markazi — Boʻston shahri."""
    await message.answer(text)


@dp.message_handler(text='To`rtko`l')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/To%27rtko%27l_tumani.png/300px-To%27rtko%27l_tumani.png')
    text = """Toʻrtkoʻl tumani (qoraqalpoqcha: Toʻrtkuʼl rayonı, Төрткүл районы) — Qoraqalpogʻiston Respublikasidagi tuman. 1927-yil 3-iyulda tashkil etilgan. Gʻarbdan Ellikqalʼa tumani, janubi-gʻarbdan Xorazm, sharqdan Navoiy va Buxoro viloyatlari bilan chegaradosh. Maydoni — 7,5 ming km2. Aholisi — 161,2 ming kishi (2004). Tumanda 1 shahar (Toʻrtkoʻl), 14 qishloq (ovul) fuqarolari yigʻini (A. Durdiyev, Jambasqala, Kaltaminor, Koʻkcha, Otauba, Oxunboboyev, Oqboshli, Oqqamish, Paxtachi, Tozabogʻyop, Ullubogʻ, Chubukli, Shoʻraxon, Qumboskan) bor. Markazi — Toʻrtkoʻl sh.."""
    await message.answer(text)


@dp.message_handler(text='Xo`jayli')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Xo%27jayli_tumani.png/300px-Xo%27jayli_tumani.png')
    text = """Xoʻjayli tumani — Qoraqalpogʻiston Respublikasidagi tuman. 1926 yil 14 yanvarda tashkil etilgan. Amudaryoning chap sohilida joylashgan. Shimolidan Nukus, janubi-sharkdan Qoraoʻzak, shim.gʻarbdan Qanlikoʻl, Shumanay tumanlari, gʻarb va janubidan Turkmanistonning Koʻhna Urganch tumani bilan chegaradosh. Maydoni 0,85 ming km². Aholisi 146,4 mint kishi (2004). Tumanda 9 ovul fuqarolari yigʻini (Amudaryo, Begjap, Janajap, Kenagas, Koʻlob, Naymankoʻl, Saroykoʻl, Sarichunkoʻl, Somonkoʻl), 1 shahar (Xoʻjayli), 1 shaharcha (Vodnik) bor. Markazi – Xoʻjayai shahri."""
    await message.answer(text)


@dp.message_handler(text='Chimboy')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Chimboy_tumani.png/1280px-Chimboy_tumani.png')
    text = """Chimboy tumani - Qoraqalpogʻiston Respublikasidagi tuman. 1927-yil 3-iyulda tashkil etilgan. Shim,gʻarbdan Moʻynoq, gʻarbdan Boʻzatov va jan.dan Kegeyli, sharq va shim.sharqdan Qoraoʻzak, tumanlari bilan chegaradosh. Maydoni 3 ming km². Aholisi 92,8 ming kishi (2004). Tumanda 8 ovul fuqarolari yigʻini (Baxtli, Kenes, May, Mayjap, Tagjap, Tozajoʻl, Qiziloʻzek, Qoʻsterek) bor. Markazi — Chimboy shahri"""
    await message.answer(text)

@dp.message_handler(text='Shumanay')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Shumanay_tumani.png/1280px-Shumanay_tumani.png')
    text = """Shumanay tumani - Qoraqalpogʻiston Respublikasidagi tuman. 1950-yil 6 oktyabrda tashkil etilgan. 1960-yil 5 fevralda Qoʻngʻirot va Xoʻjayli tumanlariga qoʻshib yuborilgan edi. 1976-yil 9 yanvarda qayta tashkil etildi. Sharqdan Xoʻjayli, Qanlikoʻl, shim. va gʻarbdan Qoʻngʻirot tumanlari, jan.dan Turkmaniston bilan chegaralangan. Maydoni 0,64 ming km². Aholisi 41,4 ming kishi (2003). Tumanda 1 shahar (Shumanay), 6 ovul fuqarolari yigʻini (Birleshiq, Dehqonobod, Ketenlar, Mamiy, Oqjap, Sarmonboykoʻl) bor. Tuman markazi — Shumanay shahri."""
    await message.answer(text)



# FARGONA VILOYATI



@dp.message_handler(text='Oltiariq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Oltiariq_tumani.png/300px-Oltiariq_tumani.png')
    text = """Oltiariq tumani - Fargʻona viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Jan.dan Fargʻona, shim.dan Namangan viloyati, gʻarb va shim.gʻarbdan Rishton, Buvayda hamda Bagʻdod, shim.-sharkdan Oxunboboyev, Yozyovon tumanlari va jan.dan Qirgʻizistonning Qadamjoy tumani bilan chegaradosh. Maydoni 0,63 ming km². Aholisi 166 ming kishi (2003). Oltiariq tumanida 1 shahar (Tinchlik), 1 shaharcha (Oltiariq), 15 qishloq fuqarolari yigʻini (Azimobod, Bo'rbaliq, Joʻrak, Zilxa, Katput, Oltiariq, Oqboʻyra, Povulgʻon, Polosoy, Fayziobod, Yangiarab, Yangiqoʻrgʻon, Qapchigʻay, Qiziltepa, Eskiarab) bor. Markazi — Oltiariq shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Bagʻdod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Bag%27dod_tumani.png/1280px-Bag%27dod_tumani.png')
    text = """Bagʻdod tumani — 1926-yilning 29-sentabrida tashkil topgan. Tuman Fargʻona viloyatining markaziy hududida joylashgan boʻlib, 333,3 km. kv maydonni egallaydi[1]. Chegaralarining umumiy uzunligi: 98,1 km. Janubdan Rishton (34,2 km), sharqdan Oltiariq (21,2 km), shimoldan Buvayda (19,5 km), gʻarbdan Uchko'prik (23,2 km) tumanlari bilan chegaradosh. Tuman hududidan „Qoʻqon-Andijon-Qoʻqon[sayt ishlamaydi] “ yoʻnalishi boʻyicha harakatlanuvchi temir yoʻl oʻtgan. Markazi — Bagʻdod shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Beshariq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Beshariq_tumani.png/300px-Beshariq_tumani.png')
    text = """Beshariq tumani — Fargʻona viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Fargʻona viloyatining Oʻzbekiston va Furqat tumanlari, Tojikistonning Konibodom va Asht tumanlari bilan chegaradosh. Maydoni 0,77 ming km2. Aholisi 175,9 ming kishi (2012). Beshariq tumanida 1 shahar (Beshariq) va 8 qishloq fuqarolari yigʻini (Andarxon, Beshariq, Vatan, Rapqon, Tovul, Yakkatut, Qashqar, Qorajiyda) bor. Markazi — Beshariq shahri."""
    await message.answer(text)

@dp.message_handler(text='Buvayda')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Buvayda_tumani.png/1280px-Buvayda_tumani.png')
    text = """Buvayda tumani — Fargʻona viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. 1959-yil 14-dekabrda tugatilib, uning hududi Uchkoʻprik va Bagʻdod tumanlariga qoʻshib yuborilgan. 1973-yil 26-dekabrda qayta tuzildi. Tuman hududi Qoʻqon shahridandan shimolroqsa joylashgan. Buvayda tumani viloyatning Bagʻdod, Uchkoʻprik, Dangʻara, Oltiariq tumanlari, Namangan viloyatining Pop tumani bilan chegaradosh. Maydoni 0,28 ming km2. Aholisi 173,6 ming kishidan ziyod (2011). Buvayda tumanida 11 qishloq fuqarolari yigʻini (Alqor, Bekobod, Beshterak, Buvayda, Jaloyir, Oqqoʻrgʻon, Uzumzor, Yangiqadam, Yangiqoʻrgʻon, Qoʻngʻirot, Qoʻrgʻonobod) bor. Markazi — Ibrat (Yangiqoʻrgʻon) qishlogʻi.Buvayda nomi Bibiubayda nomidan olingan"""
    await message.answer(text)


@dp.message_handler(text='Dangʻara')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Dang%27ara_tumani.png/1280px-Dang%27ara_tumani.png')
    text = """Dangʻara tumani — Fargʻona viloyatidagi tuman. 1939-yil 10 fevralda tashkil etilgan (1962-yil 24 dek.da Pop tumani bilan birlashtirilgan. 1970-yil 7 dekabrda qayta tuzilgan). Dangʻara tumani viloyatning Buvayda, Uchkoʻprik, Oʻzbekistan, Furqat tumanlari, Qoʻqon sh., Namangan viloyatining Pop tumani, Tojikiston Respublikasining Asht tumani bilan chegaradosh. Mayd. 0,45 ming km2. Aholisi 160,9 ming kishi (2016). Dangʻara tumanida 1 shaharcha (Dangʻara), 49 ta maxalla fuqarolari yigʻini mavjud. Markazi — Dangʻara shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Fargʻona')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Farg%27ona_tumani.png/300px-Farg%27ona_tumani.png')
    text = """Fargʻona tumani — Oʻzbekiston Respublikasining Fargʻona viloyatidagi tuman. 1926-yil 29-sentabrda tashkil qilingan. 1962-yil 24-dekabrda Quva tumaniga qoʻshib yuborilgan. 1964-yil 22-fevralda qayta tuzilgan. Shim.dan Margʻilon va Fargʻona shaharlari, sharqdan Quva tumani va Quvasoy shahri, jan.sharq va jan.dan Qirgʻiziston Respublikasi, shim.gʻarbdan. Oltiariq tumani bilan chegaradosh. Maydoni 0,62 ming km². Aholisi 168,5 ming kishi (2004). Tumanda 2 ta shaharcha ( Vodil va Chimyon), 13 fuqarolar yigʻini (Avval, Gulshan, Damkoʻl, Vodil, Kaptarxona, Logʻon, Soyboʻyi, Mindon (30 maktabda oʻqiganman), Navkat, Oqbilol, Xonqiz, Chekshoʻra, Chimyon) bor. Tuman markazi – Vodil shaxarchasi."""
    await message.answer(text)


@dp.message_handler(text='Furqat')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Furqat_tumani.png/1280px-Furqat_tumani.png')
    text = """Furqat tumani – Fargʻona viloyatidagi tuman. 1992-yil 9-aprelda tashkil etilgan. Shim.dan Tojikiston Respublikasi va Dangʻara tumani, gʻarbdan Beshariq, janubiy va sharkdan Oʻzbekiston tumanlari bilan chegaradosh. Maydoni 0,31 ming km². Aholisi 88,7 ming kishi (2003). Tumanda shaharcha va qishloq fuqarolari yigʻini (Navbahor, Qushchi, Qizil qiyoq, Tomosha, Jangketmon, Qulbobo, Eshon shaharcha, Toʻrgʻay qishloq, Gʻirri qishloq, Kichik yangi qishloq, Katta yangi qishloq, Koʻk doʻppi qishloq, Xayit qishloq, Shunqor qishloq, Qoʻqonboʻy, Gʻallakor, Gʻuncha va h.k") bor. Markazi – Navbahor shahar. Aholisi, asosan, oʻzbeklar, shuningdek, tojik, tatar, rus, qirgʻiz va boshqa millat vakillari ham yashaydi. Aholining oʻrtacha zichligi 1 km² ga 286,1 kishi (2003)."""
    await message.answer(text)


@dp.message_handler(text='Qoʻshtepa')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Qo%27shtepa_tumani.png/300px-Qo%27shtepa_tumani.png')
    text = """Qoʻshtepa tumani (1943-yilgacha Margʻilon tumani) — Fargʻona viloyatidagi tuman. 1926-yilda tashkil etilgan. Keyinchalik tuman hududidan Toshloq, Yozyovon kabi yangi tumanlar ajralib chiqqan. Gʻarbdan Oltiariq, janubdan Fargʻona, shimoldan Yozyovon, sharqdan Toshloq tumanlari va Margʻilon shahri bilan chegaradosh. Maydoni 0,39 ming km². Aholisi 195,3 ming kishi (2020). Qoʻshtepa tumanida 18 ta qishloq fuqarolari yigʻini (Boltalikoʻl, Doʻrmon, Yoʻldoshobod, Langar, Loyson, Oxunboboyev, Paxtakor, Sarimozor, Solijonobod, Surxtepa, Xalqobod, Shahartepa, Oʻqchi, Koraqushchi, Qumtepa, Gʻishtmon,Qayrag'och,Nurafshon bor). Markazi Langar- Shaharchasi"""
    await message.answer(text)


@dp.message_handler(text='Quva')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Quva_tumani.png/300px-Quva_tumani.png')
    text = """Quva tumani — Oʻzbekiston Respublikasining Fargʻona viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Janubiy-gʻarbdan Fargʻona, shimoliy-gʻarb va gʻarbdan Toshloq tumanlari, shimol va sharqdan Andijon viloyatining Boʻz, Shahrixon, Asaka, Marhamat tumanlari, janubiy-sharq va janubdan Qirgʻizistonning Oʻsh viloyati bilan chegaradosh. Maydoni 440 km². Aholisi: 261,000 kishi (2021). Tumanda 65 ta mahalla fuqarolari yigʻini bor. Markazi – Quva shahri."""
    await message.answer(text)


@dp.message_handler(text='Rishton')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Rishton_tumani.png/300px-Rishton_tumani.png')
    text = """Rishton tumani — Fargʻona viloyatidagi tuman. 1926-yil 29 sentabrda tashkil etilgan. 1959-yil 7 martda Soʻx tumani bilan birlashtirilgan. 1990-yil 27 fevralda Soʻx tumani ajralib chiqqan. Shim.dan Bagʻdod, jan.sharqsan Oltiariq, gʻarbdan Oʻzbekiston va Uchkoʻprik tumanlari, janubdan Qirgʻiziston bilan chegaradosh. Maydoni 0,42,1 ming km². Aholisi 150.2 ming kishi (2003). Tumanda 1 shahar (Rishton), 11 qishloq fuqarolari yigʻini (Beshkapa, Buzrukxoʻja Usmonxoʻjayev, Boʻston, Yoyilma, Zoxidon, Mehnatobod, Oqoltin, Oqyer, Rishton, Toʻda, Qayragʻoch) bor. Markazi — Rishton shahri."""
    await message.answer(text)


@dp.message_handler(text='Soʻx')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/So%27x_tumani.png/300px-So%27x_tumani.png')
    text = """Soʻx tumani — Oʻzbekiston Respublikasining Fargʻona viloyatidagi tuman. 1942-yil iyulda tashkil etilgan. 1959-yil 7 martda Rishton tumaniga qoʻshib yuborildi. 1990-yil 27 fevralda qaytadan tuzilgan. Qirgʻiziston bilan chegaradosh. Maydoni 0,22 ming km². Aholisi 51569 kishi (2003). Tumanda 4 qishloq fuqarolari yigʻini (Oxunboboyev, Ravon, Soʻx, Xushyor) bor. Markazi — Ravon qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Toshloq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Toshloq_tumani.png/300px-Toshloq_tumani.png')
    text = """Toshloq tumani — Fargʻona viloyatidagi tuman. 1935-yilda tashkil etilgan. 1959-yilda Oxunboboyev tumaniga birlashtirilgan. 1973-yil 12-aprelda qayta tiklangan. Gʻarbdan Margʻilon shahri, shimoli-gʻarbdan Qo'shtepa, Yozyovon, sharqdan Quva tumanlari, jananubi-sharqdan Quvasoy shahri va shimoli-sharqdan Andijon viloyati Boʻz tumani bilan chegaradosh. Maydoni 0,24 ming km². Aholisi 208,7 ming kishi, shundan shahar aholisi - 48,2 ming kishi, qishliq aholisi - 160,4 ming kishi (2021-yil 1-oktyabr). Tumanda 1 ta shaharcha (Toshloq), 51 ta Mahalla fuqarolari yigʻini (Nayman, Chek, Istiqlol, Xonariq, Mehnatobod, Naymanbo'ston, Quyi Yakkatut, Soy bo'yi, Ucholish, Guzarboshi, Xo'jaariq, Zarkent, Yangi Yo'l, Yuqoriqishloq, Chuqurqishloq, Jarqishloq, Turvat, Qumariq, Obisiyo, Farog'at, Qumqishloq, Sadda, Teraktagi, Konizar, Katta ko'cha, So'filar, So'kchilik, Axshak, Xotinqumi, Yakkovut, Axshakguzar, Qanjirg'a, Tog'liq, Arabmozor, Ko'lariq, Xonaqa, Besarang, Aylanmajar, Toshloq, Shodlik, Furqat, Do'stlik, Suvboshi, Qamchipurush, Qo'rg'oncha, Piyozchilik, Xamrak, Varzak, Qipchoqariq, O'zbekiston, Bo'ston) bor.[1]. Tuman markazi – Toshloq shaharchasi"""
    await message.answer(text)


@dp.message_handler(text='Uchkoʻprik')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Uchko%27prik_tumani.png/1280px-Uchko%27prik_tumani.png')
    text = """Uchkoʻprik tumani — Fargʻona viloyatidagi tuman. 1926-yil 29 sentabrda tashkil etilgan. 1962-yil 24 dekabrda Bagʻdod tumani bilan qoʻshib yuborildi. 1964-yil 31 dekabrda qayta tuziddi. Sharqdan Bagʻdod, Buvayda, shim. va gʻarbdan Dangʻara, Qoʻqon shahri, gʻarb va janubi-gʻarbdan Oʻzbekiston jan.sharkdan Rishton tumanlari bilan chegaradosh. 0,28 ming km². Aholisi 164 ming kishi (2004). Tumanda 9 qishloq fuqarolari yigʻini (Kenagas, Mehnatobod, Navroʻz, Poloxon, Sariqoʻrgʻon, Uchqoʻrgʻon, Chorbogʻ, Yangiqishloq, Gʻozigʻijdon) bor. Markazi — Uchkoʻprik qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Oʻzbekiston')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/O%27zbekiston_tumani.png/300px-O%27zbekiston_tumani.png')
    text = """Oʻzbekiston tumani — Fargona viloyatidagi tuman. 1926-yil 29-sentabr da tashkil etilgan. 1962-yil 24 dekabrda tugatilgan, 1963-yil 17-aprelda qayta tuzilgan. Shim.dan Qoʻqon shahri, Furqat tumani, jan. va gʻarbdan Tojikiston Respublikasi, shim.gʻarbdan Beshariq, sharqdan Uchkoʻprik tumanlari, jan.sharqda Rishton tumani va Qirgʻiziston Respublikasi bilan chegaradosh. Maydoni 0,69 ming km². Aholisi 181,1 ming kishi (2005). Oʻzbekiston tumanida 1 shahar (Yaypan), 1 shaharcha (Shoʻrsuv), 10 qishloq fuqarolari yigʻini (Konizar, Mingtut, Nursuq, Ovchi, Oxunboboyev, Rajabgardi, Tagob, Qaynar, Qizilqaqir, Gʻaniobod) bor. Markazi — Yaypan shahri"""
    await message.answer(text)


@dp.message_handler(text='Yozyovon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Yozyovon_tumani.png/300px-Yozyovon_tumani.png')
    text = """Yozyovon tumani — Fargʻona viloyatidagi tuman. 1952 yil 16 aprelda tashkil etilgan (1959 yil 14 dekabrda Toshloq tumani bilan birlashtirilib Oxunboboyev nomi berilgan, 1962 yil 24 dekabrda Oxunboboyev tumaniga Margʻilon tumani ham qoʻshilgan. 1980 yil 27 dekabrda Yozyovon tumani qayta tuzildi). Yozyovon tumani viloyatning Toshloq, Oxunboboyev, Oltiariq, Buvayda tumanlari, Namangan viloyatining Pop tumani, Andijon viloyatining Ulugʻnor, Boʻz tumanlari bilan chegaradosh. Maydon 0,41 ming km2. Aholisi 71,6 ming kishi (2000). Yozyovon tumanida 1 shaharcha (Yozyovon), 10 qishloq fuqarolari yigʻini (Guliston, Yozyovon, Ishtirxon, Xonobod, Choʻliguliston, Yangiboʻston, Yangiobod, Qatortol, Qorasoqol, Qoratepa) bor. Markazi — Yozyovon shaharchasi. """
    await message.answer(text)


@dp.message_handler(text='Chiroqchi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chiroqchi_tumani.png/300px-Chiroqchi_tumani.png')
    text = """Chiroqchi — Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman. Hududi 2.8 ming km2. Aholisi 445.5 ming kishi.[2] Shimolda Samarqand viloyatining Nurobod va Pastdargʻom tumanlari, gʻarbda Koson tumani, sharqda Shahrisabz va Yakkabogʻ tumanlari, janubda esa Qamashi, Gʻuzor va Qarshi tumanlari bilan chegaradosh. Tuman hududida Chimqoʻrgʻon va Qalqama suv omborlari mavjud. Markazi — Chiroqchi shahri. Tumanda 33 ta mahalla va 20 ta qishloq fuqarolar yigʻinlari (Dam, Dodiq, Jar, Koʻkdala, Langar, Mirzatoʻp, Oxunboboyev, Paxtaobod, Torjilgʻa, Oʻymovut, Uyshun, Humo, Chim, Chorvador, Shoʻrquduq, Eski Anhor, Yangi Hayot, Qalqama, Qahramon, Qumdaryo) faoliyat yuritgan. 2022-yil 17-martda ulardan ayrimlari Koʻkdala tumaniga oʻtkazilgan."""
    await message.answer(text)


@dp.message_handler(text='Dehqonobod')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Dehqonobod_tumani.png/300px-Dehqonobod_tumani.png')
    text = """Dehqonobod tumani – Oʻzbekiston Respublikasining Qashqadaryo viloyatida joylashgan boʻlib, 1926 yil 29 sentabr da tashkil etilgan (1962 yil 24 dekabrda Gʻuzor tumani bilan birlashtirilgan. 1971 yil 31 avgustda qayta tuzildi). Dehqonobod tumani viloyatning janubi-sharqida joylashgan. Shim.-gʻarbda Gʻuzor tumani, shimoli-sharqda Qamashi tumani, janubi-sharqda Surxondaryo viloyati, gʻarbda Turkmaniston bilan chegaradosh. Maydoni 4,0 ming km2. Aholisi 100,3 ming kishi (2000). Dehqonobod tumanida 1 ta shaharcha (Qarashina), 14 qishloq fuqarolari yigʻini (Beshqoʻton, Bibiqorasoch, Bozortepa, Boshchorboq, Duob, Qarashina, Obiravon, Oqirtma, Oqrabot, Oqtosh, Oqqishloq, Qizilcha, Qirqquloch, Qoʻrgʻontosh) bor. Markazi – Qarashina shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='G`uzor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/G%27uzor_tumani.png/1280px-G%27uzor_tumani.png')
    text = """Gʻuzor tumani - Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Shimolidan Qamashi, Chiroqchi, sharqdan Dehqonobod, gʻarbdan Qarshi va Nishon tumanlari, janubida 25 km masofada Turkmaniston bilan chegaradosh. Maydoni 2,62 ming km2. Aholisi 207,6 ming kishi (2021). Tumanda 1 ta shahar (Gʻuzor), 12 qishloq fuqarolari yigʻini (Batosh, Boʻston, Guliston, Gulshan,Mehnatobod, Pachkamar,Qorapul, Qoʻshtepa Xalqobod, Shakarbuloq, Sherali, Zarbdor) bor. Markazi — Gʻuzor shahri."""
    await message.answer(text)


@dp.message_handler(text='Kasbi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Kasbi_tumani.png/1280px-Kasbi_tumani.png')
    text = """Kasbi tumani – Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman. 1970-yil 16 oktabrda tashkil etilgan. Kasbi tumani viloyatning gʻarbida joylashgan. Qarshi, Koson, Nishon, Muborak, Bahoriston, Usmon Yusupov tumanlari bilan chegaradosh. Maydon 0,65 ming km2. Aholisi 127,6 ming kishi (2000). Kasbi tumanida 12 qishloq fuqarolari yigʻini (Talishbe,Denov, Komilon, Mugʻlon, Toshqoʻrgʻon, Chovqay, Choʻlquvar, Yuksalish, Yangihayot, Qamashi, Katagʻon,Mesit,Maymanoq) bor. Markazi – Mugʻlon qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Kitob')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Kitob_tumani.png/1280px-Kitob_tumani.png')
    text = """Kitob tumani - Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman. Viloyatning shimoli-sharqida. 1926-yil sentabrda tashkil etilgan. 1962-yil 24-dekabrda Shahrisabz tumani bilan birlashtirilgan. 1968-yil 25-dekabrda qayta toʻzildi. Viloyatning Chiroqchi, Shahrisabz tumanlari, Samarqand viloyati va Tojikiston bilan chegaradosh. Maydoni 1,75 ming km². Aholisi 178,9 ming kishi (2000). Kitob tumanida 1 shahar (Kitob) va 12 ta qishloq fuqarolari yigʻini (Bektemir, Beshterak, Bogʻbon, Makrid, Palandara, Paxtaobod, Sivaz, Toʻpchoq, Qaynarbuloq, Katorbogʻ, Quynoqboy, Jilisuv) bor (2000). Markazi — Kitob shahri Tuman hududidan Katta Oʻzbekiston trakti oʻtgan. Taxtaqoracha dovoni (balandligi 1788 m) esa respublika janubini shimoliy viloyatlar bilan bogʻlaydi."""
    await message.answer(text)


@dp.message_handler(text='Koson')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Koson_tumani.png/300px-Koson_tumani.png')
    text = """Koson tumani - Oʻzbekiston Respublikasining Qashqadaryo viloyatida joylashgan tuman. 1926-yil 29-sentabr da tashqil etilgan. Samarqand viloyati, Muborak, Qarshi, Kasbi tumanlari bilan chegaradosh. Maydoni 1,88 ming km². Aholisi 197,1 ming kishi (2003). Koson tumanida 1 shahar (Koson) va 9 qishloq fuqarolari yigʻini (Boʻlmas, Guvalak, Gulbogʻ, Doʻstlik, Koson, Obidida, Olachabob, Poʻloti, Tinchlik) bor (2003). Markazi — Koson shahri"""
    await message.answer(text)


@dp.message_handler(text='Mirishkor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Mirishkor_tumani.png/300px-Mirishkor_tumani.png')
    text = """Mirishkor tumani — Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman. 2003-yil 6-yanvarida Usmon Yusupov va Bahoriston tumanlarining birlashtirilishi natijasida tashkil etilgan. Mirishkor tumani Qashqadaryo viloyatining janubi-gʻarbida joylashgan. Tuman shimoldan Muborak, sharqdan Kasbi, Qarshi, Nishon tumanlari, gʻarbdan Buxoro viloyatining Olot va Qorakoʻl tumanlari, janubdan Turkmanistonning Lebap viloyati bilan chegaradosh. Mirishkor tumanida 12 fuqarolar yigʻini (Avazchoʻl, Vori, Guliston. Gulshanbogʻ, Jeynov, Mirishkor, Navbahor, Obod, Pomuq, Chamanzor, Chandir, Yangiobod) bor. Maydoni 3,1 ming km2. Mirishkor tumani hududi jihatidan Qashqadaryo viloyatida 3 oʻrinda turadi. Aholisi 119,150 kishi (2020-yil 1-yanvar). Eng yirik aholi punti -Jeynov shaharchasi (26,4 ming kishi) Tuman markazi - Yangi Mirishkor qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Muborak')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Muborak_tumani.png/300px-Muborak_tumani.png')
    text = """Muborak tumani - Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman. 1978-yil 13-sentabrda tashkil etilgan. Gʻarbda Buxoro viloyati, shimolida Navoiy va Samarqand viloyatlari, sharqda viloyatning Koson tumani, janubida Kasbi va Mirishkor tumanlari bilan chegaradosh. Maydoni 3,07 ming km². Aholisi 62 ming kishiga yaqin (2003). Tumanda 4 qishloq fuqarolar yigʻini (Muborak, Sariq, Qarluk, Qoraqum), 1 shahar (Muborak) bor. Tuman markazi — Muborak shahri"""
    await message.answer(text)


@dp.message_handler(text='Nishon')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Nishon_tumani.png/300px-Nishon_tumani.png')
    text = """Nishon tumani - Qashqadaryo viloyatidagi tuman. 1975-yil 6-martda tashkil etilgan. Janubida Turkmaniston, shimolida viloyatning Qarshi, sharqda Gʻuzor, gʻarbda Kasbi tumanlari bilan chega-radosh. Maydoni 2,1 ming km². Aholisi 155 ming kishi (2021). Nishon tumanida 2 shahar (Tallimarjon va Yangi Nishon), 1 shaharcha (Nuriston), 8 qishloq fuqarolar yigʻini (Balxiyak, Nishon, Navroʻz, Oydin, Oqoltin, Paxtazor, Qirkdu-loch, Shirinobod) bor. Tuman markazi — Yangi Nishon shahri"""
    await message.answer(text)


@dp.message_handler(text='Qamashi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Qamashi_tumani.png/300px-Qamashi_tumani.png')
    text = """Qamashi tumani — Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman, 1937-yil 29-sentabrda tashkil etilgan. 1962-yil 24-dekabrda Qarshi tumaniga qoʻshilgan. 1964-yil 31-dekabrda yana qaytadan tashkil etilgan. Shimoliy dan Chiroqchi, Yakkabog, Shahrisabz tumanlari, gʻarbdan Koson tumani, janubiy dan Gʻuzor, Dehqonobod tumanlari, sharqdan Surxondaryo viloyatining Boysun tumani bilan chegaradosh. Maydoni 2,66 ming km2. Aholisi 191,4 ming kishi (2005). Tumanda 11 qishloq fuqarolari yigʻini (Yortepa, Jonbuzsoy, Koʻkbuloq, Laylaksoy, Oqravot, Toʻqboy, Chim, Qamay, Qiziltepa, Korabogʻ, Qoratepa), 41 ta mahalla fuqarolar yigʻini bor. Markazi — Qamashi shahri."""
    await message.answer(text)


@dp.message_handler(text='Qarshi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Qarshi_tumani.png/300px-Qarshi_tumani.png')
    text = """Qarshi tumani — Oʻzbekiston Respublikasining Qashqadaryo viloyatidagi tuman, 1931-yil 1-oktabr da tashkil etilgan. Shimoliy dan Koson, shimoli-sharqdan Chiroqchi, sharqdan Qamashi, Gʻuzor, janubiy dan Nishon, gʻarbdan Kasbi tumanlari bilan chegaradosh.. Maydoni 0,9 ming km2. Aholisi 177 ming kishi (2005). Tumanda 1 shahar (Beshkent), 15 ta qishloq fuqarolari yigʻini (Bogʻobod, Dasht, Yertepa, Kat, Kojar, Nuqrobod, Paxtakor, Poshton, Talliqoʻrgʻon, Xonobod, Charogʻil, Choʻliboʻston, Qovchin, Qoratepa, Hilol) bor. Markazi — Beshkent shahri."""
    await message.answer(text)


@dp.message_handler(text='Shahrisabz')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Shahrisabz_tumani.png/1280px-Shahrisabz_tumani.png')
    text = """Shahrisabz tumani - Qashqadaryo viloyatidagi tuman. 1926-yil 29 sentyabrda tashkil etilgan. Shimolidan Kitob tumani, sharqdan Tojikiston, Surxondaryo viloyati, janubidan Yakkabogʻ, Qamashi, gʻarbdan Chiroqchi tumanlari bilan chegaradosh. Maydoni 1,70 ming km². Aholisi 272,4 ming kishi (2004). Tumanda 1 shahar (Shahrisabz): 1 shaharcha (Miroqi), 12 ta qishloq fuqarolar yigʻini (Dukchi, Kunchiqar, Moʻminobod, Naʼmaton, Oqsuv, Toʻdamaydon, Xitoy, Shakarteri, Shamaton, Oʻzbekiston, Qutchi, Hisorak) bor. Markazi — Shahrisabz shahri."""
    await message.answer(text)


@dp.message_handler(text='Yakkabog`')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Yakkabog%27_tumani.png/300px-Yakkabog%27_tumani.png')
    text = """Yakkabogʻ tumani — Qashqadaryo viloyatidagi tuman. 1926-yil 29-sentyabrda tashkil etilgan. Yakkabogʻ tumani turli yillarda Shahrisabz, Chiroqchi, Qamish tumanlariga qoʻshilgan. Keyin yana ajratilgan. Shimoldan Chiroqchi, Shahrisabz, sharq, gʻarb va janubdan Qamashi tumanlari bilan chegaradosh. Maydoni 1,3 ming km2. Aholisi 204,9 ming kishi (2011). Tumanda 1 shahar (Yakkabogʻ)[2], 2 shaharcha (Eski Yakkabogʻ, Mevazor), 9 qishloq fuqarolari yigʻini (Samoq, Sandal, Xiyobon, Chaydari, Esat, Oʻrta, Qayragʻoch, Qishlik, Qoʻshchinor) bor. Tuman markazi – Yakkabogʻ shahri"""
    await message.answer(text)


@dp.message_handler(text='Konimex')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Konimex_tumani.png/300px-Konimex_tumani.png')
    text = """Konimex tumani — Navoiy viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Konimex tumani viloyatning shimoli-gʻarbida joylashgan. Sharqdan Navbahor, shimoli-sharqdan Nurota, gʻarbdan Tomdi, Uchquduq, janubdan Qiziltepa tumanlari, gʻarbdan Buxoro viloyatining Gʻijduvon, Peshku tumanlari bilan chegaradosh. Maydoni 15,5 ming km2. Aholisi 36,9 ming kishi (2002). Tumanda 1 shaharcha (Konimex), 7 qishloq fuqarolari yigʻini (Boymurot, Sarjal, Uchtepa, Chordara, Yangiobod(Sho'rko'l), Yangiqazgan, Karaqota) bor. Markazi Konimex shaharchasi."""
    await message.answer(text)


@dp.message_handler(text='Karmana')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Karmana_tumani.png/300px-Karmana_tumani.png')
    text = """Karmana tumani - Navoiy viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. Zarafshon daryosining quyi qismi sohilida joylashgan.
1962-yildan Navoiy tumani deb yuritilgan. 1980-yilda Navoiy tumanidan Navbahor tumani ajralib chiqqan. 1988-yilda qayta qoʻshilgan. 1992-yildan yana alohida tuman boʻlgan. 1999-yil Karmana shahri hududi Navoiy shahri tarkibiga (Karmana tumani sifati-da) kiritildi. 2003-yil dekabrda Navoiy tumapi nomi Karmana tumani deb oʻzgartirildi va Karmana shahri tuman markazi sifatida belgilandi."""
    await message.answer(text)


@dp.message_handler(text='Navbahor')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Navbahor_tumani.png/300px-Navbahor_tumani.png')
    text = """Navbahor tumani - Navoiy viloyatidagi tuman. Viloyatning janubi-sharqida joylashgan. 1980-yil 12-martda tashkil etilgan. 1988-yilda Navoiy tumaniga qoʻshib yuborilgan. 1992-yilda yana alohida tuman sifatida qayta tuzilgan. Navbahor tumani sharqda Samarqand viloyatining Paxtachi tumani, gʻarbda Konimex tumani va Buxoro viloyati, shimolida Nurota va Konimex tuman yaylov yerlari, janubida Karmana tumani bilan chegaradosh. Maydoni 1,57 ming km². Aholisi 86,5 ming kishi (2003). Tumanda 7 qishloq fuqarolari yigʻini (Arabsaroy, Beshrabot, Gigant, Olchin, Turkiston, Yangiyoʻl, Yangiqoʻrgʻon) bor. Markazi — Beshrabot qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Navoiy')
async def echo(message: types.Message):
    text = """Navoiy tumani - Navoiy viloyatidagi tuman (1926—58 yillarda Karmana, 1962-yildan hozirgi nomda. 1980-yilda Navoiy tumani dan Navbahor tumani ajralib chiqqan. 1988-yilda qayta qoʻshilgan, 1992-yilda yana ajralgan). 1999-yilda Karmana shahri Navoiy shahri tarkibiga qoʻshilganligi munosabati bilan, tuman markazi Malikrabot shaharchasiga koʻchirildi. Navoiy tumani Zarafshon daryosining chap sohilida joylashgan. Shim.dan Navbahor tumani, gʻarbdan Qiziltepa tumani, sharkdan Samarqand viloyatining Paxtachi tumani, jan.dan Qashqadaryo viloyati bilan chegaradosh. Maydoni 0,95 ming km². Aholisi 69,5 ming kishi (2003). Tumanda 6 qishloq fuqarolar yigʻini (Doʻrmon, Jaloyir, Narpay, Uyrat, Yangiariq, Hazora), 1 shaharcha (Malikrabot) bor."""
    await message.answer(text)


@dp.message_handler(text='Qiziltepa')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Qiziltepa_tumani.png/300px-Qiziltepa_tumani.png')
    text = """Qiziltepa tumani - Navoiy viloyatidagi tuman. 1935-yil 9-fevral da tashkil etilgan. 1962-yil 24-dekabrda Gʻijduvon tumaniga qoʻshilgan. 1970-yil 7-dekabrda qaytadan tashkil etilgan. Shimoliy dan Konimex, Navbahor tumanlari, shimoli-sharqsan Karmana tumani, sharqdan Samarqand va Qashqadaryo viloyatlari, janubidan Buxoro viloyatining Kogon tumani, gʻarbdan Buxoro, Vobkent va Gʻijduvon tumanlari bilan chegaradosh. Maydoni 2,2 ming km². Aholisi 112,4 ming kishi (2004). Tumanda 1 shahar (Qiziltepa), 8 qishloq fuqarolar yigʻini (Arabon, Boʻston, Vangʻozi, Gardiyon, Zarmitvn, Oqoltin, Xoʻjahasan, Yangihayot) bor. Markazi — Qiziltepa shahri"""
    await message.answer(text)


@dp.message_handler(text='Uchquduq')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Uchquduq_tumani.png/300px-Uchquduq_tumani.png')
    text = """Uchquduq tumani - Navoiy viloyatidagi tuman. 1982-yil 25 martda tashkil etilgan. Shim.dan Qozogʻiston Respublikasi, gʻarbdan Qoraqalpogʻiston Respublikasi, jan.dan Buxoro viloyati va sharqdan Tomdi, Konimex tumanlari bilan chegaradosh. Maydoni 46,63 ming km². Aholisi 38,8 ming kishi (2004). Tumanda 5 qishloq fuqarolar yigʻini (Avangard, Boʻzdoʻngi, Mingbuloq, Oltintov, Uzunquduq) bor. Markazi — Uchquduq shahri."""
    await message.answer(text)


@dp.message_handler(text='Zarafshon')
async def echo(message: types.Message):
    text = """Zarafshon - Oʻzbekiston shaharlaridan biri, Navoiy viloyatida joylashgan. Shahar 1965-yillarda bunyod etilgan. Zarafshon qizilqum choʻlida joylashgan. Aholisi 65 ming kishidan koʻproq.(2009)"""
    await message.answer(text)


@dp.message_handler(text='Tomdi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Tomdi_tumani.png/1280px-Tomdi_tumani.png')
    text = """Tomdi tumani — Navoiy viloyatidagi tuman. 1927-yil 3 iyulda tashkil etilgan. Jandan Konimex, Nurota tumanlari, shimdan Qozogʻistonning Qiziloʻrda, sharqsan Janubiy Qozogʻiston viloyatlari, janubi-sharqdan Jizzax viloyati, gʻarbdan Uchquduq tumani bilan chegaradosh. Maydoni 42,4 ming km². Aholisi 26,4 ming kishi (2004). Tumanda 7 qishloq fuqarolar yigʻini (Keregetov, Koriz, Oqquduq, Oqtov, Soʻkitti, Tomdibuloq, Sheli) bor. Tuman markazi — Tomdibuloq qishlogʻi."""
    await message.answer(text)


@dp.message_handler(text='Xatirchi')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Xatirchi_tumani.png/300px-Xatirchi_tumani.png')
    text = """Xatirchi tumani — Navoiy viloyatidagi tuman. 1926-yil 29-sentabrda tashkil etilgan. 1927–30 yillarda Zarafshon okrugidagi tuman, 1938-yildan Samarqand viloyati, 1982-yildan Navoiy viloyati, 1989-yildan Samarqand viloyati, 1992-yildan Navoiy viloyati tarkibida. Shimolidan Nurota, janubisharqdan Samarqand viloyatining Kattaqoʻrgʻon, shimoli-sharqdan Qoʻshrabot, janubidan (Zarafshon daryosi orqali) Narpay va Paxtachi tumanlari, gʻarbdan Navoiy viloyatining Navbahor tumani bilan chegaradosh. Maydoni 1,37 ming km². Aholisi 143,9 ming kishi (2004). Tumanda 1 shahar (Yangirabot), 1 shaharcha (Langar), 9 qishloq fuqarolari yigʻini (Bogʻchakalon, Olchinobod, Oxunboboyev, Oqoltin, Poʻlkan shoir, Xonaqa, Yangiyoʻl, Krracha Mirdosh) bor. Markazi – Xatirchi shahri."""
    await message.answer(text)


@dp.message_handler(text='Nurota')
async def echo(message: types.Message):
    await message.answer_photo('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Nurota_tumani.png/300px-Nurota_tumani.png')
    text = """Nurota tumani - Navoiy viloyatidagi tuman. Shimolidan viloyatning Tomdi, gʻarbdan Konimex tumanlari, Buxoro viloyati, sharqdan Jizzax viloyati, janubidan Navoiy, Xatirchi tumanlari, Samarqand viloyati bilan chegaradosh. Maydoni 6,5 ming km². Aholisi 78 ming kishi (2003). 1 shahar (Nurota), 7 kish-loq fuqarolari yigʻini (Nurota, Dehi-baland, Sentob, Qizilcha, Chuya, Gum, Gʻozgʻon) bor. Tuman markazi — Nurota shahri
Nurota tumani 1926-yil 29-sentabrda Nurota uyezdi (markazi Nurota qishlogʻi) oʻrnida tashkil etilgan. 1930-yil 17 avpdan Nurota tumani Samarqand viloyati, 1982-yildan Navoiy viloyati, 1988-yildan Samarqand viloyati, va nihoyat, 1992-yil martdan yana Navoiy viloyati tarkibida."""
    await message.answer(text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
