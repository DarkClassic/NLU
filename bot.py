import telebot

#main variables

TOKEN = "605014854:AAF1HuRNnc0M8VmzZKlPz7rbYV2FSoFkDE4"

bot = telebot.TeleBot(TOKEN)

bot.send_message(341757028, "test")

upd = bot.get_updates()
print(upd)

#last_upd = upd[-1]

#message_from_user = last_upd.message
#print(message_from_user)

print(bot.get_me())



#def log(message):
    #print("----------------")
   # file = open("LOG.txt", mode='a', encoding='utf_8')
    #file2 = open("username.txt", mode='a', encoding='utf_8')
    #f_str = str(str(message.chat.id) + "\n")
  # file2.write(str(message.from_user.username) + "\n")
  #  file.write(f_str)
   # file.close()
    #file2.close()
   # print("Сообщение от {0} {1} {2} {3} TEXT - {4}. \n ".format(message.from_user.first_name,message.from_user.last_name,message.from_user.username,str(message.from_user.id),str(message.text)))





@bot.message_handler(commands=['start'])
def handle_text(message):
    log(message)
    bot.send_message(message.from_user.id,"Бот створений для вашого комфорту, якшо ви студент нашого коледжу, натисніть STUDENT \n"
                                      "Якщо ви хочете почати навчатись в нашому коледжі, натисніть STUDY")
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/STUDENT','/STUDY')
    user_markup.row('/HIDE')

    bot.send_message(message.from_user.id,'WELCOME!',reply_markup=user_markup)


@bot.message_handler(commands=['STUDY'])
def handle_text(message):
    bot.send_message(message.from_user.id,'http://plc.nlu.edu.ua/')
    bot.send_location(message.from_user.id, 49.580058, 34.559962)

@bot.message_handler(commands=['STUDENT'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Дорогий студент, дякуємо за використання боту, ви можете спілкуватися з ним за допомогою бесіди, для відображення повного списку натисніть /help")
    # bot.send_message(message.from_user.id, 'Відключаем основну клавіатуру...Щоб включити її знову натисніть  /start',
                    # reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['help'])
def handle_text(message):

    bot.send_message(message.from_user.id,
                     "Повний список основних команд \n >>> /Schedule - розклад \n >>> /News - новини коледжу  \n >>> /AI - робота з штучним інтелектом ")
    bot.send_message(message.from_user.id, '   ', reply_markup=telebot.types.ReplyKeyboardRemove())

#Прохання від автора, бот має систему ИИ, він може знаходити НПА по потрібній вам темі, відфільтровуючи їх та шукаючи чинні, я буду дуже вдячний, якщо ви будете кидати йому
@bot.message_handler(commands=['Schedule'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     "Повний список основних команд \n >>> /Schedule - розклад \n >>> /News - новини коледжу :arrow_forward: \n >>> /AI - робота з штучним інтелектом ")
    bot.send_message(message.from_user.id, "Наразі нічого немає...  ")
    bot.send_message(message.from_user.id, '   ', reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['News'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     "Повний список основних команд \n >>> /Schedule - розклад \n >>> /News - новини коледжу :arrow_forward: \n >>> /AI - робота з штучним інтелектом ")
    bot.send_message(message.from_user.id, "Зараз нічого немає...  ")
    bot.send_message(message.from_user.id, '   ', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['AI'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Прохання від автора, бот має систему ИИ, він може знаходити НПА по потрібній вам темі, відфільтровуючи їх та шукаючи чинні, я буду дуже вдячний, "
                                           "якщо ви будете відправляти йому посилання з НПА та вести бесіду з ним по темі права, таким чином ви по запросу, "
                                           "наприклад(Трудове право, відпустка зможете отриматі пов'язані документи та терміни.) Наданний момент він може відповідати на нескладні запитання [В РОЗРОБЦІ]")


@bot.message_handler(commands=['HIDE'])
def handle_text(message):

    bot.send_message(message.from_user.id,'Відключаем клавіатуру...Щоб включити її знову натисніть  /start', reply_markup=telebot.types.ReplyKeyboardRemove())


#@bot.message_handler(commands=['admins'])
#def handle_text(message):



@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Будь-ласка, використовуйте команди, нариклад /start"
    if message.text == "Головний закон?" or message.text == "головний закон":

      bot.send_message(message.chat.id, "Конституція України")


    elif message.text == "Admin":
     # bot.send_message(message.from_user.id, "Пароль..?")
     # if message.text == "passPOLICE2001":
          bot.send_message(message.from_user.id, "Введите Сообщение!")
          DarkMes = message.text
          a_file = open("LOG.txt", mode='r', encoding='utf_8')
          for line in a_file:
              bot.send_message(message.from_user.id == str(a_file), str(DarkMes))
       # bot.send_message(message.chat.id, "работаю,так что сосать")



    else:
        log(message)
        bot.send_message(message.from_user.id, answer)



bot.polling(none_stop=True,interval=0)
