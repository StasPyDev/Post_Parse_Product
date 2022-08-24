# Витягує силки з меню
def get_menu(soup):
    get_block_menu = soup.find('div', class_='megamenu-background')
    ul_menu = get_block_menu.find('ul', class_='megamenu shift-up')
    li_category = ul_menu.find_all('li', class_='with-sub-menu hover desktop-menu')

    data_link_menu = []

    for link_menu in li_category:
        name_link = link_menu.find('a').get_text()
        link = link_menu.find('a').get('href')

        data_link_menu.append({
            'Name': name_link,
            'Link_menu': link
        })

    return data_link_menu
