import telebot

bot = telebot.TeleBot('5325079329:AAGqWJjwUr-3ywZ3mkmowAzs8cBNidjqvUA')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message is None):
        bot.send_message(-1001467716299, ' message is None ' )
    
    if (message.from is None):
        bot.send_message(-1001467716299, ' message.from is None ' )
 
    if (message.from.id is None):
        bot.send_message(-1001467716299, ' message.from.id is None ' )
    
    #userid = message.from.id
    bot.send_message(-1001467716299, ': ' + message.text + f' date={message.date}' )
   
bot.polling(none_stop=True, interval=0)