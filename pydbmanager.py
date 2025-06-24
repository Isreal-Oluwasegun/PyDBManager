import mysql.connector

class Database:

    """
    Library Module
    ==============

    This module provides a class to interact with a MySQL database. It allows users to create databases and tables, 
    execute SELECT queries, and perform INSERT operations dynamically through validated SQL strings.

    Author: Isreal Makinde
    Date: 2025-06-24


    Library database handler for managing MySQL operations.

    Attributes:
        __db (str): Name of the database to connect or create.
        __connection (MySQLConnection): Established connection to the MySQL server.
        __cursor (MySQLCursor): Cursor object to interact with the database.

    Methods:
        create_table(command): Executes a CREATE TABLE SQL command.
        insert_into(command): Inserts records using a valid INSERT INTO SQL command.
        query(command): Runs a SELECT statement and displays results.
    """

    def __init__(self, dbname, host="localhost", user="root", password=None):
        self.__db = dbname
        self.__host = host
        self.__user = user
        self.__password = password
        self.__connection = self.__establish_connection()
        self.__cursor = self.__connection.cursor()
        self.__create_database(self.__db)

    def __establish_connection(self):
        try:
            connection = mysql.connector.connect(
                host = self.__host,
                user = self.__user,
                password = self.__password
                )
            print("Connection successful")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        return connection
    

    def __create_database(self, db):
        self.__db = db
        if self.__connection:
            self.__cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db}; ")
            self.__cursor.execute(f"USE {self.__db};")

    @staticmethod
    def __validate_command(command):
        if isinstance(command, str) and command.strip():
            command = command.lower().strip()
            return command
        else:
            print("invalid input string")
            return None
        
    def create_table(self, command):
        """
        Create a table in the current database using a provided SQL command.

        Args:
            command (str): A valid SQL CREATE TABLE statement.

        Returns:
            None

        Raises:
            RuntimeError: If execution fails or the SQL is invalid.
        """
        command = self.__validate_command(command)
        if self.__connection:
            try:
                if command.startswith("create table"):
                    self.__cursor.execute(command)
                    self.__connection.commit()
                else:
                    print("invalid create command")
                    return None
            except Exception as e:
                return f"cannot perform operation {e}"
            
    def query(self, command):
        """
        Query a table in the current database using a provided SQL command.

        Args:
            command (str): A valid SELECT FROM statement.

        Returns:
            None

        Raises:
            RuntimeError: If execution fails or the SQL is invalid.
        """

        command = self.__validate_command(command)
        
        if self.__connection:
            try:
                if command.startswith("select"):
                    self.__cursor.execute(command)
                    result = self.__cursor.fetchall()
                    for a in result:
                        print(a)
                else:
                    print("invalid select statement")
                    return None
            except Exception as e:
                return f"cannot perform operation {e}"
    
    def insert_into(self, command):
        """
        Insert into a table in the current database using a provided SQL command.

        Args:
            command (str): A valid SQL INSERT INTO statement.

        Returns:
            None

        Raises:
            RuntimeError: If execution fails or the SQL is invalid.
        """ 
        command = self.__validate_command(command)
        if self.__connection:
            try:
                if command.startswith("insert into"):
                    self.__cursor.execute(command)
                    self.__connection.commit()
                else:
                    print("Invalid insert command")
                    return None
            except Exception as e:
                return f"cannot perform operation {e}"
            


if __name__== "__main__":
    db = Database("MyDatabase", password="Makinde0604")
    db.create_table("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(100));")
    db.insert_into("INSERT INTO users (id, name) VALUES (1, 'Isreal');")
    db.query("SELECT * FROM users;")
        