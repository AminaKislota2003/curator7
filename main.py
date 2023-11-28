import telebot

bot=telebot.TeleBot('6416428052:AAEqbD8Kp2meJj7IB-7r6Q-XMym1yQy4pPY')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Вы запустили бота *STAR_Fbot* \n существуют следующие команды: \n /info - маленькая информация \n /!!! - секретная информация \n /problem - проблема с Flask ', parse_mode='Markdown')

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, 'Этого маленького бота сделал студент колледжа ХХХ второго курса \n \n мне не нужен мак т.к. уже есть', pars_mode='Markdown')

@bot.message_handler(commands=['!!!'])
def main(message):
    bot.send_message(message.chat.id, 'Серетная информация -> [ХХХ](https://youtu.be/xvFZjo5PgG0)', parse_mode='Markdown')

@bot.message_handler(commands=['problem'])
def main(message):
    bot.send_message(message.chat.id, 'У меня проблема с Flask при подключении debag. Начитает бесконечно грузить сайт \n
	сам код (мб поможете) -> [S](https://pastebin.com/dl/sG777DbU) \n если все таки захотите помочь ,я скину остальные файлы ', parse_mode='Markdown')


bot.infinity_polling()
