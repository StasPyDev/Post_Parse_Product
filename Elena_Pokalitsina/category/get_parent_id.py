# Дізнаємося ID яке підходить категорії
def get_id(name, api, parent_id):
    get_category_id = api.get('products/categories/', params={'per_page': 100}).json()

    for category_list in get_category_id:
        if category_list.get('name') == name and category_list.get('parent') == parent_id:
            parent_id = category_list.get('id')
            return parent_id
