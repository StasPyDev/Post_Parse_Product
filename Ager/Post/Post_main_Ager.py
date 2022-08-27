import json

from Ager.Post.Post_site import post


def open_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        src = json.load(file)

    return src


def post_product(file, api):
    files_info = open_file(file=file)

    for file_info in files_info:
        post(info=file_info, api=api)
