import project, telegram_bot

if __name__ == "__main__":
    
    project.shop.run(debug = True)
    telegram_bot.bot.infinity_polling()