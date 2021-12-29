# Yahoo-Stock-Checker
Getting information of a stock from Yahoo 

# yahoo_stock.py
This script contains only one function, taking in the yahoo stock code as an input and returning the stock information dictionary as an output, without any side effects.  
This script access the following 2 urls using selenium:  
  https://sg.finance.yahoo.com/quote/{stock_code}?p={stock_code}  
  https://sg.finance.yahoo.com/quote/{stock_code}/key-statistics?p={stock_code}  
before reading the tables with BeautifulSoup in bs4.  

![image](https://user-images.githubusercontent.com/80518234/147623264-0b2ce990-2458-422f-99d6-aaf9a43d2a94.png)

The funciton is meant to be used in other bigger projects, such as data compilation or a stock bot as shown below. 

# bot.py 
The code in bot.py was adapted from https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq  
This .py was written just to demostrate a possible usage of the yahoo_stock.py  
This telegram bot reads a stock code and replies with some key values of the stock.  

![image](https://user-images.githubusercontent.com/80518234/147623448-c2af3455-576f-4dc9-b878-8fd01d6c1247.png)


# cons
- Getting the stock information takes awhile (~20s), somethings with add timeouts in between checks. Not good for getting large amount of data  
- Require some hard coding to select specific information  
- Different case conditions has to be added to make it more resistant to bad inputs  
