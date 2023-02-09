from log import get_id_user, get_input_data, get_result, save_log
from controller import process_func, process_step
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "5915956816:AAGWZYlBpZG37Z0j7G9mq4kMJys406bK9v4"
bot = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, я могу высчитать твой пример: ')

    get_id_user(update.effective_chat.id)

def math_example(update, context):
    data = update.message.text
    get_input_data(data)
    result = process_func(data)
    get_result(result)
    save_log()
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')


start_handler = CommandHandler('start', start)
math_example_handler = MessageHandler(Filters.text, math_example)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(math_example_handler)


updater.start_polling()
updater.idle()