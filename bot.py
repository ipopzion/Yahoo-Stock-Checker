#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Telegram Bot that tells of the stock prices.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from yahoo_stock import stock_check

with open('token.txt', 'r') as file: 
    TOKEN = file.read()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def get_stock_info(update, context):
    """Returns stock info."""
    stock_code = update.message.text.strip()
    print(stock_code)
    stock_info = stock_check(stock_code)
    text = f"\
<a href='https://sg.finance.yahoo.com/quote/{stock_code}.SI/key-statistics?p={stock_code}.SI'>{stock_code}</a>\n\
Price         : {stock_info['Previous close']}\n\
PE-Ratio   : {stock_info['PE ratio (TTM)'] or ''}\n\
Dividends : {stock_info['Forward annual dividend yield 4'] or ''}\n"
    update.message.reply_text(text=text, parse_mode=telegram.ParseMode.HTML)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - return stock info
    dp.add_handler(MessageHandler(Filters.text, get_stock_info))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
