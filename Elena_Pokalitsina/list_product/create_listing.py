from Elena_Pokalitsina.INFO import product_info


# Загрузка товару на сайт(не варіації товару)
def new_listing(api, type, info, number, category_info):
    options = product_info.options_to_product(number)
    var_size = [x.get('option_size') for x in options]
    var_color = [x.get('option_color') for x in options]

    data = {
        'name': info.get('Title'),
        'type': type,
        'sku': info.get('Model_num'),
        'regular_price': info.get('Price'),
        'description': info.get('Description'),
        'images': info.get('Image'),
        'categories': [{'id': category_info.get('Category_id')}],
        'tags': [{'name': category_info.get('Category_name')}],
        'attributes': [{
            "name": 'Розмір',
            "visible": "true",
            "variation": "true",
            "options": var_size[0]
        },
            {
                "name": 'Колір',
                "visible": "true",
                "variation": "true",
                "options": var_color[0]
            },
            {
                "name": "Виробник",
                "visible": "true",
                "options": [info.get("Vendor")]
            }]
    }
    r = api.post('products', data).json()
    return r
