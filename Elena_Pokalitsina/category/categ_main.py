from Distribution_of_Category.category_main import distribution
from Elena_Pokalitsina.category.get_category_requests import start_parse


def category_main(link, title, api):
    global category_id
    data_category = start_parse(link=link)
    if data_category == 'Взуття':
        title = title.split()
        for element in title:
            if element in ('Лофери', 'Сапоги', 'Черевики', 'Кеди'):
                category_id = distribution(category=data_category, api=api)
    else:
        category_id = distribution(category=data_category, api=api)

    return data_category, category_id
