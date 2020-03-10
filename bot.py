import telebot
import os
import Numbers
import Schedule

#main variables


TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)



for line in range(1,2):
 bot.send_message(341757028, "test")
#for line in range(1,150):
 #bot.send_message(572202721, "111")
 #for line in range(1,50):
  #bot.send_message(624156407, "P3")

#upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]

#message_from_user = last_upd.message
#print(message_from_user)

print(bot.get_me())



def log(message):
    print("----------------")

    file2 = open("username.txt", mode='a', encoding='utf_8')

    file2.write(str(message.from_user.username) + "\n")
  #  for line in file2:
        #if "DarkCassic" in line:
           #fileLog.write("123")
         #  print("123")


    file2.close()
    print("Сообщение от {0} {1} {2} {3} TEXT - {4}. \n ".format(message.from_user.first_name,message.from_user.last_name,message.from_user.username,str(message.from_user.id),str(message.text)))


@bot.message_handler(commands=['start'])
def handle_text(message):
    log(message)
    bot.send_message(message.from_user.id,"Бот створений для вашого комфорту, якшо ви студент нашого коледжу, натисніть STUDENT \n"
                                      "Якщо ви хочете почати навчатись в нашому коледжі, натисніть STUDY \n"
                                        "Для отримування новин,розкаладу натисніть, ->   /Register  <-")
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/STUDENT','/STUDY')
    user_markup.row('/HIDE')

    bot.send_message(message.from_user.id,'WELCOME!',reply_markup=user_markup)

@bot.message_handler(commands=['Register'])
def handle_text(message):
    log(message)
    fileLog = open("LOG.txt", mode='a+', encoding='utf_8')
    f_str = str(str(message.chat.id) + "\n")
    bot.send_message(341757028,"Сообщение от {0} {1} {2} {3} TEXT - {4}. \n ".format(message.from_user.first_name,message.from_user.last_name,message.from_user.username,str(message.from_user.id),str(message.text)))

    bot.send_message(message.from_user.id, "Вас ЗАРЕЄСТРОВАНО,дякуємо {0}".format(message.from_user.first_name))
    fileLog.write(f_str)
    fileLog.close()




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
                     "Повний список основних команд \n >>> /Schedule - розклад \n >>> /News - новини коледжу  \n >>> /Retaking - графік перездач ")
    bot.send_message(message.from_user.id, '   ', reply_markup=telebot.types.ReplyKeyboardRemove())

#Прохання від автора, бот має систему ИИ, він може знаходити НПА по потрібній вам темі, відфільтровуючи їх та шукаючи чинні, я буду дуже вдячний, якщо ви будете кидати йому
@bot.message_handler(commands=['Schedule'])

def handle_text(message):
    bot.send_message(message.from_user.id,
                     "Повний список основних команд \n >>> /Schedule - розклад \n >>> /News - новини коледжу  \n >>> /Retaking - графік перездач ")
    bot.send_message(message.from_user.id, "Перший курс - /1 \n"
                                           "Другий курс - /2 \n"
                                            "Третій курс - /3 \n"
                                            "Четвертий курс - /4 \n")
    bot.send_message(message.from_user.id, '   ', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['Edit'])

def handle_text(message):

    bot.send_message(message.from_user.id, "Пароль?")


    @bot.message_handler(content_types=['text'])
    def handle_text(message):

        if message.text == "EditAdmin123":
            Numbers.prov = 1
            bot.send_message(message.from_user.id, "Введите Новости")
        elif message.text == message.text and Numbers.prov == 1:
            if Numbers.prov == 1:
                Numbers.prov = 0
                Numbers.defText = message.text
                print(Numbers.defText)
            a_file = open("LOG.txt", mode='r', encoding='utf_8')
            for line in a_file:
                help_s = line
                print(help_s)
                bot.send_message(help_s, message.text)
                Numbers.prov = 0





@bot.message_handler(commands=['News'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     "Повний список основних команд \n >>> /Schedule - розклад \n >>> /News - новини коледжу \n >>> /Retaking - графік перездач ")
    bot.send_message(message.from_user.id,Numbers.defText)
   # bot.send_message(message.from_user.id, '   ', reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['HIDE'])
def handle_text(message):

    bot.send_message(message.from_user.id,'Відключаем клавіатуру...Щоб включити її знову натисніть  /start', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(commands=['Retaking'])
def handle_text(message):
    Numbers.full_text = ""
    a_file = open("Retaking/TEXT.txt", mode='r', encoding='utf_8')
    for line in a_file:
        Numbers.full_text += line
    bot.send_message(message.chat.id, Numbers.full_text)
#@bot.message_handler(commands=['admins'])
#def handle_text(message):

@bot.message_handler(commands=['1'])
def handle_text(message):
    log(message)
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/11','/12','/13')
    user_markup.row('/HIDE')
    bot.send_message(message.from_user.id, "Оберіть группу", reply_markup=user_markup)
    bot.send_message(message.from_user.id, "Для отримання документу розкладу натиснить це - /doc",reply_markup=user_markup)

@bot.message_handler(commands=['2'])
def handle_text(message):
    log(message)
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/21','/22','/23','/25')
    user_markup.row('/HIDE')
    bot.send_message(message.from_user.id, "Оберіть группу", reply_markup=user_markup)


@bot.message_handler(commands=['3'])
def handle_text(message):
    log(message)
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/31','/32','/33','/24')
    user_markup.row('/HIDE')
    bot.send_message(message.from_user.id, "Оберіть группу", reply_markup=user_markup)


@bot.message_handler(commands=['4'])
def handle_text(message):
    log(message)
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/41','/42','/43','/34')
    user_markup.row('/HIDE')
    bot.send_message(message.from_user.id, "Оберіть группу", reply_markup=user_markup)


@bot.message_handler(commands=['doc'])
def handle_text(message):
    check = 0
    dir = 'Schudele/'
    ifd = os.listdir(dir)
    try:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, p_file)
            p_file.close()
            check = 1
    except:
        if check == 0:
            bot.send_message(message.chat.id, "Файл отсутсвует")

@bot.message_handler(commands=['11'])
def handle_text(message):
    check = 0
    dir = 'Schudele/First/11'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/First/11/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check =1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            # p_file = open("Schudele/First/11/photo.png", mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")

@bot.message_handler(commands=['12'])
def handle_text(message):
    check = 0
    dir = 'Schudele/First/12'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/First/12/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['13'])
def handle_text(message):
    check = 0
    dir = 'Schudele/First/13'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/First/13/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")

@bot.message_handler(commands=['21'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Second/21'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Second/21/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['22'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Second/22'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Second/22/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['23'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Second/23'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Second/23/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['25'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Second/25'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Second/25/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")

@bot.message_handler(commands=['24'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Second/24'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Second/24/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['31'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Third/31'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Third/31/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['32'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Third/32'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Third/32/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['33'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Third/33'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Third/33/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")

@bot.message_handler(commands=['34'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Third/34'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Third/34/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['41'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Fourth/41'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Fourth/41/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['42'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Fourth/42'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Fourth/42/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")
@bot.message_handler(commands=['43'])
def handle_text(message):
    check = 0
    dir = 'Schudele/Fourth/43'
    ifd = os.listdir(dir)
    Numbers.full_text = ""
    try:
        a_file = open("Schudele/Fourth/43/TEXT.txt", mode='r', encoding='utf_8')
        for line in a_file:
            Numbers.full_text += line
        bot.send_message(message.chat.id, Numbers.full_text)
        check = 1
    except:
        print(dir)
        for file in ifd:
            p_file = open(dir + '/' + file, mode='rb')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            bot.send_photo(message.chat.id, p_file)
            p_file.close()
            check = 1

    if check == 0:
        bot.send_message(message.chat.id, "Файл отсутсвует")


   # else:
      #  log(message)
       # bot.send_message(message.from_user.id, answer)
line = ""
Numbers.full_text = ""
Numbers.prov = 0
bot.polling(none_stop=True,interval=0)
