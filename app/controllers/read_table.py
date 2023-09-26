import psycopg2
from psycopg2 import extras
import pyodbc
from sqlalchemy import create_engine, URL
from sqlalchemy import text

class DatabaseConnector:
    def __init__(self, driver, connection_settings):
        self.driver = driver
        self.connection_settings = connection_settings
        self.connection = None
        self.connection_functions = {
            "psycopg2": self._connect_psycopg2,
            "pyodbc": self._connect_pyodbc,
            "sqlalchemy": self._connect_sqlalchemy,
        }
        self.execution_functions = {
            "psycopg2": self._execute_query_psycopg2,
            "pyodbc": self._execute_query_pyodbc,
            "sqlalchemy": self._execute_query_sqlalchemy,
        }

    def connect(self):
        if self.driver not in self.connection_functions:
            raise ValueError("Unsupported driver")
        
        self.connection = self.connection_functions[self.driver]()

    def execute_query(self, query):
        if self.connection is None:
            raise Exception("Connection not established. Call connect() first.")
        
        return self.execution_functions[self.driver](query)

    def close(self):
        if self.connection is not None:
            self.connection.close()

    def _connect_psycopg2(self):
        return psycopg2.connect(**self.connection_settings)

    def _connect_pyodbc(self):
        connection_string = f'DRIVER={self.connection_settings["driver"]};SERVER={connection_settings["host"]};DATABASE={connection_settings["dbname"]};UID={connection_settings["user"]};PWD={connection_settings["password"]};charset=utf8mb4;'
        
        # connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+host+';DATABASE='+dbname+';UID='+user+';PWD='+password
        # return pyodbc.connect(**self.connection_settings)
        return pyodbc.connect(connection_string)
    

    def _connect_sqlalchemy(self):
        url_object = URL.create(
            drivername=self.connection_settings['driver'],
            username = self.connection_settings['user'],
            password = self.connection_settings['password'],
            host = self.connection_settings['host'],
            database = self.connection_settings['dbname'],
            port = self.connection_settings['port']
        )
        return create_engine(url_object).connect()

    def _execute_query_psycopg2(self, query):
        cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def _execute_query_pyodbc(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def _execute_query_sqlalchemy(self, query):
        # returning a list of dictionaries instead of a list of tuples
        return [row._asdict() for row in self.connection.execute(text(query)).fetchall()]