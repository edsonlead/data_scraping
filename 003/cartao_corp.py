from valid_url import simple_get
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

url = 'http://transparencia.ce.gov.br/content/planejamento-e-execucao-orcamentaria/despesas/cartao-corporativo'
html = simple_get(url)
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')

def get_values(tables):
    for table in tables:
        name_table = table.td.text.strip()
        
        values = table.find_all('td', {'align':'right'})

        if ((values[0].text.strip()) == 'Valor(R$)'):
            values.pop(0)

        result = []

        for v in range(len(values)):
            value = values[v].text.strip()
            value = value.replace('R$ ','')
            value = value.replace('.','')
            value = value.replace(',','.')

            result.append(round(float(value),2))
    
        result.pop(-1)
        
        mean_std(name_table,result)
        sinplot(name_table,result)


def mean_std(name_table,result):
    values_mean = np.mean(result)
    values_std = np.std(result)
    
    print(name_table)
    print('Média de gastos -> R$ {:.2f}'.format(values_mean))
    print('Desvio padrão   ->    {:.2f}'.format(values_std))
    print()
  

def sinplot(name_table, result):
    if (len(result) == 12):
        moths = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

    if (len(result) == 4):
        moths = ['jan','fev','mar','abr']

    x = range(0,len(result))
    
    plt.title(name_table)
    plt.xticks(x,moths)
    plt.xlabel('Mês')
    plt.ylabel('Valor(R$)')
    plt.plot(x,result)
    plt.savefig('images/'+name_table+'.png')
    plt.show()


get_values(tables)
