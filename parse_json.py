import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen


def read_xml(site):
    tree = ET.fromstring(site)

    return tree


def param_parse(site):
    data_group_id = []
    data_all_params = []

    for id_offer in site.iter('offer'):
        group_id = id_offer.get('group_id')
        if group_id not in data_group_id:
            data_group_id.append(group_id)

    for param_element in site.iter('offer'):
        param_group_id = param_element.get('group_id')
        params = param_element.findall('param')

        data_params = []

        for param in params:
            name = param.get('name')
            param = param.text

            data_params.append({'name': name,
                                'visible': 'true',
                                'options': param})

        data_all_params.append({'Group_id': param_group_id,
                                'Params': data_params})

    data_par = []
    number = []
    for group_num in data_group_id:
        data_prm = []
        if group_num not in number:
            for data_element in data_all_params:
                if data_element.get('Group_id') == group_num:
                    for param in data_element.get('Params'):
                        if param not in data_prm:
                            data_prm.append(param)
            else:
                data_par.append({'Group_id': group_num,
                                 'Param': data_prm})
                number.append(group_num)
    # print(data_par)

    return data_par


def parse_xml(site):
    data = []

    for element in enumerate(site.iter('offer')):
        element_details = element[1]

        id = element_details.get('id')
        available = element_details.get('available')
        group_id = element_details.get('group_id')

        url_product = element_details.find('url').text
        price_product = element_details.find('price').text
        category_id = element_details.find('categoryId').text
        delivery = element_details.find('delivery').text
        name_product = element_details.find('name').text
        vendor_product = element_details.find('vendor').text
        model_number = element_details.find('model').text
        description = element_details.find('description').text
        images = element_details.findall('picture')
        params = element_details.findall('param')

        data_pictures = []

        for image in enumerate(images):
            data_pictures.append({'src': image[1].text,
                                  'alt': name_product})

        data_params = []

        for param in params:
            name = param.get('name')
            param = param.text
            data_params.append({'Name': name,
                                'Option': param})

        data.append({'ID': id,
                     'Available': available,
                     'Group_id': group_id,
                     'URL': url_product,
                     'Price': price_product,
                     'Category_id': category_id,
                     'Delivery': delivery,
                     'Title': name_product,
                     'Vendor': vendor_product,
                     'Model_num': model_number,
                     'Description': description,
                     'Image': data_pictures,
                     'Params': data_params
                     })
    return data


def save_json(data):
    with open('INFO_Product_2.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def show(file):
    for i in file.iter('offer'):
        print(i.findtext('description'))


def start():
    url_elena_pokalitsina = 'https://elenapokalitsina.com.ua/index.php?route=extension/feed/yandex_yml&currency=UAH'
    url_ager = 'https://ager.ua/download/standart_yml_catalog_roznica.xml'

    read = read_xml(urlopen(url_ager).read())
    show(read)

    # data_collection = parse_xml(read)
    # save_json(data_collection)


if __name__ == '__main__':
    start()
