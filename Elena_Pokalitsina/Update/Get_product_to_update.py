from Elena_Pokalitsina.Update.Update_post import update_to_id
from secret.Secret_Key import api_main


def get_product_to_update():
    api = api_main()
    page = 1
    for i in range(page):
        all_products = api.get('products/', params={'page': f'{i + 1}'}).json()
        for product in all_products:
            product_id = product['id']
            category_group = product.get('categories')[0]
            category = category_group.get('name')

            if category == 'Взуття':
                title = product['name'].split()
                for element in title:
                    if element in ('Лофери', 'Сапоги', 'Черевики', 'Кеди'):
                        update_to_id(product_id=product_id, category=element)
            else:
                update_to_id(product_id=product_id, category=category)
    page += 1

