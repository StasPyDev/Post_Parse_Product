from Elena_Pokalitsina.Delete_Product.Delete_product import delete
from Elena_Pokalitsina.Update_or_Delete.Update_post import update_to_id
from secret.Secret_Key import api_main


def get_product_to_update_or_delete(update_or_delete):
    api = api_main()
    for i in range(86):
        all_products = api.get('products/', params={'page': f'{1}'}).json()
        for product in all_products:
            product_id = product['id']
            category_group = product.get('categories')[0]
            category = category_group.get('name')
            if update_or_delete == 3:
                if category == 'Взуття':
                    title = product['name'].split()
                    for element in title:
                        if element in ('Лофери', 'Сапоги', 'Черевики', 'Кеди'):
                            update_to_id(product_id=product_id, category=element)
                else:
                    update_to_id(product_id=product_id, category=category)
            elif update_or_delete == 5:
                delete(product_id=product_id, api=api)
        print(f'Page {i + 1} done!')
