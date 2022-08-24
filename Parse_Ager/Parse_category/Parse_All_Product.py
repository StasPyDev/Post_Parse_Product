from Parse_Ager.Parse_category.Parse_Product import start_parse_page_prd
from Parse_Ager.Parse_category.Requests_page.html_page import get_page


# Отримання кількість сторінок в категорії
def get_numeration(soup):
    paginations = soup.find('div', class_='row pagination-results').find('ul', class_='pagination')
    counts_page = int(paginations.find_all('li')[-1].find('a').get('href').split('/')[-2].split('page-')[-1])
    return counts_page


# Створення силок на всі сторінки з данної категорії
def pagination_page(counts_page, url):
    data_urls = []
    for count in range(counts_page):
        create_url = f'{url}page-{count + 1}'
        data_urls.append(create_url)
    return data_urls


# Отримання силок на товари
def get_all_product_links(pages):
    data = []
    for page in pages:
        soup = get_page(url=page)
        products_block = soup.find('div', id='mfilter-content-container').find_all('div', class_='col-md-3 col-sm-4 col-xs-6')
        for product in products_block:
            data.append(product.find('div', class_='name').find('a').get('href'))

    return data


def start_parse_info(soup, url):
    count = get_numeration(soup)
    page_all_products = pagination_page(counts_page=count, url=url)
    product_links = get_all_product_links(pages=page_all_products)
    data = []

    for id, product_link in enumerate(product_links):
        soup_product = get_page(url=product_link)
        product_soup = start_parse_page_prd(soup=soup_product, url=product_link)
        data.append(product_soup)
        # if id % 100 == 0:
        print(f'---Product-{id} to {len(product_links)} done!---')
    return data
