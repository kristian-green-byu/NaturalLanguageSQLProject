import mysql.connector
import config

class Db:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=config.db_host,
            user=config.db_user,
            password=config.db_password
        )
        if not self.connection.is_connected():
            raise ConnectionError("Could not connect to database")
        self.make_db()

    def make_db(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS cs452_bank")
        cursor.close()

    def make_tables(self) -> None:
        cursor = self.connection.cursor()
        