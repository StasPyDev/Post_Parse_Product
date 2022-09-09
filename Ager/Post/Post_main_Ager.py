import json

from Ager.Post.Post_site import post


def open_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        src = json.load(file)

    return src


def post_product(file, api):
    files_info = open_file(file=file)

    for id_product, file_info in enumerate(files_info):
        # get_post_product = api.get('products/', params={'search': file_info['Title']}).json()
        # for get_post in get_post_product:
        #     if get_post['status'] == 'publish':
        #         if id_product % 100 == 0:
        #             print(f'Done {id_product}')
        #         continue
        #     else:
        if id_product >= 1466:
            post(info=file_info, api=api)
            print(f'--{id_product}-- is {len(files_info)} Done!')
