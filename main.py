import telebot
from db import database


async def on_startup(dispatcher):
    await database.connect()
  

async def on_shutdown(dispatcher):
    await database.disconnect()
    await bot.delete_webhook()
    
async def save(user_id, text):
    await database.execute(f"CREATE TABLE messages ("
                           f"id SERIAL PRIMARY KEY,"
                           f"telegram_id INTEGER NOT NULL,"
                           f"text text NOT NULL"
                           f");")


    await database.execute(f"INSERT INTO messages(telegram_id, text) "
                           f"VALUES (:telegram_id, :text)", values={'telegram_id': user_id, 'text': text})


async def read(user_id):
    results = await database.fetch_all('SELECT text '
                                       'FROM messages '
                                       'WHERE telegram_id = :telegram_id ',
                                       values={'telegram_id': user_id})
    return [next(result.values()) for result in results]



# Создаем экземпляр бота
bot = telebot.TeleBot('5325079329:AAGqWJjwUr-3ywZ3mkmowAzs8cBNidjqvUA')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(-1001467716299, 'Вы написали: ' + message.text)
    await save(message.from_user.id, message.text)
    messages = await read(message.from_user.id)
    await message.answer(messages)
    
# Запускаем бота
bot.polling(none_stop=True, interval=0)