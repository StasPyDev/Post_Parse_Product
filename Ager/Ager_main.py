import json

from Ager.Parse.Parse_category.Parse_Main_Ager import start_parse
from Ager.Post.Post_main_Ager import open_file
from Ager.Post.Post_main_Ager import post_product
from secret.Secret_Key import api_main


def ager_main():
    second_select = int(input('Choose an action: \n1. Post\n2. Parse\n3. Get info all category\n'))
    file = 'INFO_Product_Ager.json'
    if second_select == 1:
        post_product(file=file, api=api_main())
    elif second_select == 2:
        start_parse(url='https://ager.ua/uk/', file=file)
    elif second_select == 3:
        get_all_category(file=file)


def get_all_category(file):
    data_category = []
    file_data = open_file(file)
    for category in file_data:
        if len(category.get('Category')) == 0:
            pass
        else:
            if category.get('Category')[-1] not in data_category:
                data_category.append(category.get('Category')[-1])

    with open('INFO_Category_Ager.json', 'w', encoding='utf-8') as files:
        json.dump(data_category, files, indent=4, ensure_ascii=False)
