#Monitora a Velocidade da Internet salvando os dados num arquivo excel
#projeto adaptado de: https://www.linkedin.com/posts/barbaragfigueiredostatistics_faz-um-tempo-que-tenho-notado-a-velocidade-activity-6783124228955766784-fUmv
import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as np
from threading import Timer

def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [data_atual, hora_atual, velocidade]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)
    print('dado salvo, data:{} , hora:{}'.format(data_atual,hora_atual))
    #Timer definido a cada 10min
    Timer(600, internet).start()


def beginner():
    try:
        internet()
    except Exception as e:
        print('Erro: {}\n'.format(e))
        beginner()


beginner()

