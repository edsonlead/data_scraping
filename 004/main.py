import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

URL = "https://saikoanimes.com/legendados/?fwp_paged=%i"
PAGES = range(1,10)
FILE = "list_anime.html"
BOOTSTRAP = "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'>"
CHARSET = "<meta charset='UTF-8'>"
TITLE = "Lista de Animes do Site Saikô"
STYLE_IMG = '<style>img{width:91px;height:130px;margin: 0 auto;}</style>'
SITE = "http://edsonlead.com"
NOW = datetime.now()

fopen = open(FILE, "w")

fopen.write("<html lang='pt-br'><head>{} {} {}</head><title>{}</title><body>".format(BOOTSTRAP,CHARSET,STYLE_IMG,TITLE))
fopen.write("<div class='container'><br /><br />")
fopen.write("<h2 class='text-center'>{}</h2>".format(TITLE))
fopen.write("<h4 class='text-center'>LEGENDADOS</h4>")
fopen.write("<p class='text-center'>[DATA SCRAPING] Post no site: <a href='{}/lista-de-animes-do-site-saiko/' target='_blank'>{}/lista-de-animes-do-site-saiko/</a></p>".format(SITE, SITE))
fopen.write("<p class='text-center'>Última atualização em {}/{}/{} {}h:{}min</p>".format(NOW.day, NOW.month, NOW.year, NOW.hour, NOW.minute))

for i in PAGES:
    url = URL%(i)
    req = requests.get(url)
    html = bs(req.content, "html.parser")
    data = html.find("div",{"class":"anime"}).find("div",{"class":"anime"})
    data_2 = html.find("div",{"class":"anime"}).find_all("div",{"class":"anime"})

    fopen.write("<span class='badge badge-danger'>PÁGINA Nº {}</span>".format(i))
    fopen.write("<table class='table table-striped'>")
    fopen.write("<thead class='thead-dark'><tr><th>ID</th><th>Pôster</th><th>Anime</th><th>Link</th><th>Nota</th></tr></thead>")

    for b in range(len(data_2)):
        data_ = data_2[b]
        name_anime =  data_.find("div",{"class":"listtittle"}).get_text().strip()
        url_anime = data_.find("a").get('href')
        user_score = data_.find("div",{"class":"rwp-users-score"}).find("span",{"class":"rwp-users-score-value"})
        user_score = user_score.get_text()
        image_anime = data_.find("img")

        req_2 = requests.get(url_anime)
        html_2 = bs(req_2.content,"html.parser")
        data_3 = html_2.find("div", {"class":"list"})
        #data_4 = data_3.find_all("a", {"class":"btn-sa"})
        #data_4 = data_3.find_all("a")


        fopen.write("<tr>")
        fopen.write("<td>{}</td>".format(b))
        fopen.write("<td rowspan='2'><p style='text-align: center;'>{}</p></td>".format(image_anime))
        fopen.write("<td>{}</td>".format(name_anime))
        fopen.write("<td><a href='{}' target='_blank'>{}</a></td>".format(url_anime, url_anime))
        fopen.write("<td>{}</td>".format(user_score))
        fopen.write("</tr>")

        fopen.write("<tr><td></td><td colspan='3'>")


        if data_3 is not None:
            data_4 = data_3.find_all("a")
            if data_4 is not None:
                for c in range(len(data_4)):
                    data_c = data_4[c]
                    fopen.write("<span class='btn btn-outline-secondary'>{}</span>\t\t\t".format(data_c))
            if data_4 == []:
                fopen.write("<span class='alert alert-danger' role='alert'>Lista de Episódios Não Encontrada!</span>")

        else:
            fopen.write("<span class='alert alert-danger' role='alert'>Lista de Episódios Não Encontrada!</span>")


        fopen.write("</td></tr>")


    fopen.write("</table><br />")

fopen.write("</div><footer class='footer'><div class='container'>")
fopen.write("<p class='text-center text-muted'>Desenvolvido por: Edson Araújo<br / >Site: <a href='{}'>{}</a></p>".format(SITE, SITE))
fopen.write("</div></footer></body></html>")

fopen.close()
