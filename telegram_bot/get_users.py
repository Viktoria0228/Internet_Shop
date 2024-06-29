from .create_bot import bot
from registration_page.models import User
from project.settings import shop

@bot.callback_query_handler(func=lambda callback: "get_users" in callback.data)
def get_users(callback):
    print("get_users")
    with shop.app_context():
        users = User.query.all()
        users_names = "\n".join([user.name for user in users])
        '''
        user_names = []
        for user in users:
            user_names.append(user.name)
        '''
        bot.send_message(chat_id=callback.message.chat.id, text = users_names)