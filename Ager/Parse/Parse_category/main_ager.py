import json

from Ager.Parse.Parse_category.Parse_All_Product import start_parse_info
from Ager.Parse.Parse_category.Parse_menu import get_menu
from Ager.Parse.Parse_category.Requests_page.html_page import get_page


def save_file(deta: list, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(deta, file, indent=4, ensure_ascii=False)


def parse_separate_category(menu_link):
    data = []
    print(f"-----{menu_link.get('Name')}-----")
    soup = get_page(url=menu_link.get('Link_menu'))
    data_info = start_parse_info(soup=soup, url=menu_link.get('Link_menu'))
    for info in data_info:
        data.append(info)
    return data


def start_parse(url: str, file: str):
    global data
    soup = get_page(url=url)
    menu_links = get_menu(soup=soup)
    get_count = int(input(f'Which category to run for a collection?\n1. Жіночий одяг\n2. Чоловічий одяг'
                          f'\n3. Новинки одягу\n4. Аксесуари\n5. Розпродаж одягу\n6. Взуття'
                          f'\n(0 - Parse all category)\n'))
    for menu_link in menu_links:
        match get_count:
            case 1 if menu_link['Name'] == 'Жіночий одяг':
                data = parse_separate_category(menu_link=menu_link)
            case 2 if menu_link['Name'] == 'Чоловічий одяг':
                data = parse_separate_category(menu_link=menu_link)
            case 3 if menu_link['Name'] == 'Новинки одягу':
                data = parse_separate_category(menu_link=menu_link)
            case 4 if menu_link['Name'] == 'Аксесуари':
                data = parse_separate_category(menu_link=menu_link)
            case 5 if menu_link['Name'] == 'Розпродаж одягу':
                data = parse_separate_category(menu_link=menu_link)
            case 6 if menu_link['Name'] == 'Взуття':
                data = parse_separate_category(menu_link=menu_link)
            case 0:
                data = parse_separate_category(menu_link=menu_link)

    save_file(deta=data, file_name=file)
