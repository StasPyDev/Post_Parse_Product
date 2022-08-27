import requests
from bs4 import BeautifulSoup as bs


HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


def get_html(url):
    r = requests.get(url=url, headers=HEADERS)
    return r.text


def soup_html(html):
    soup = bs(html, 'lxml')
    return soup


def get_page(url):
    html_page = get_html(url=url)

    return soup_html(html=html_page)
