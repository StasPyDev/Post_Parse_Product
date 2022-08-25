import json


# Інформація про всі товари
def get_file():
    with open('INFO_Product_Ager.json', 'r', encoding='utf-8') as file:
        files = json.load(file)

    return files


# Якщо інформація підходить за номером, бере повну інформацію про товар
def get_product_info(number):
    file = get_file()
    for element in file:
        if element.get("Group_id") == number:
            return element


# Основні значення товара (Розмір та Колір)
def options_to_product(group_id):
    files = get_file()

    data = []
    data_size = []
    data_color = []

    for file in files:
        if file.get('Group_id') == group_id:
            for number in file.get("Params"):
                if number.get("Name") == 'Размер' or number.get("Name") == 'Розмір':
                    if number.get('Option') is None:
                        continue
                    else:
                        if number.get('Option') not in data_size:
                            data_size.append(number.get('Option'))
                elif number.get("Name") == 'Цвет' or number.get("Name") == 'Колір':
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
