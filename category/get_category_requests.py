import requests
from bs4 import BeautifulSoup

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


def get_html(link):
    r = requests.get(url=link, headers=HEADERS)
    return r.text


def get_parse_page_to_category(html):
    soup = BeautifulSoup(html, 'lxml')

    block_category = soup.find('ul', class_='breadcrumb')
    li_categorys = block_category.find_all('li')
    all_li_category = []
    for li in li_categorys:
        text_category = li.text.strip()
        all_li_category.append(text_category)

    all_li_category.pop(0)
    all_li_category.pop(-1)

    return all_li_category


def start_parse(link):
    html = get_html(link=link)
    bs = get_parse_page_to_category(html=html)
    return bs
