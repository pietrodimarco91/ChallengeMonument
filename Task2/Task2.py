__author__='Pietro Di Marco'

from intercom.client import Client
from mysql.connector import MySQLConnection, Error

dbconfig = {
    'user': "root",
    'password': "root",
    'host': "127.0.0.1",
    'port': 3306,
    'database': "Users"
}


def get_users_mysql():
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        query = ("SELECT id, name, email FROM USER")

        cursor.execute(query)
        res = list()
        for (id, name, email) in cursor:
            dict = {
                "id": id,
                "name": name,
                "email": email
            }
            res.append(dict)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return res


if __name__ == '__main__':
    users = get_users_mysql()

    # Configure client
    intercom = Client(personal_access_token='my_personal_access_token')
    #Send data to intercom
    intercom.users.submit_bulk_job(create_items=users)
