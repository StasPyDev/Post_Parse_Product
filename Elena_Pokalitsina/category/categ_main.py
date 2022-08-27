from Elena_Pokalitsina.category.categ_selenium import get_name_category
from Elena_Pokalitsina.category.get_category_requests import start_parse
from Elena_Pokalitsina.category.get_parent_id import get_id
from Elena_Pokalitsina.category.post_category import post_category


def category_main(link, api):
    global data_category

    select = int(input('What do you want:\n1. Start part to Selenium\n2. Start parse to Requests\n'))

    if select == 1:
        data_category = get_name_category(link=link)
    elif select == 2:
        data_category = start_parse(link=link)
    category_name = ''
    parent_id = 0

    for category in data_category:
        result = post_category(api=api, name_category=category, parent_id=parent_id)

        message = result.get('message')

        if message is None:
            parent_id = result.get('id')
            category_name = category
        elif message is not None:
            parent_id = get_id(name=category, api=api, parent_id=parent_id)
            category_name = category

    return category_name, parent_id
