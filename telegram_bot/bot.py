import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

FORMAT = '%(asctime)s - %(message)s'  # задаем формат атрибуту format: дата - сообщение
logging.basicConfig(filename="bot.log", level=logging.INFO, format=FORMAT)

def talk_to_me(update, context):
    text = update.message.text
    print(text)  # вывод в консоль
    update.message.reply_text(text)  # вывод в телеграм

def greet(update,context):
    """
    update - информация от телеграм
    context - отдаём команды боту
    """
    print("Вызван /start")  # вывод в консоль
    
    update.message.reply_text("Hello there")  # вывод в телеграм

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
