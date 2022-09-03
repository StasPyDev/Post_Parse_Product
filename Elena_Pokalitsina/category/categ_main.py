from Distribution_of_Category.category_main import distribution
from Elena_Pokalitsina.category.get_category_requests import start_parse


def category_main(link, api):
    data_category = start_parse(link=link)

    category_id = distribution(category=data_category, api=api)

    return data_category, category_id
