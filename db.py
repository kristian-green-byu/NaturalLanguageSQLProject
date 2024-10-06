import mysql.connector
import config
import sql_init

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
        cursor.execute("CREATE DATABASE IF NOT EXISTS cs452_bank;")
        cursor.execute("USE cs452_bank;")
        cursor.close()

    def init_tables(self) ->None:
        self.make_tables()
        self.populate_tables()

    def make_tables(self) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql_init.create_tables, multi=True)
        except mysql.connector.Error as e:
            print(str(e))
        cursor.close()

    def populate_tables(self) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql_init.populate_tables, multi=True)
        except mysql.connector.Error as e:
            print(str(e))
        cursor.execute("SELECT * FROM Transaction")
        for x in cursor:
            print(x)
        cursor.close()

    def execute_statement(self, statement):
        cursor = self.connection.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        cursor.close()
        return result