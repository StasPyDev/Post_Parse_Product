import json


# Інформація про всі товари
def get_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        files = json.load(file)

    return files


# Якщо інформація підходить за номером, бере повну інформацію про товар
def get_product_info(number, file):
    # file = get_file(file)
    for element in file:
        if element.get("Group_id") == number:
            return element


# Основні значення товара (Розмір та Колір)
def options_to_product(group_id, file):
    # files = get_file(file)

    data = []
    data_size = []
    data_color = []

    for product_info in file:
        if product_info.get('Group_id') == group_id:
            for number in product_info.get("Params"):
                if number.get("Name") == 'Размер':
                    if number.get('Option') is None:
                        continue
                    else:
                        if number.get('Option') not in data_size:
                            data_size.append(number.get('Option'))
                elif number.get("Name") == 'Цвет':
                    if number.get('Option') is None:
                        continue
                    else:
                        if number.get('Option') not in data_color:
                            data_color.append(number.get('Option'))
        else:
            continue
    data.append({"name_size": "Размер",
                 "option_size": data_size,
                 "name_color": "Цвет",
                 "option_color": data_color})

    return data
