import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# from bot import get_stock_info

def stock_check(stock_code):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        options=options, 
        executable_path='D:\PythonFiles\Drivers\chromedriver.exe'
        )

    url1 = f"https://sg.finance.yahoo.com/quote/{stock_code}.SI?p={stock_code}.SI"
    url2 = f"https://sg.finance.yahoo.com/quote/{stock_code}.SI/key-statistics?p={stock_code}.SI"

    unchecked1, unchecked2 = True, True
    stock = {}
    stock.update({'Code':stock_code})

    trycount = 0
    
    while unchecked1:
        try:
            driver.get(url1)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "quote-summary")))
            html = BeautifulSoup(driver.page_source, features='lxml')
            rows = html.find_all('tr') 
            for row in rows: 
                data_type, data_value = row.find_all('td')
                stock.update({data_type.get_text().strip(): data_value.get_text()})
            unchecked1 = False
        except:
            print("unable to get info1, retrying")
            trycount += 1 
            if trycount > 6:
                print(stock_code + " skipped")
                return {}
            time.sleep(10)

    while unchecked2:
        try:
            driver.get(url2)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "Main")))
            unchecked2 = False
            html = BeautifulSoup(driver.page_source)
            rows = html.find_all('tr') 
            for row in rows: 
                data_type, data_value = row.find_all('td')
                stock.update({data_type.get_text(): data_value.get_text()})
        except:
            print("unable to get info2, retrying")
            trycount += 1 
            if trycount > 6:
                print(stock_code + " skipped")
                return {}
            time.sleep(10)
    
    driver.close()
    return stock

# print(stock_check('D05'))