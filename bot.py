from telegram import Update
from telegram.ext import Updater , CommandHandler , MessageHandler , CallbackContext
import threading
from time import sleep

def start(update: Update , context : CallbackContext):
    msgId = update.message.message_id
    
    if len(context.args) != 0 :
        
        if context.args[0] == password:
            if update.message.chat_id not in authedUsers:
            
                authedUsers.append(update.message.chat_id)
                context.bot.send_message(update.message.chat_id, 'welcome :)')
            else:
                context.bot.send_message(update.message.chat_id, 'welcome Back')
        else:
            context.bot.send_message(update.message.chat_id, 'Hello World!')
    else:
            context.bot.send_message(update.message.chat_id, 'Hello World!')    

def main(): 
    dispatcher.add_handler(CommandHandler(['start'], start))
    updater.start_polling()

def run():
    global updater ,dispatcher , password ,authedUsers
    updater = Updater('5881430169:AAFV46_g5hiIL9uYpigFI8zetNKOx-aU2n0')
    dispatcher = updater.dispatcher
    password = "Hi"
    authedUsers = [163552356] #  , 5449566206
    t1 = threading.Thread(target=main)
    t1.start()
def send(text):

    for user in authedUsers :
        CallbackContext(dispatcher).bot.send_message(user, text)

if __name__ == '__main__':
    
    run()
    breakpoint()
