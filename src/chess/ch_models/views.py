import requests
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Bank

from bs4 import BeautifulSoup


def welcome(request):
    return render(request, 'welcome.html')

def scrapping(request):

    URL = 'https://rate.am/'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="rb")
    player_list = results.find_all("tr")

    for pl in player_list[2:18]:

        tds = pl.find_all('td')
        for i in range(len(tds)):
            try:
                b = Bank.objects.get(name=tds[3].text)
            except ObjectDoesNotExist:
                b = Bank(name=tds[1].text,
                    branch_count=tds[3].text,
                    usd_buy=tds[5].text,
                    usd_sell=tds[6].text,
                    euro_buy=tds[7].text,
                    euro_sell=tds[8].text)
                b.save()
            else:
                b.usd_buy = tds[5].text
                b.save()


    return HttpResponse()

