#!/usr/bin/env python3
#######################################
#@utor: Edson Araújo                 ##
#@mail: edsonlead@gmail.com          ##
#       <3                           ##
#######################################

import requests
import numpy as np
from bs4 import BeautifulSoup

URL = "http://www.portaltransparencia.gov.br/PortalComprasDiretasOEOrgaoSubordinado.asp?Ano=%i&CodigoOS=%s"
ANOS = range(2004, 2018)
BILHAO = 1000000000.0

"""
    CÓDIGOS
    Presidência República: 20000
    Ciência e Tec: 24000
    Educação: 26000
    Previdência Social: 33000
    Saúde: 36000
    Meio Ambiente: 44000
    Esporte: 51000
"""

def get_valores(codigo):
    values = []
    for ano in ANOS:
        url = URL %(ano, codigo)
        rq = requests.get(url)
        html = BeautifulSoup(rq.content, "html.parser")
        data = html.find_all("td", {"class":"colunaValor"})
        data = data[1]
        data = data.get_text().strip()
        data = (str(data).replace(".",""))
        data = (str(data).replace(",","."))
        print(data)
        values.append(float(data))
    print(values)
    return np.array(values)/BILHAO


#get_valores(20000)
