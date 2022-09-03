def delete(product_id, api):
    delete = api.delete(f'products/{product_id}', params={'force': True}).json()
