def get_seo_product(info, category_info):
    seo_data = [{
        'key': "_yoast_wpseo_focuskw",
        'value': category_info.get('Category_name')
    },{
        'key': "_yoast_wpseo_metadesc",
        'value': info.get('Title')
    }]
    return seo_data
