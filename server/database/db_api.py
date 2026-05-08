import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, path: str = "tiPhone.db") -> None:
        self.connection = sqlite3.connect(path)
        #self.cursor = self.connection.cursor()
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                create table if not exists Users(
                    pk_id integer primary key,
                    username text unique,
                    display_name text,
                    first_name text,
                    last_name text,
                    tiphone_number text,
                    secret_hash text,
                    password_hash text
                );
            """)
            self.connection.commit()
        except Error:
            self.connection.rollback()
        finally:
            cursor.close()


    def add_user(self, username: str) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                insert into Users(username) values (?);               
            """, (username))
            self.connection.commit()
        except Error:
            self.connection.rollback()
        finally:
            cursor.close()

    
    def update_user_data(self, id: int, username: str, display_name: str, first_name: str, last_name: str):
        pass


    def change_user_password(self, id: int, password: str):
        pass


    def change_user_secret(self, id: int):
        pass
