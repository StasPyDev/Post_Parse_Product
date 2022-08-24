import threading

from Parse_Ager.Parse_category.Parse_All_Product import get_all_product_links


def division_process(core: int, file: str):
    pool = threading.BoundedSemaphore(value=core)
    for i in enumerate(file):
        thr = threading.Thread(target=get_all_product_links, args=(url3, i[1].strip(), pool, options), name=f'thr-{i[0]}')
        thr.start()
