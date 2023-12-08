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
    def get_companies_and_vacancies_count():
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(constants.ALL_COMPANIES_REQUEST)
                    res = cur.fetchall()
        finally:
            conn.close()
        return res

    @staticmethod
    def get_vacancies_by_company_name(company_name):
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"SELECT vacancy_name, salary, vacancy_link FROM vacancies "
                                f"WHERE company_id IN "
                                f"(SELECT company_id FROM companies WHERE company_name = '{company_name}')")
                    res = cur.fetchall()
        finally:
            conn.close()
        return res

    @staticmethod
    def get_all_vacancies_data():
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(constants.ALL_VACANCIES_REQUEST)
                    res = cur.fetchall()
        finally:
            conn.close()
        return res

    @staticmethod
    def get_avg_salary():
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(constants.GET_AVG_SALARY)
                    res = cur.fetchone()
        finally:
            conn.close()
        return res

    @staticmethod
    def get_vacancies_with_higher_salary():
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(constants.ABOVE_AVG_SALARY_REQUEST)
                    res = cur.fetchall()
        finally:
            conn.close()
        return res

    @staticmethod
    def get_vacancies_by_keyword(keyword):
        conn = DBManager.__get_connector()
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"SELECT * FROM vacancies WHERE vacancy_name LIKE '%{keyword}%'")
                    res = cur.fetchall()
        finally:
            conn.close()
        return res

    def __fill_tables(self, site_discover, main_cursor):
        tables_data = site_discover.get_tables_data(self.__tables_list)
        for table_name in self.__tables_list:
            table_data = tables_data[table_name]
            for line_id, line in enumerate(table_data, 1):
                main_cursor.execute(f"""INSERT INTO {table_name} VALUES('{line_id}', '{"', '".join(line)}');""")

    @staticmethod
    def __clear_data(table_name, main_cursor):
        main_cursor.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;")

    @staticmethod
    def __get_connector():
        conn = psycopg2.connect(
            host=constants.HOST,
            database=constants.DATABASE,
            user=constants.USER,
            password=constants.PASSWORD
        )
        return conn
