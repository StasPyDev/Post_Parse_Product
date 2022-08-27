from Ager.Parse.Parse_category.main_ager import start_parse
from Ager.Post.Post_main_Ager import post_product
from secret.Secret_Key import api_main


def ager_main():
    second_select = int(input('Choose an action: \n1. Post\n2. Parse\n'))
    file = 'INFO_Product_Ager.json'
    if second_select == 1:
        post_product(file=file, api=api_main())
    elif second_select == 2:
        start_parse(url='https://ager.ua/uk/', file=file)
