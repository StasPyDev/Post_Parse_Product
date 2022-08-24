import json

from INFO import product_info
from list_product import create_listing


# Загрузка товару без варіації на сайт
def post_simple_product(number, api, type, category_info):
    try:
        info_to_product = product_info.get_product_info(number=number)
        create_listing.new_listing(api=api, type=type, info=info_to_product, number=number, category_info=category_info)
        print('Simple product is DONE!!!')
    except json.JSONDecodeError as err:
        print(err)
