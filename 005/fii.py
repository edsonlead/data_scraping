from bs4 import BeautifulSoup
from valid_url import simple_get
import dryscrape


url = 'https://www.clubefii.com.br/fundo_imobiliario_lista'
new_url = url[:28]
html = simple_get(url)

soup = BeautifulSoup(html, 'html.parser')

table_fii = soup.find('table')

table_tr = table_fii.find_all('tr')
del table_tr[0]

file_tmp = 'fii.tmp'


def fii():

    for td in range(len(table_tr)):
        table_td = table_tr[td].find('td')
        link_fii = table_td.a.get('href')
        code_fii = table_td.text.strip()

        url_fii = new_url+link_fii

        info_fii = url_fii+'#informacoes_basicas'

        html_fii = simple_get(info_fii)

        tmp = open(file_tmp, 'w')
    
        session = dryscrape.Session()
        session.visit(info_fii)
        response = session.body()
        soup_fii = BeautifulSoup(response, 'lxml')
        tmp.write(soup_fii.prettify())
    
        infos_fii = infofii(file_tmp)



def infofii(file_tmp):

    tmp = open(file_tmp, 'r')
    info_fii_tmp = open('info_fii.tmp', 'a+')

    soup = BeautifulSoup(tmp, 'html.parser')

    description = soup.find(id='lbl_des').text.strip()

    table_info = soup.find('table', class_='scroll_bar_grossa_clube_fii')
    table_info_tr = table_info.find_all('tr')

    teste = []

    for tr in range(len(table_info_tr)):
        table_info_td = table_info_tr[tr].find_all('td')

        for info in range(len(table_info_td)):
            infos = table_info_td[info].div.text.strip()
            teste.append(infos)

    code_neg = teste[0]
    abl = teste[3]
    ifix = teste[4]
    cotas = teste[5]
    segmento = teste[8]
    administrador = teste[9]
    gestor = teste[10]

    infos_fii = []
    infos_fii = [code_neg, abl, ifix, cotas, segmento, administrador, gestor]
    
    infos_fii = ' | '.join(infos_fii)
    info_fii_tmp.write(infos_fii+'\n')
    info_fii_tmp.write(description+'\n\n')
    info_fii_tmp.close()



fii()
