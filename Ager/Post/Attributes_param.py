def get_attribute_param(info: dict) -> list:
    param_data = []
    for param in info.get('Params'):
        param_data.append({
            'name': param.get('Name'),
            "visible": "true",
            'options': [param.get('Option')]
        })
    param_data.append(get_size_param(info=info))
    return param_data


def get_size_param(info: dict) -> dict:
    if len(info.get('Size_Params')) == 1:
        return {'name': 'Розмір', 'visible': 'true', 'variation': 'true', 'options': info.get('Size_Params')[0]}
    else:
        return {'name': 'Розмір', 'visible': 'true', 'variation': 'true', 'options': info.get('Size_Params')}
