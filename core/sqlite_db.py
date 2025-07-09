import sqlite3
import pandas as pd


class SQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table_from_dataframe(self, table_name: str, df: pd.DataFrame):
        df.to_sql(name=table_name, con=self.conn, if_exists='replace', index=False)

    def create_table_from_dataframes(self, dicts: dict):
        for key, value in dicts.items():
            value.to_sql(name=key, con=self.conn, if_exists='replace', index=False)

    def query_table_to_dataframe(self, table_name):
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql_query(query, self.conn)

    def close(self):
        self.conn.close()
