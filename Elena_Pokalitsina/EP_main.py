from Elena_Pokalitsina.First_stage import read_file, post_product, create_category


def ep_main():
    second_select = int(input('Choose an action: \n1. Post\n2. Create category\n'))
    file = 'INFO_Product_2.json'
    if second_select == 1:
        files = read_file(file_name=file)
        post_product(file=files)
    elif second_select == 2:
        files = read_file(file_name=file)
        create_category(file=files)
