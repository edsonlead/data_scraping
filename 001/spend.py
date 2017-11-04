import requests
import numpy as np
from bs4 import BeautifulSoup

URL = "http://www.portaltransparencia.gov.br/PortalComprasDiretasOEOrgaoSubordinado.asp?Ano=%i&CodigoOS=%s"
YEARS = range(2004, 2018)
BILLION = 1000000000.0

def get_value(code):
    values = []
    for year in YEARS:
        url = URL %(year, code)
        req = requests.get(url)
        html = BeautifulSoup(req.content, "html.parser")
        data = html.find_all("td", {"class":"colunaValor"})
        data = data[1]
        data = data.get_text().strip()
        data = (str(data).replace(".",""))
        data = (str(data).replace(",","."))
#       print(data)
        values.append(float(data))
#    print(values)
    return np.array(values)/BILLION


#get_value(20000)
