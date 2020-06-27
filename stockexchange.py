from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.tmxmoney.com/en/index.html')

wait = WebDriverWait(driver, 10)

def search(ticker):
    searchElement =driver.find_element_by_id('QuoteSymbol_1')
    searchElement.send_keys(ticker)
    wait.until(EC.visibility_of_all_elements_located((BY.CLASS_NAME, 'ac_even')))
    searchElement.send_keys(Keys.DOWN)
    searchElement.send_keys(Keys.ENTER)

def get_stock_address():
    return driver.current_url

def get_last_price():
    return driver.find_element_by_class_name('price').text

search('L')
print(get_stock_address())
print(get_last_price())
time.sleep(3)
driver.quit()
