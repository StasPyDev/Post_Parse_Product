import json

from Parse_Ager.Parse_category.main_ager import start_parse
from Post_Products import main_post
from category.categ_main import category_main
from secret.Secret_Key import api_main


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


def create_category(file):
    api = api_main()
    data_links = []
    data = []
    for link in file:
        link_product = link.get('URL')
        group_id = link.get('Group_id')
        if group_id not in data_links:
            category_new_post, category_id = category_main(link=link_product, api=api)
            data_links.append(group_id)
            data.append({
                'Group_id': group_id,
                'Category_id': category_id,
                'Category_name': category_new_post
            })
        else:
            continue
        print(f'Number {group_id} is DONE!')

    with open('INFO_Category_requests.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read_file():
    with open('INFO_Product_Ager.json', 'r', encoding='utf-8') as file:
        files = json.load(file)
    return files


def main():
    print('ver. 1.3')
    select = int(input('Select what are you do:\n1. Post product to API\n2. Create category\n3. Parse category from Ager\n'))

    if select == 1:
        files = read_file()
        post_product(file=files)
    elif select == 2:
        files = read_file()
        create_category(file=files)
    elif select == 3:
        start_parse(url='https://ager.ua/uk/')


if __name__ == '__main__':
    main()
