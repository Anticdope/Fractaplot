import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Creates a new table in the database
        columns is a dict with keys as column names and values as column types
        """
        columns_with_types = ', '.join([f'{name} {type}' for name, type in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns_with_types});")
        self.conn.commit()

    def get_component_types(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [table[0] for table in self.cursor.fetchall()]

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        return [table[0] for table in tables]

    def get_columns(self, table_name):
        self.cursor.execute(f'PRAGMA table_info("{table_name}")')
        return [column[1] for column in self.cursor.fetchall()]

    def create(self, table_name, **kwargs):
        """
        Inserts a new row into the table
        """
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join('?' for _ in kwargs)
        values = tuple(kwargs.values())
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
        self.conn.commit()

    def read(self, table_name, **kwargs):
        """
        Fetches rows from the table
        """
        condition = ' AND '.join([f"{k} = '{v}'" for k, v in kwargs.items()])
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()

    def update(self, table_name, condition_dict, **kwargs):
        """
        Updates rows in the table
        """
        updates = ', '.join([f"{k} = '{v}'" for k, v in kwargs.items()])
        condition = ' AND '.join([f"{k} = '{v}'" for k, v in condition_dict.items()])
        self.cursor.execute(f"UPDATE {table_name} SET {updates} WHERE {condition}")
        self.conn.commit()

    def delete(self, table_name, **kwargs):
        """
        Deletes rows from the table
        """
        condition = ' AND '.join([f"{k} = '{v}'" for k, v in kwargs.items()])
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def close(self):
        self.conn.close()
