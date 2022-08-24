import pymysql
from sshtunnel import SSHTunnelForwarder

from secret.data_DB import *

try:
    server = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=user,
        ssh_password=password,
        remote_bind_address=(host, port)
    )
    server.start()

    connection = pymysql.connect(
        host=host,
        port=server.local_bind_port,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    print("Successfully connected...")
    print("#" * 20)
    cursor = connection.cursor()
    with cursor:

        select = ('SELECT * FROM wp_pmxi_images;')
        cursor.execute(select)
        get_article = cursor.fetchall()

        for i in enumerate(get_article):
            id_pr = i[1].get('id')
            num = i[0]+1
            print(num, id_pr)

except Exception as ex:
    print("Connection refused...")
    print(ex)
