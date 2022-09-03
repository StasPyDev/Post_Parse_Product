import json

from Elena_Pokalitsina.Get_First_INFO import main_post
from Elena_Pokalitsina.category.categ_main import category_main
from secret.Secret_Key import api_main


def create_category(file):
    api = api_main()
    data_links = []
    data = []
    for link in file:
        link_product = link.get('URL')
        group_id = link.get('Group_id')
        if group_id not in data_links:
            category_name, category_id = category_main(link=link_product, api=api)
            data_links.append(group_id)
            data.append({
                'Group_id': group_id,
                'Category_id': category_id,
                'Category_name': category_name
            })
        else:
            continue
    print(f'Number is DONE!')

    with open('INFO_Category_EP.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def post_product(file):
    data = []
    numbers_data = []
    data_numbers = []
    for group_id in file:
        group_id = group_id.get('Group_id')
        if group_id not in data_numbers:
            data_numbers.append(group_id)
        numbers_data.append(group_id)

    for group_id in data_numbers:
        count = 0
        for number in numbers_data:
            if number == group_id:
                count += 1
            else:
                continue

        data.append({'Group_id': group_id,
                     'Count': count})
        count = 0

    for number in data:
        main_post(number=number)


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        files = json.load(file)
    return files
