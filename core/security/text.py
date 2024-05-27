import os
import mysql.connector
from cryptography.fernet import Fernet

class Passwd:
    def __init__(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="friday"
        )

        cursor = db.cursor()

        cursor.execute("SELECT key_value FROM `key` WHERE key_name = 'my_key'")
        result = cursor.fetchone()
        self.__key = result[0] if result else None

        cursor.execute("SELECT key_value FROM `key` WHERE key_name = 'my_password'")
        result = cursor.fetchone()
        self.__real_password = result[0] if result else None