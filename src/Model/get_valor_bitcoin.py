from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging as log

dict_xpath = {
    'ultimo_lançamento' : '/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/div[2]/div/div[1]/div[2]/div',
    'valor'  :'/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div'
}
def get_valores_bit(navegador, tempo):
    print("esperando carregar pagina")
    log.info("esperando carregar pagina"),

    tempo.until(EC.presence_of_element_located((By.XPATH, dict_xpath['valor'])))

    print('pagina carregada com sucesso ')
    log.info('pagina carregada com sucesso ')
    valor = navegador.find_element(By.XPATH, dict_xpath['valor']).text
    ultimo_lançamento = navegador.find_element(By.XPATH, dict_xpath['ultimo_lançamento']).text

    return valor, ultimo_lançamento
