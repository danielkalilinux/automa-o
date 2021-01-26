# automação

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyautogui as cursor





perg = str(input('difite aquii: '))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com.br/')
time.sleep(5)

cursor.write('{}'.format(perg))
cursor.press("enter")
