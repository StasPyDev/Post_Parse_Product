import json

from Parse_Ager.Parse_category.Parse_All_Product import start_parse_info
from Parse_Ager.Parse_category.Parse_menu import get_menu
from Parse_Ager.Parse_category.Requests_page.html_page import get_page


def save_file(deta: list):
    with open('INFO_Product_Ager.json', 'w', encoding='utf-8') as file:
        json.dump(deta, file, indent=4, ensure_ascii=False)


def start_parse(url: str):
    data = []
    soup = get_page(url=url)
    menu_links = get_menu(soup=soup)
    get_count = int(input(f'How links to go? {len(menu_links)}: '))
    for menu_link in menu_links[:get_count + 1]:
        print(f"-----{menu_link.get('Name')}-----")
        soup = get_page(url=menu_link.get('Link_menu'))
        data_info = start_parse_info(soup=soup, url=menu_link.get('Link_menu'))
        for info in data_info:
            data.append(info)
    save_file(deta=data)
