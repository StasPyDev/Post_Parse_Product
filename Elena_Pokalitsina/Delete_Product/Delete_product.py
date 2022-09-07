def delete(product_id, api):
    api.delete(f'products/{product_id}', params={'force': True, 'search': 'ТМ Elena Pokalitsina'}).json()
