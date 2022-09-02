from Distribution_of_Category.category_main import distribution
from secret.Secret_Key import api_main


def update_to_id(product_id, category):
    api = api_main()
    category_id = distribution(category=category, api=api)
    data = {
        'categories': [{'id': f'{category_id}'}]
    }
    put = api.put(f"products/{product_id}", data).json()
    print(f'{put["id"]} - {put["name"]}')
