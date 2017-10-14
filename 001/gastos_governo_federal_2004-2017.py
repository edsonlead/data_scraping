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
        url = URL %(ano, codigo) # Usando sintaxe mais limpa para juntar os valores
        rq = requests.get(url)
        html = BeautifulSoup(rq.content, "html.parser")
        data = html.find_all("td", {"class":"colunaValor"}, limit=2)
        data = r2e(data, "[<td class=\"colunaValor\">")  # Evitando repetição de código usando função externa
        data = r2e(data, "<td class=\"colunaValor\">")
        data = r2e(data, "</td>")
        data = r2e(data, "]")
        data = r2e(data, ".")
        data = r2e(data, "\r\n")
        data = r2e(data, " ")
        data = re.sub(r"^[0-9]*\,[0-9]*\,", "", data)
        data = r2e(data, ",")
        values.append(float(data)) # Convertendo direto o dado pra não ser necessária reiteração
    print(values)
    return np.array(values)/BILHAO # Retornando direto

# Replace de alguma coisa para valor vazio
def r2e(data, pattern):
    return str(data).replace(pattern, "")

def grafico_individual(valores, nome):
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n", fontsize="20")
    plt.xlabel("Ano", fontsize="16")
    plt.ylabel("Em bilhões de R$", fontsize="16")
    plt.plot(ANOS, valores, label=nome)
    legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, fontsize=12, borderaxespad=0.)
    legend.get_frame().set_facecolor('#ffffff')
    plt.show()

def grafico_unificado():
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n", fontsize="20")
    plt.xlabel("Ano", fontsize="16")
    plt.ylabel("Em bilhões de R$", fontsize="16")
    plt.plot(ANOS, v_presidencia, label="Presidência da República")
    plt.plot(ANOS, v_ciencia_tec, label="Ciência e Tecnologia")
    plt.plot(ANOS, v_educacao, label="Educação")
    plt.plot(ANOS, v_prev_social, label="Previdência Social")
    plt.plot(ANOS, v_saude, label="Saúde")
    plt.plot(ANOS, v_meio_ambiente, label="Meio Ambiente")
    plt.plot(ANOS, v_esporte, label="Esporte")
    formatacao_legenda = plt.legend(bbox_to_anchor=(1.01, 1), loc=2, fontsize=12, borderaxespad=0.)
    formatacao_legenda.get_frame().set_facecolor('#ffffff')

    #plt.rcParams["figure.figsize"] = [15,7]
    #plt.savefig("educ-sau.png")
    plt.show()

# Obtendo os valores
v_presidencia = get_valores(20000)
v_ciencia_tec = get_valores(24000)
v_educacao = get_valores(26000)
v_prev_social = get_valores(33000)
v_saude = get_valores(36000)
v_meio_ambiente = get_valores(44000)
v_esporte = get_valores(51000)

grafico_individual(v_presidencia, "Presidência da República")
grafico_individual(v_ciencia_tec, "Ciência e Tecnologia")
grafico_individual(v_educacao, "Educação")
grafico_individual(v_prev_social, "Previdência Social")
grafico_individual(v_saude, "Saúde")
grafico_individual(v_meio_ambiente, "Meio Ambiente")
grafico_individual(v_esporte, "Esporte")

grafico_unificado()
