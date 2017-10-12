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


url1 = "http://www.portaltransparencia.gov.br/PortalComprasDiretasOEOrgaoSubordinado.asp?Ano="
url2 = "&CodigoOS="

year = list(range(2004,2018))
dataArr = []
bi = 1000000000.0

#Presidência República: 20000
#Ciência e Tec: 24000
#Educação: 26000
#Previdência Social: 33000
#Saúde: 36000
#Meio Ambiente: 44000
#Esporte: 51000


def datas(k,c):
    for i in year:
        url = url1+str(i)+url2+str(k)
        req = requests.get(url)
        bsObj = BeautifulSoup(req.content, "html.parser")
        data1 = bsObj.find_all("td", {"class":"colunaValor"}, limit=2)
        data2 = (str(data1).replace("[<td class=\"colunaValor\">",""))
        data2 = (str(data2).replace("<td class=\"colunaValor\">",""))
        data2 = (str(data2).replace("</td>",""))
        data2 = (str(data2).replace("]",""))
        data2 = (str(data2).replace(".",""))
        data2 = (str(data2).replace("\r\n",""))
        data2 = (str(data2).replace(" ",""))
        data2 = re.sub(r"^[0-9]*\,[0-9]*\,","", data2)
        data2 = (str(data2).replace(",","."))

        dataArr.append(data2)

        
    dataArr = [float(j) for j in dataArr]
    dataArr = np.array(dataArr)
    dataArr = dataArr/c
    print(dataArr)
    return dataArr


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
    plt.plot(year, mPreR, label="Presidência da República")
    plt.plot(year, mCien, label="Ciência e Tecnologia")
    plt.plot(year, mEduc, label="Educação")
    plt.plot(year, mPreS, label="Previdência Social")
    plt.plot(year, mSaud, label="Saúde")
    plt.plot(year, mMeiA, label="Meio Ambiente")
    plt.plot(year, mEspo, label="Esporte")
    
    legend = plt.legend(bbox_to_anchor=(1.01, 1),loc=2, fontsize=12, borderaxespad=0.)
    legend.get_frame().set_facecolor('#ffffff')
    
    #plt.rcParams["figure.figsize"] = [15,7]
    #plt.savefig("educ-sau.png")
    plt.show()


mPreR = datas(20000, bi)
mCien = datas(24000, bi)
mEduc = datas(26000, bi)
mPreS = datas(33000, bi)
mSaud = datas(36000, bi)
mMeiA = datas(44000, bi)
mEspo = datas(51000, bi)


plotCost(mPreR, "Presidência da República")
plotCost(mCien, "Ciência e Tecnologia")
plotCost(mEduc, "Educação")
plotCost(mPreS, "Previdência Social")
plotCost(mSaud, "Saúde")
plotCost(mMeiA, "Meio Ambiente")
plotCost(mEspo, "Esporte")

plotCostAll()
