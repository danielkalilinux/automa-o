# atenção o codigo esta em andamento estou armazenando.

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyautogui as cursor
#importei as lib



print('''
         BBBBB    OOOOO  TTTTTTT 
         BB   B  OO   OO   TTT   
         BBBBBB  OO   OO   TTT   
         BB   BB OO   OO   TTT   
         BBBBBB   OOOO0    TTT 
''')

#aqui criei as variaveis
number = 1
helps = 2

#aqui os prints.
print('[1] google hacking')


#aqui o input
entrada = int(input('Oque deseja?: '))
time.sleep(2)


#aqui esta tudo do number = 1
if entrada == number:
    print('\nselecione em que tipo deseja.\n')
    

    #aqui ta as variaveis
    filetype = 1
    site = 2
    intitle = 3
    inurl = 4
    intext = 5

    #aqui esta os prints.
    print('\n[1] filetype\n')
    print('[2] site\n')
    print('[3] inititle\n')
    print('[4] inurl\n')
    print('[5] intext\n')
    entrad = int(input('oque procura?:'))


#aqui esta o if do filetype.
if entrad == filetype:
   
    print('[1] txt\n')
    print('[2] pdf\n')
    print('[3] xls\n')
   
    tipo = int(input('selecione o tipo de arquivo:'))
    txt = 1
    pdf = 2
    xls = 3


#aqui esta o if do site.
if entrad == site:

    tipo0 = str(input('digite o site: '))
   
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com.br/')
    time.sleep(2)

    cursor.write('site: "{}"'.format(tipo0))
    cursor.press("enter")
    exit()
    



#aqui asta o if do intitle.
if entrad == intitle:
    tipo01 = str(input('digite o site: '))
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com.br/')
    time.sleep(2)

    cursor.write('intitle: "{}"'.format(tipo01))
    cursor.press("enter")
    exit()


#aqui esta o if do inurl.
if entrad == inurl:
    tipo02 = str(input('digite o site: '))
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com.br/')
    time.sleep(2)

    cursor.write('inurl: "{}"'.format(tipo02))
    cursor.press("enter")
    exit()


#aqui esta o if do intext
if entrad == intext:
    tipo03 = str(input('digite o site: '))
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com.br/')
    time.sleep(2)

    cursor.write('intext: "{}"'.format(tipo03))
    cursor.press("enter")
    exit()



#-------------------------------------------------------------------------
#pera... aqui ele vai pega o input "tipo".
#aqui esta o if do txt.
if tipo == txt:
    out = str(input('o que deseja? '))
    

    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get('https://www.google.com.br/')
    time.sleep(5)

    cursor.write('filetype:txt "{}"'.format(out))
    cursor.press("enter")

#aqui ele tambem vai pega o input do "tipo".
#aqui esta o if do pdf.
if tipo == pdf:
    outt = str(input('o que deseja? '))
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com.br/')
    time.sleep(5)

    cursor.write('filetype:pdf "{}"'.format(outt))
    cursor.press("enter")


#aqui esta o if do xls
if tipo == xls:
    utt = str(input('o que deseja? '))
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com.br/')
    time.sleep(5)

    cursor.write('filetype:xls "{}"'.format(utt))
    cursor.press("enter")
