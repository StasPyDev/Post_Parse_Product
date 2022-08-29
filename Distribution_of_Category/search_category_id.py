def search_category(name_category, api):
    get_category_id = api.get('products/categories/', params={'per_page': 100}).json()

    for category_list in get_category_id:
        if category_list.get('name').lower() == name_category:
            parent_id = category_list.get('id')
            return parent_id