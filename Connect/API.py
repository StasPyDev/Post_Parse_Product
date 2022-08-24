from woocommerce import API


# Підключення до сайту
def connect_woocommerce(url, user_key, secret_key) -> API:
    wcapi = API(
        url=url,
        consumer_key=user_key,
        consumer_secret=secret_key,
        version='wc/v3',
        timeout=400
    )

    return wcapi
