import sqlite3
import os

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    # Establish a connection to the database
    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    # Execute SQL commands from a script file
    def execute_sql_script(self, script_file):
        with open(script_file, 'r') as file:
            sql_script = file.read()
        self.cursor.executescript(sql_script)
        self.connection.commit()

    #Close the connection to the database
    def close(self):
        self.connection.close()

    #Initialize the database by creating tables and adding dummy data if needed
    def initialize_database(self):
        if not os.path.exists(self.db_name):
            self.connect()
            self.execute_sql_script("script.sql")
            self.close()