import telebot
from telebot import types

bot = telebot.TeleBot("5956319562:AAGbYiFKWCX4vSSAvhG39UkbRj5d3Uulifg")


@bot.message_handler(commands=["start"])
def start(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2) 
    bot1 = types.KeyboardButton("Выбрать курс 💻")
    bot2 = types.KeyboardButton("Инфо ℹ️")  
    markup.add( bot1, bot2)
    mess = f"Привет👋, <b>{message.from_user.first_name}</b> \n Если ты определся какой курс тебе нужен-смело нажимай на кнопку <b>'Выбрать курс 💻'</b>\nЕсли ты хочешь узнать подробную информацию о курсах -смело нажимай на кнопку <b>'Инфо ℹ️'</b>"
    bot.send_message(message.chat.id,mess,parse_mode = "html",reply_markup=markup)
    

@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Выбрать курс 💻":
     markup = types.InlineKeyboardMarkup(row_width=2)
     keyboard_1 = types.InlineKeyboardButton(text="Основы программирования",callback_data="item_1")
     keyboard_2 = types.InlineKeyboardButton(text="Fullstack разработчик",callback_data="item_2")
     keyboard_3 = types.InlineKeyboardButton(text="Java разработчик",callback_data="item_3")
     keyboard_4 = types.InlineKeyboardButton(text="Front-End разработчик",callback_data="item_4")
     keyboard_5 = types.InlineKeyboardButton(text="Python разработчик",callback_data="item_5")
     keyboard_6 = types.InlineKeyboardButton(text="Web &UI/UX дизайн",callback_data="item_6")
     keyboard_7 = types.InlineKeyboardButton(text="QA тестировщик",callback_data="item_7")
     keyboard_8 = types.InlineKeyboardButton(text="Автоматизация тестирования",callback_data="item_8")
     back = types.InlineKeyboardButton(text="На главную 🏘 ",callback_data ="back")
     markup.add(keyboard_1 ,keyboard_2,keyboard_3,keyboard_4,keyboard_5,keyboard_6,keyboard_7,keyboard_8,back)
     bot.send_message(message.chat.id,"Один из самых часто-задаваемых вопросов от новичков, который мы слышим - Какой ЯП учить ",reply_markup=markup)
    
    elif message.text == "Инфо ℹ️":
     markup = types.InlineKeyboardMarkup()
     Back = types.InlineKeyboardButton(text="На главную 🏘 ",callback_data ="back")
     markup.add(Back)
     bot.send_message(message.chat.id,"<b>ℹ️ Информация</b> \n Подробнее про  курсы вы можете перейти по ссылке ниже👇\n Website-https://prog.academy",parse_mode = "html",reply_markup = markup)



@bot.callback_query_handler(func =lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == "item_1":
     markup = types.InlineKeyboardMarkup(row_width=2)
     osnovi = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/osnovi")
     back = types.InlineKeyboardButton("На главную 🏘 ",callback_data= "back")
     markup.add(osnovi,back)
     bot.send_message(callback.message.chat.id,"Курс посвящен базовым понятиям программирования: типы данных, операторы, переменные, условия, циклы, массивы и функции. Он является вводным и подойдет слушателям с небольшим опытом или вообще без опыта программирования.",reply_markup=markup)


    elif callback.data == "item_2":
     markup = types.InlineKeyboardMarkup(row_width=2)
     fullstack= types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/fullstack")
     back = types.InlineKeyboardButton("На главную 🏘 ",callback_data= "back")
     markup.add(fullstack,back)
     bot.send_message(callback.message.chat.id,"<b>FullStack</b> совмещает в себе знания Front-End и Backend. Такие специалисты пользуются большим спросом на рынке труда и даже на старте претендуют на высокие зарплаты.",parse_mode = "html",reply_markup=markup)


    elif callback.data == "item_3":
     markup = types.InlineKeyboardMarkup(row_width=2)
     java = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/java")
     back = types.InlineKeyboardButton("На главную 🏘 ",callback_data="back")
     markup.add(java,back)
     bot.send_message(callback.message.chat.id,"<b>Java</b> - язык программирования общего назначения. На Java пишут бизнес логику веб приложений и мобильные приложения под операционную систему Android. С помощью Java созданы такие проекты как Minecraft и Privat24, а сам язык используют в Google, Facebook, eBay и многих других известных компаниях.",parse_mode = "html",reply_markup=markup)
   

    elif callback.data == "item_4":
     markup = types.InlineKeyboardMarkup(row_width=2)
     frontend = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/frontend")
     back = types.InlineKeyboardButton("На главную 🏘 ",callback_data="back")
     markup.add(frontend,back)
     bot.send_message(callback.message.chat.id,"<b>Front-End</b> – это разработка визуальной части веб сайтов. Это одна из самых востребованных специальностей. Направление включает изучение языков HTML, CSS и JavaScript. Front-End подходит тем, кто хочет сразу видеть результаты своей работы. Сверстанные страницы можно открыть в веб-браузере сразу после их создания.",parse_mode="html",reply_markup=markup)
    

    elif callback.data == "item_5":
     markup = types.InlineKeyboardMarkup(row_width=2)
     python = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/python") 
     back = types.InlineKeyboardButton("На главную 🏘 ",callback_data= "back")
     markup.add(python,back)
     bot.send_message(callback.message.chat.id,"<b>Python </b>- высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен, поэтому Python часто рекомендуют новичкам как 1-й язык программирования. Python активно используют в компаниях Google, Facebook, Microsoft, Dropbox и Intel.",parse_mode="html",reply_markup=markup)   
  

    elif callback.data == "item_6":
     markup = types.InlineKeyboardMarkup(row_width=2)
     web = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/web-design")
     back= types.InlineKeyboardButton("На главную 🏘 ",callback_data= "back")
     markup.add(web,back)
     bot.send_message(callback.message.chat.id,"<b>Web-дизайнер</b> – это специалист, который отвечает за то, как выглядит и воспринимается Интернет сайт. Он придумывает логотипы, баннеры и другие элементы графики, продумывает навигацию по сайту, определяет, где следует разместить текст и изображения. Результаты работы Web-дизайнера передаются Front-End разработчикам и они превращают макет в рабочий сайт.",parse_mode="html",reply_markup=markup)
     

    elif callback.data == "item_7":
     markup = types.InlineKeyboardMarkup(row_width=2)
     web = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/qa")
     back= types.InlineKeyboardButton("На главную 🏘 ",callback_data= "back")
     markup.add(web,back)
     bot.send_message(callback.message.chat.id,"<b>QA - quality assurance - обеспечение качества.</b>\n"
"<b>Тестировщик </b>— специалист, принимающий участие в тестировании компонента или системы. В его обязанность входит поиск вероятных ошибок и сбоев в функционировании программы. Тестировщик моделирует различные ситуации, которые могут возникнуть в процессе использования предмета тестирования, чтобы разработчики смогли исправить обнаруженные ошибки.",parse_mode="html",reply_markup=markup)
  

    elif callback.data == "item_8":
     markup = types.InlineKeyboardMarkup(row_width=2)
     web = types.InlineKeyboardButton("Перейти на курс",url="https://prog.academy/qa-auto")
     back= types.InlineKeyboardButton("На главную 🏘 ",callback_data= "back")
     markup.add(web,back)
     bot.send_message(callback.message.chat.id,"<b>Автоматизированное тестирование </b> – это метод тестирования программного обеспечения, который выполняется с использованием специальных программных средств, которые, в свою очередь необходимы для выполнения набора тестовых примеров. Напротив, ручное тестирование выполняется человеком, сидящим перед компьютером и тщательно выполняющим каждый шаг теста «руками».",parse_mode="html",reply_markup=markup)
  

    elif callback.data == "back":
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1 = types.KeyboardButton("Выбрать курс 💻")
     item2 = types.KeyboardButton("Инфо ℹ️")
     markup.add(item1,item2)
     bot.send_message(callback.message.chat.id,"Вы в главном меню!",reply_markup=markup)
  


bot.polling(none_stop=True)