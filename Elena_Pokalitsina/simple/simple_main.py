import json

from Elena_Pokalitsina.INFO import product_info
from Elena_Pokalitsina.list_product import create_listing


# Загрузка товару без варіації на сайт
def post_simple_product(number, api, type, category_info, file):
    try:
        info_to_product = product_info.get_product_info(number=number, file=file)
        create_listing.new_listing(api=api, type=type, info=info_to_product, number=number,
                                   category_info=category_info, file=file)
    except json.JSONDecodeError as err:
        print(err)
