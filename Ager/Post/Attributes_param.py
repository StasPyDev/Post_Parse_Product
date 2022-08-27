def get_attribute_param(info):
    param_data = []
    for param in info.get('Params'):
        param_data.append({
            'name': param.get('Name'),
            "visible": "true",
            'options': [param.get('Option')]
        })
    return param_data
