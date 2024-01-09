from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging as log
import os
import traceback
import pyautogui as p
from src.Model.get_valor_bitcoin import get_valores_bit
from src.Model.save_valor import save

get_user = os.getlogin()



with open(f'C:/Users/{get_user}/Desktop/RPA_INFORMA_VALORES_DO_BITCOIN/log.txt', 'w') as f:
    pass

log.basicConfig(filename=f'C:/Users/{get_user}/Desktop/RPA_INFORMA_VALORES_DO_BITCOIN/log.txt',level=log.INFO, format=' %(asctime)s - %(levelname)s - %(message)s',
                datefmt='%d/%m/%Y %I:%M:%S %p')
log.info('Iniciando script valores do bitcoin ')
print('inicalizando')
res = True
while res:
    driver = webdriver.Chrome(f'chromedriver.exe')
    navegador = driver
    espera = WebDriverWait(navegador, 60)


    try:

        navegador.get('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved=2ahUKEwiju5_d3f2CAxXcJ7kGHXbKBJsQ-fUHegQIDRAf')    
        navegador.maximize_window()
        valor, ultimo = get_valores_bit(navegador, espera)
        save(valor)
        print('em pause aguarde')
       

    except:
        errro = traceback.format_exc()
        log.info(f'{errro}')
        print(errro)
    finally:
        navegador.quit()
        p.sleep(60)
    
        
