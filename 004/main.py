import requests
from bs4 import BeautifulSoup as bs

URL = "https://saikoanimes.com/legendados/?fwp_paged=%i"
PAGES = range(1,10)
FILE = "list_anime.html"
BOOTSTRAP = "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'>"
CHARSET = "<meta charset='UTF-8'>"
TITLE = "Lista Animes do Site Saikô"
SITE = "http://edsonlead.com"

fopen = open(FILE, "w")

fopen.write("<html lang='pt-br'><head>{}{}</head><title>{}</title><body>".format(BOOTSTRAP,CHARSET,TITLE))
fopen.write("<div class='container'>")
fopen.write("<h2 class='text-center'>{}</h2>".format(TITLE))
fopen.write("<h4 class='text-center'>LEGENDADOS</h4>")
fopen.write("<p class='text-center'>[DATA SCRAPING] Post no site: <a href='{}/' target='_blank'>{}</a></p>".format(SITE, SITE))
fopen.write("<p class='text-center'>Última atualização: 10/Dez/2017</p>")

for i in PAGES:
    url = URL%(i)
    req = requests.get(url)
    html = bs(req.content, "html.parser")
    data = html.find("div",{"class":"anime"}).find("div",{"class":"anime"})
    data_2 = html.find("div",{"class":"anime"}).find_all("div",{"class":"anime"})

    fopen.write("PAGE {}".format(i))
    fopen.write("<table class='table table-striped'>")
    fopen.write("<thead class='thead-dark'><tr><th>ID</th><th>Anime</th><th>Download</th><th>Nota</th></tr></thead>")

    for b in range(len(data_2)):
        data_ = data_2[b]
        name_anime =  data_.find("div",{"class":"listtittle"}).get_text().strip()
        url_anime = data_.find("a").get('href')
        user_score = data_.find("div",{"class":"rwp-users-score"}).find("span",{"class":"rwp-users-score-value"})
        user_score = user_score.get_text()

        fopen.write("<tr>")
        fopen.write("<td>{}</td>".format(b))
        fopen.write("<td>{}</td>".format(name_anime))
        fopen.write("<td><a href='{}' target='_blank'>{}</a></td>".format(url_anime, url_anime))
        fopen.write("<td>{}</td>".format(user_score))
        fopen.write("</tr>")


    fopen.write("</table><br />")

fopen.write("<p class='text-center'>Desenvolvido por: Edson Araújo<br / >Site: <a href='{}'>{}</a></p>".format(SITE, SITE))
fopen.write("</div></body></html>")

fopen.close()
