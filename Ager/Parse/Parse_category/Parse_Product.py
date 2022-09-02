# Зображення товару
def get_image(soup):
    global span_image_block
    data_image = []
    try:
        span_image_block = soup.find('div', class_='product-image vertical_carusel').find_all('span')
    except Exception:
        pass

    for link_img in span_image_block:
        image = link_img.get('data-zoom-image')
        alt = link_img.find('img').get('title')
        data_image.append({'src': image,
                           'alt': alt})

    return data_image


# Назва товару та категорії
def get_name_and_category(soup):
    global model_id, get_name, get_category
    try:
        get_name = soup.find('h1', class_='h1_product').get_text()
        model_id = get_name.split()[-1]
    except Exception:
        pass
    try:
        get_category = soup.find('ul', class_='breadcrumb_ager').find_all('li')
    except Exception:
        pass

    name_category = [name.get_text().strip() for name in get_category]
    name_category.pop(0)
    name_category.pop(-1)
    return get_name, name_category, model_id


# Ціна, первинні параметри товару
def price_block(soup):
    global param_size, available
    model = soup.find('div', class_='description').find('div', class_='description_items')
    group_id = model.find('strong').get_text()
    quantity = [quan.get_text().strip() for quan in model][-1]
    try:
        available = model.find('b', class_='text-danger').get_text()
    except Exception:
        pass
    try:
        block_param = soup.find('div', class_='select-size').find_all('span')
        param_size = [param.get_text().strip() for param in block_param]
    except Exception:
        pass

    block_price = soup.find('div', class_='price').find_all('span')
    price = [price.get_text().strip() for price in block_price]
    return group_id, quantity, price, param_size


# Додаткова інформація про товар
def params_block(soup):
    global block_description
    try:
        block_description = soup.find('div', id='tab-description')
    except Exception as ex:
        pass

    block_params = soup.find('div', id='tab-attribute').find('tbody').find_all('tr')
    data_params = []
    for param in block_params:
        tds = param.find_all('td')
        data = []
        for td in tds:
            if td.get_text() in ('Група кольору', 'Доставка', 'Оплата', 'Повернення'):
                break
            else:
                data.append(td.get_text())
        if data:
            data_params.append({
                'Name': data[0],
                'Option': data[1]
            })
        else:
            continue

    return data_params, block_description


# Таблиця з розмірами
def columns_size(soup):
    try:
        block_column = soup.find_all('table', class_='attribute')

        return block_column[-1]
    except Exception as ex:
        print(ex)


def start_parse_page_prd(soup, url):
    links_image = get_image(soup=soup)
    name, category, model_id = get_name_and_category(soup=soup)
    group_id, quantity, price, size_params = price_block(soup=soup)
    params, description = params_block(soup=soup)
    block_column_size = columns_size(soup=soup)
    data = {
        'Group_id': group_id,
        # 'Available': available,
        'URL': url,
        'Price': price[0].split()[0],
        'Title': name,
        'Vendor': 'Ager',
        'Model_num': model_id,
        'Description': f'{description}',
        'Category': category,
        'Images': links_image,
        'Params': params,
        'Size_Params': size_params,
        'Block_size': f'{block_column_size}'
    }

    return data
