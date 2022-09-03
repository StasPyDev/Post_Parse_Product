import json

from Elena_Pokalitsina.simple import simple_main
from Elena_Pokalitsina.variable import var_main
from secret.Secret_Key import api_main


# Отримую ID категорії для нового лістингу
def get_category_info(group_id):
    with open('INFO_Category_EP.json', encoding='utf-8') as file:
        files = json.load(file)

    for element in files:
        if element.get('Group_id') == group_id:
            # category_id = distribution(category=element['Category_name'], api=api_main())
            return {'Category_id': element['Category_id'], 'Category_name': element['Category_name']}


# Відправляє данні на лістинг нового товару
def post(number, api):
    group_id = number.get('Group_id')
    number_count = number.get('Count')
    category_info = get_category_info(group_id=group_id)
    # Перевірка на ТИП товару
    if number_count >= 2:
        type = 'variable'
        var_main.post_var_product(number=group_id, api=api, type=type, count=number_count, category_info=category_info)
    else:
        type = 'simple'
        simple_main.post_simple_product(number=group_id, api=api, type=type, category_info=category_info)


def main_post(number):
    api = api_main()
    post(number=number, api=api)
