import telebot

bot = telebot.TeleBot("7038064232:AAGOxMupvF9OnZDgOhgk4YUMd5dagbpa-EM")

get_users_button = telebot.types.InlineKeyboardButton(text = 'GET USERS', callback_data = "get_users")
get_products_button = telebot.types.InlineKeyboardButton(text = "GET PRODUCTS", callback_data = "get_products")
add_user_button = telebot.types.InlineKeyboardButton(text = 'ADD USER', callback_data = "add_user")
inline_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [[get_users_button, get_products_button, add_user_button]])
# keyboard.add(button1, button2, button3)

@bot.message_handler(commands = ['start'])
def start_message(message):
    print("start bot")
    bot.send_message(chat_id = message.chat.id, text = "Вітаю, користувачу!")
    bot.send_message(chat_id = message.chat.id, text = "Оберіть одну з функцій бота", reply_markup = inline_keyboard)
    