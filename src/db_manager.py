import psycopg2

from src import constants


class DBManager:
    def __init__(self, tables_names_list):
        self.__tables_list = tables_names_list

    def update_tables(self, site_discover):
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    for table in self.__tables_list:
                        DBManager.__clear_data(table, cur)
                    self.__fill_tables(site_discover, cur)
        finally:
            conn.close()

    @staticmethod
    def __clear_data(table_name, main_cursor):
        main_cursor.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;")

    def __fill_tables(self, site_discover, main_cursor):
        tables_data = site_discover.get_tables_data(self.__tables_list)
        for table_name in self.__tables_list:
            table_data = tables_data[table_name]
            for line_id, line in enumerate(table_data, 1):
                main_cursor.execute(f"""INSERT INTO {table_name} VALUES('{line_id}', '{"', '".join(line)}');""")

    @staticmethod
    def __get_connector():
        conn = psycopg2.connect(
            host=constants.HOST,
            database=constants.DATABASE,
            user=constants.USER,
            password=constants.PASSWORD
        )
        return conn
