import json
import time

from Elena_Pokalitsina.Get_First_INFO import main_post
from Elena_Pokalitsina.category.categ_main import category_main
from secret.Secret_Key import api_main


def create_category(file, save_file):
    api = api_main()
    data_links = []
    data = []
    for link in file:
        link_product = link.get('URL')
        group_id = link.get('Group_id')
        title = link['Title']
        if group_id not in data_links:
            category_name, category_id = category_main(link=link_product, title=title, api=api)
            data_links.append(group_id)
            data.append({
                'Group_id': group_id,
                'Category_id': category_id,
                'Category_name': category_name
            })
        else:
            continue
    print(f'Parse is DONE!')
    save_to_file(file_name=save_file, data=data)


def save_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def post_product(file, file_name):
    data = []
    numbers_data = []
    data_group_id = []
    for info in file:
        group_id = info.get('Group_id')
        if group_id not in data_group_id:
            data_group_id.append(group_id)
        numbers_data.append(group_id)

    for group_id in data_group_id:
        count = 0
        for number in numbers_data:
            if number == group_id:
                count += 1
            else:
                continue

        data.append({'Group_id': group_id,
                     'Count': count})
        count = 0

    for id_count, number in enumerate(data):
        # get_post_product = api_main().get('products/', params=('search': ))
        main_post(number=number, file_name=file_name, file=file)
        print(f'Ready {id_count + 1}')
        if id_count % 100 == 0:
            time.sleep(10)


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        files = json.load(file)
    return files
