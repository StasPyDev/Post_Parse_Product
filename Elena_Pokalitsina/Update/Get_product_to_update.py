from Elena_Pokalitsina.Update.Update_post import update_to_id
from secret.Secret_Key import api_main


def get_product_to_update():
    api = api_main()
    page = 1
    for i in range(page):
        all_products = api.get('products/', params={f'page': {i + 1}}).json()
        for product in all_products:
            product_id = product['id']
            print(product_id)
            category_group = product.get('categories')[0]
            category = category_group.get('name')
            update_to_id(product_id=product_id, category=category)
    page += 1

