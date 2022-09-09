def get_seo_product(info):
    seo_data = [{
        'key': "_yoast_wpseo_focuskw",
        'value': f"{'' if not info.get('Category') else info.get('Category')[-1]}"
        },
        {
        'key': "_yoast_wpseo_metadesc",
        'value': info.get('Title')
    }]
    return seo_data
