# Yahoo-Stock-Checker
Getting information of a stock from Yahoo 

# yahoo_stock.py
This script contains only one function, taking in the yahoo stock code as an input and returning the stock information dictionary as an output, without any side effects. 
This script access the following 2 urls using selenium: 
  https://sg.finance.yahoo.com/quote/{stock_code}?p={stock_code}
  https://sg.finance.yahoo.com/quote/{stock_code}/key-statistics?p={stock_code}
before reading the tables with BeautifulSoup in bs4. 
The funciton is meant to be used in other bigger projects, such as data compilation or a stock bot as shown below. 

# bot.py 
The code in bot.py was adapted from https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq
This .py was written just to demostrate a possible usage of the yahoo_stock.py
This telegram bot reads a stock code and replies with some key values of the stock. 



