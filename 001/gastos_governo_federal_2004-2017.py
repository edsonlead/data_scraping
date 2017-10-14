#!/usr/bin/env python3
#######################################
#@utor: Edson Araújo                 ##
#@mail: edsonlead@gmail.com          ##
#       <3                           ##
#######################################

import re
import requests
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

reqUrl = "http://www.portaltransparencia.gov.br/PortalComprasDiretasOEOrgaoSubordinado.asp?Ano=%i&CodigoOS=%s"

year = range(2004,2018)
bi = 1000000000.0

#Presidência República: 20000
#Ciência e Tec: 24000
#Educação: 26000
#Previdência Social: 33000
#Saúde: 36000
#Meio Ambiente: 44000
#Esporte: 51000


def datas(k):
    dataArr = []
    for i in year:
        url = reqUrl %(i, k) # Usando sintaxe mais limpa para juntar os valores
        req = requests.get(url)
        bsObj = BeautifulSoup(req.content, "html.parser")
        data1 = bsObj.find_all("td", {"class":"colunaValor"}, limit=2)
        data2 = r2e(data1, "[<td class=\"colunaValor\">")  # Evitando repetição de código usand função externa
        data2 = r2e(data2, "<td class=\"colunaValor\">")
        data2 = r2e(data2, "</td>")
        data2 = r2e(data2, "]")
        data2 = r2e(data2, ".")
        data2 = r2e(data2, "\r\n")
        data2 = r2e(data2, " ")
        data2 = re.sub(r"^[0-9]*\,[0-9]*\,","", data2)
        data2 = str(data2).replace(",",".")

        dataArr.append(float(data2)) # Convertendo direto o dado pra não ser necessária reiteração
    print(dataArr)
    return np.array(dataArr)/bi # Retornando direto

# Replace de alguma coisa para valor vazio
def r2e(data, pattern):
    return str(data).replace(pattern, "")

def plotCost(dataY, nameR):
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n", fontsize="20")
    plt.xlabel("Ano", fontsize="16")
    plt.ylabel("Em bilhões de R$", fontsize="16")
    plt.plot(year, dataY, label=nameR)
    
    legend = plt.legend(bbox_to_anchor=(1.05, 1),loc=2, fontsize=12, borderaxespad=0.)
    legend.get_frame().set_facecolor('#ffffff')
   
    plt.show()

def plotCostAll():
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n", fontsize="20")
    plt.xlabel("Ano", fontsize="16")
    plt.ylabel("Em bilhões de R$", fontsize="16")
    plt.plot(year, v_presidencia, label="Presidência da República")
    plt.plot(year, v_ciencia_tec, label="Ciência e Tecnologia")
    plt.plot(year, v_educacao, label="Educação")
    plt.plot(year, v_prev_social, label="Previdência Social")
    plt.plot(year, v_saude, label="Saúde")
    plt.plot(year, v_meio_ambiente, label="Meio Ambiente")
    plt.plot(year, v_esporte, label="Esporte")
    
    legend = plt.legend(bbox_to_anchor=(1.01, 1),loc=2, fontsize=12, borderaxespad=0.)
    legend.get_frame().set_facecolor('#ffffff')

    #plt.rcParams["figure.figsize"] = [15,7]
    #plt.savefig("educ-sau.png")
    plt.show()

v_presidencia = datas(20000)
v_ciencia_tec = datas(24000)
v_educacao = datas(26000)
v_prev_social = datas(33000)
v_saude = datas(36000)
v_meio_ambiente = datas(44000)
v_esporte = datas(51000)

plotCost(v_presidencia, "Presidência da República")
plotCost(v_ciencia_tec, "Ciência e Tecnologia")
plotCost(v_educacao, "Educação")
plotCost(v_prev_social, "Previdência Social")
plotCost(v_saude, "Saúde")
plotCost(v_meio_ambiente, "Meio Ambiente")
plotCost(v_esporte, "Esporte")

plotCostAll()
