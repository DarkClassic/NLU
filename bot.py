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
 
