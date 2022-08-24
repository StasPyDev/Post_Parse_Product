import json

from INFO import product_info
from list_product import create_listing
from variable import info_to_var


# До загрузка варіацій для товару
def post_var_product(number, api, type, count, category_info):
    try:
        info_to_product = product_info.get_product_info(number=number)
        new_product = create_listing.new_listing(api=api, type=type, info=info_to_product, number=number, category_info=category_info)

        info_product = new_product.get('message')
        if info_product == 'Неверный или дублированный артикул.':
            pass
        else:
            parent_product_id = new_product.get('id')
            for id_var, var_param in enumerate(info_to_var.get_info_to_variation(list_group_id=number)):
                option = var_param.get('Options')
                stock_status = var_param.get('stock_status')
                data = {
                    'regular_price': info_to_product.get('Price'),
                    'attributes': option,
                    'stock_status': stock_status
                }

                new_variable = api.post(f'products/{parent_product_id}/variations', data).json()
                print(f'-{id_var + 1}-{count}-{new_variable}')
            print('Variable product is DONE!!!!')

    except json.JSONDecodeError as err:
        print(err)
