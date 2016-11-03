from rails.app import Rails
app = Rails()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater('292705016:AAGHG0J129bFE9BHcLE_EufB6IBXsXVXWuU')

# Get the dispatcher to register handlers
dp = updater.dispatcher
bot = updater.bot


@app.rail('get_texts', ['reply'])
def receive_msg(self):
    try:
        msg = self.rail.pop()
        self.carriages['reply'].append(msg)
    except IndexError:
        pass


@app.rail('reply', [])
def reply(self):
    try:
        msg = self.rail.pop()
        bot.sendMessage(chat_id=msg['chat_id'], text='HI!!')
    except IndexError:
        pass


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def fill_q(bot, update):
    app.wagons['get_texts'].rail.append(update.message)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    dp.add_handler(MessageHandler(Filters.text, fill_q))

    # log all errors
    dp.add_error_handler(error)
    updater.start_polling()
    #updater.idle()

if __name__ == '__main__':
    app.run(preworks = [main])
