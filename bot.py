import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
#enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                  level=logging.INFO)
logger=logging.getLogger(__name__)                
    
TOKEN="873494515:AAG4H6rFKuVPURlNw6W26VbdjN1DNL-WuB8"

def start(bot,update):
    print(update)
    author=update.message.from_user.first_name
    reply="Hi ! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def _help(bot,update):
    help_text="Hey! This is a help text."
    bot.send_message(chat_id=update.message.chat_id,text=help_text)

def echo_text(bot,update):
    reply=update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)
    
def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)

def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update,update.error)    




def main():
    updater=Updater(TOKEN)

    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)


    updater.start_polling()
    logger.info("Started polling..")

    updater.idle()  # to stop the program

if __name__== "__main__":
    main()    