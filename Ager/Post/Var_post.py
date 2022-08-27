import json

from Ager.Post.Post_first_element import first_element


def post_variable(info, api):
    try:
        post_new_product = first_element(info=info, api=api)
        parent_product_id = post_new_product.get('id')
        info_product = post_new_product.get('message')
        if info_product == 'Неверный или дублированный артикул.':
            pass
        else:
            for size in info.get('Size_Params'):
                data = {
                    'regular_price': info.get('Price'),
                    'attributes': [{'name': 'Розмір',
                                    'option': size}],
                }

                new_variable = api.post(f'products/{parent_product_id}/variations', data).json()

    except json.JSONDecodeError as err:
        print(err)
