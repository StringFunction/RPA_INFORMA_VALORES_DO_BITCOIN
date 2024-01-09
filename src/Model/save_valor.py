import pandas as pd
from datetime import datetime
import os

get_user = os.getlogin()



def save(valor):
    data_hj = datetime.now()
    hora_sistema = data_hj.strftime('%H:%M')
    data_sistema = data_hj.strftime('%d_%m_%Y')
    if not os.path.exists(f'C:/Users/{get_user}/Desktop/RPA_INFORMA_VALORES_DO_BITCOIN/dados_valores_bitcoin_{data_sistema}.xlsx'):
        print("ola")
        dados = {
            'Data' : [],
            'Hora' : [],
            'valor'  : []
        }
        planilha = pd.DataFrame(dados)
        print(planilha)
        planilha.to_excel(f'C:\\Users\\francisco.clecio\\Desktop\\RPA_INFORMA_VALORES_DO_BITCOIN\\dados_valores_bitcoin_{data_sistema}.xlsx', index=False)
    df = pd.read_excel(f'C:\\Users\\francisco.clecio\\Desktop\\RPA_INFORMA_VALORES_DO_BITCOIN\\dados_valores_bitcoin_{data_sistema}.xlsx')
    registro = {
       'Data' : data_sistema,
       'Hora'  :hora_sistema,
       'valor' : valor
    }
    atualizar = df.append(registro, ignore_index=True)
    df = pd.DataFrame(atualizar)

    df.to_excel(f'C:\\Users\\francisco.clecio\\Desktop\\RPA_INFORMA_VALORES_DO_BITCOIN\\dados_valores_bitcoin_{data_sistema}.xlsx', index=False)

    print(df)



















if __name__=='__main__':
 save('kiajkaj')
