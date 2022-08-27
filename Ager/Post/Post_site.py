from Ager.Post.Attributes_param import get_attribute_param
from Ager.Post.SEO import get_seo_product


def post(info, api):
    data = {
        'name': info.get('Title'),
        'type': 'simple',
        'sku': info.get('Model_num'),
        'regular_price': info.get('Price'),
        'description': f"{info.get('Description')}\n{info.get('Block_size')}",
        'images': info.get('Images'),
        # 'categories': [{'id': category_info.get('Category_id')}],
        # 'tags': [{'name': category_info.get('Category_name')}],
        'attributes': get_attribute_param(info=info),
        'meta_data': get_seo_product(info=info)
    }
    r = api.post('products', data).json()
    return r
