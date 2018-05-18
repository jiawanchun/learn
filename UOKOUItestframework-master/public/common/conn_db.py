# -*- coding: utf-8 -*-
import pymssql
from config import globalparam

def execute(sql,is_fetchone=True):
    # Connect to the database
    connection = pymssql.connect(host=globalparam.DB_HOST,
                                 port=globalparam.DB_PORT,
                                 user=globalparam.DB_USER,
                                 password=globalparam.DB_PASSWORD,
                                 charset="UTF-8")
    # database=globalparam.DB_DATABASE,
    # cursorclass=pymssql.cursors.DictCursor  这个参数 sqlserver 无法使用
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    finally:
        connection.close()