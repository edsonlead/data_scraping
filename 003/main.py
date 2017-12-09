import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

URL = 'http://transparencia.ce.gov.br/content/planejamento-e-execucao-orcamentaria/despesas/cartao-corporativo'

req = requests.get(URL)
html = BeautifulSoup(req.content, 'html.parser')
table = html.find_all('table')

def get_table(n_table):

    moths = []
    values = []
    global titles
    global m
    global v

    for t in range(len(table)):

        if (t == n_table):
            strong = table[t].find('strong')
            title = strong.get_text().strip()
            td = table[t].find_all('td')
            moth = td[1].get_text().strip()
            value = td[2].get_text().strip()

            titles = [title, moth, value]

            rest = td[3:]

            for lines in range(len(rest)):

                if lines % 2 != 0:
                    rest_values = rest[lines].get_text().strip()
                    rest_values = rest_values.replace("R$ ","")
                    rest_values = rest_values.replace(".","")
                    rest_values = rest_values.replace(",",".")
                    values.append(float(rest_values))


                if (lines % 2 == 0):
                    rest_moths = rest[lines].get_text().strip()
                    moths.append(rest_moths)


    v = values
    #m = moths
    new_v = v.pop(-1)
    #new_m = m.pop(-1)

    m = range(len(v))

    m = m
    v = v
    titles = titles

    print(aritmetic(v,titles))
    sinplot(m, v, titles)


def aritmetic(v, titles):
    a_mean = np.mean(v)
    a_std = np.std(v)

    print(titles[0])
    print("Média dos gastos: R$ {}".format(a_mean))
    print("Desvio padrão: R$ {}".format(a_std))

    #return a_mean, a_std


def sinplot(moths, values, titles):
    plt.plot(moths, values, label='Gastos')
    plt.title(titles[0]+"\n")
    plt.xlabel("Mês")
    plt.ylabel("Valor (R$)")
    legend = plt.legend()
    #plt.savefig("images/"+name+".png")
    plt.show()


get_table(0)
get_table(1)
get_table(2)
