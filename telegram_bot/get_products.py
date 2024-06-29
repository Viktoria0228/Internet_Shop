import telebot
from .create_bot import bot
from shop_page.models import Product
from project.settings import shop  # Import the Flask app instance

@bot.callback_query_handler(func=lambda callback: "get_products" in callback.data)
def get_users(callback):
    print("get_product")
    with shop.app_context():
        products = Product.query.all()
        product_names = "\n".join([product.name for product in products])  # Assuming Product has a 'name' attribute
        bot.send_message(chat_id=callback.message.chat.id, text=product_names)
