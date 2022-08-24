# Добавляє нові категорії на сайт
def post_category(api, name_category, parent_id):
    data = {
        'name': name_category,
        'parent': parent_id
    }

    create_category = api.post('products/categories', data).json()

    return create_category
