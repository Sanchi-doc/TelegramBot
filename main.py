import telebot
from telebot import types

bot = telebot.TeleBot("5889035202:AAEAfj7hjOyragLyKHn8jNEmUfXOseUY4CA")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3) 
    bt1 = types.KeyboardButton("Основы программирования")
    bt2 = types.KeyboardButton("Fullstack разработчик")
    bt3 = types.KeyboardButton("Java разработчик")
    bt4 = types.KeyboardButton("Front-End разработчик")
    bt5 = types.KeyboardButton("Python разработчик")
    bt6 = types.KeyboardButton("Web &UI/UX дизайн")
    bt7 = types.KeyboardButton("QA тестировщик")
    bt8 = types.KeyboardButton("Автоматизация тестирования")
    markup.add( bt1, bt2, bt3,bt4,bt5, bt6, bt7,bt8)
    mess = f"Привет, <b>{message.from_user.first_name} </b>!\nКакое направление тебя интересует?" 
    bot.send_message(message.chat.id,mess,parse_mode="html",reply_markup=markup)




@bot.message_handler(commands=["website"])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://prog.academy"))
    bot.send_message(message.chat.id,"Отличный выбор,просто нажми на кнопку ниже и начинай изучение курсов прямо сейчас )",parse_mode="html",reply_markup=markup)

@bot.message_handler(commands=["instagram"])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/prog.academy/"))
    bot.send_message(message.chat.id,"Нажми на кнопку ниже и погрузись в мир IT прямо сейчас",parse_mode="html",reply_markup= markup)

@bot.message_handler(commands=["facebook"])
def facebook(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Фейсбук",url="https://www.facebook.com/prog.kiev.ua"))
    bot.send_message(message.chat.id,"Нажми на кнопку ниже и погрузись в мир IT прямо сейчас",parse_mode="html",reply_markup=markup)
    

@bot.message_handler(commands=["youtube"])
def youtube(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в youtube",url="https://www.youtube.com/c/ProgKievUa"))
    bot.send_message(message.chat.id,"Нажми на кнопку ниже и погрузись в мир IT прямо сейчас",parse_mode="html",reply_markup=markup)



@bot.message_handler(commands=["telegram"])
def youtube(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в telegram",url="https://t.me/progacademy"))
    bot.send_message(message.chat.id,"Нажми на кнопку ниже и погрузись в мир IT прямо сейчас",parse_mode="html",reply_markup=markup)




@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text =='Основы программирования':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/osnovi"))
     bot.send_message(message.chat.id,"Курс посвящен базовым понятиям программирования: типы данных, операторы, переменные, условия, циклы, массивы и функции. Он является вводным и подойдет слушателям с небольшим опытом или вообще без опыта программирования."
,parse_mode="html",reply_markup=markup)
    elif message.text =='Fullstack разработчик':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/fullstack"))
     bot.send_message(message.chat.id," <b>FullStack</b>  совмещает в себе знания Front-End и Backend. Такие специалисты пользуются большим спросом на рынке труда и даже на старте претендуют на высокие зарплаты.",parse_mode="html",reply_markup=markup)
    elif message.text =='Java разработчик':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/java"))
     bot.send_message(message.chat.id," <b>Java</b> - язык программирования общего назначения. На Java пишут бизнес логику веб приложений и мобильные приложения под операционную систему Android. С помощью Java созданы такие проекты как Minecraft и Privat24, а сам язык используют в Google, Facebook, eBay и многих других известных компаниях.",parse_mode="html",reply_markup=markup)
    elif message.text =='Front-End разработчик':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/frontend"))
     bot.send_message(message.chat.id,"<b>Front-End</b> – это разработка визуальной части веб сайтов. Это одна из самых востребованных специальностей. Направление включает изучение языков HTML, CSS и JavaScript. Front-End подходит тем, кто хочет сразу видеть результаты своей работы. Сверстанные страницы можно открыть в веб-браузере сразу после их создания.",parse_mode="html",reply_markup=markup)
    elif message.text =='Python разработчик':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/python"))
     bot.send_message(message.chat.id,"<b>Python </b>- высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен, поэтому Python часто рекомендуют новичкам как 1-й язык программирования. Python активно используют в компаниях Google, Facebook, Microsoft, Dropbox и Intel.",parse_mode="html",reply_markup=markup)
    elif message.text =='Web &UI/UX дизайн':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/web-design"))
     bot.send_message(message.chat.id,"<b>Web-дизайнер</b> – это специалист, который отвечает за то, как выглядит и воспринимается Интернет сайт. Он придумывает логотипы, баннеры и другие элементы графики, продумывает навигацию по сайту, определяет, где следует разместить текст и изображения. Результаты работы Web-дизайнера передаются Front-End разработчикам и они превращают макет в рабочий сайт.",parse_mode="html",reply_markup=markup)
    elif message.text =='QA тестировщик':
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/qa"))
     bot.send_message(message.chat.id,"<b>QA - quality assurance - обеспечение качества.</b>\n"
"<b>Тестировщик </b>— специалист, принимающий участие в тестировании компонента или системы. В его обязанность входит поиск вероятных ошибок и сбоев в функционировании программы. Тестировщик моделирует различные ситуации, которые могут возникнуть в процессе использования предмета тестирования, чтобы разработчики смогли исправить обнаруженные ошибки.",parse_mode="html",reply_markup=markup)
    elif message.text =="Автоматизация тестирования":
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton("Перейти по ссылке",url="https://prog.academy/qa-auto"))
     bot.send_message(message.chat.id,"<b>Автоматизированное тестирование или автоматизация тестирования</b> – это метод тестирования программного обеспечения, который выполняется с использованием специальных программных средств, которые, в свою очередь необходимы для выполнения набора тестовых примеров. Напротив, ручное тестирование выполняется человеком, сидящим перед компьютером и тщательно выполняющим каждый шаг теста «руками».",parse_mode="html",reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id,"такого курса у нас нету (",parse_mode="html",reply_markup=markup)




bot.polling(none_stop=True)
