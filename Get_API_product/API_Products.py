from secret.Secret_Key import api_main


def get_products():
    api = api_main()
    product = api.get('products/').json()

    return product['sku']
