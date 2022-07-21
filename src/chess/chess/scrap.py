import requests
from bs4 import BeautifulSoup

from django.http import HttpResponse


URL = 'https://rate.am/'

def check_web_data(request):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #print(soup)

    results = soup.find(id="rb")
    player_list = results.find_all("tr")

    tds = player_list[3].find_all('td')
    for i in range(len(tds)):
        print(i, tds[i].text)
    

    return HttpResponse()

