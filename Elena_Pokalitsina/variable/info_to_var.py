# Отримання інформації для варіації продукта
def get_info_to_variation(list_group_id, files):
    # files = product_info.get_file()

    data = []

    for file in files:
        group_id = file.get('Group_id')
        if group_id == list_group_id:
            add_data = []
            if file.get('Available') == 'true':
                stock_status = 'instock'
            else:
                stock_status = 'outofstock'
            for param in file.get('Params'):
                name = param.get('Name')
                option = param.get('Option')
                add_data.append({"name": f"{name}",
                                 "option": f"{option}"})

        else:
            continue
        # ["Options: {Size, M...}, "stock_status": instock]
        data.append({"Options": add_data,
                     "stock_status": stock_status})

    return data
