from telegram import Bot, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)



token1 = "5915956816:AAGWZYlBpZG37Z0j7G9mq4kMJys406bK9v4"

bot = Bot(token = "5915956816:AAGWZYlBpZG37Z0j7G9mq4kMJys406bK9v4")
updater = Updater(token = token1)
dispatcher = updater.dispatcher



def start(update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Пришли мне сообщение и я удалю из него слова, в которых содержится сочетание букв "абв"')

def text_messages(update, context: CallbackContext):
    text = update.message.text.split()
    text_to_send = [el for el in text if not 'абв' in el]
    text_to_send = ' '.join(text_to_send)
    context.bot.send_message(update.effective_chat.id, text_to_send)

start_handler = CommandHandler('start', start)
text_messages_handler = MessageHandler(Filters.text, text_messages)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_messages_handler)

updater.start_polling()
updater.idle()