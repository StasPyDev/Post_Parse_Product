import json

from Elena_Pokalitsina.First_stage import read_file, post_product, create_category
from Elena_Pokalitsina.Update_or_Delete.Get_product_to_update import get_product_to_update_or_delete


def ep_main():
    second_select = int(input('Choose an action: \n1. Post\n2. Create category\n3. Update_or_Delete category\n'
                              '4. Get all categories in file\n5. Delete all products\n'))
    file = 'INFO_Product_2.json'
    if second_select == 1:
        files = read_file(file_name=file)
        post_product(file=files)
    elif second_select == 2:
        files = read_file(file_name=file)
        create_category(file=files)
    elif second_select == 3:
        get_product_to_update_or_delete(update_or_delete=second_select)
    elif second_select == 4:
        files = read_file(file_name='INFO_Category.json')
        get_all_category(file=files)
    elif second_select == 5:
        get_product_to_update_or_delete(update_or_delete=second_select)


def get_all_category(file):
    data = []
    for name in file:
        if name['Category_name'].lower() not in data:
            data.append(name['Category_name'].lower())

    with open('INFO_Category_EP.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
