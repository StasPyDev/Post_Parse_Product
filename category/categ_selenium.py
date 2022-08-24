from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')


def get_name_category(link):
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\Stas2\\PycharmProjects\\Product_ElenaPokalitsina\\category\\chromedriver\\chromedriver.exe',
        options=options)

    driver.get(url=link)
    try:
        # Закриває банер з оголошенням
        try:
            button = driver.find_element(By.CLASS_NAME, 'close')
            button.click()
        except Exception as ex2:
            print(ex2)

        data_category = []

        ul_category = driver.find_element(By.CLASS_NAME, 'breadcrumb')
        li_name = ul_category.find_elements(By.TAG_NAME, 'li')
        # Наповнення списку категоріями
        for category in li_name:
            data_category.append(category.text)
        # Видалення непотрібних елементів з категорії
        data_category.pop(0)
        data_category.pop(-1)

        return data_category
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
