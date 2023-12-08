from src import constants
from src.db_manager import DBManager
from src.site_discover import HeadHunterDiscover


class WorkSession:
    def __init__(self):
        self.__site_discover = HeadHunterDiscover(constants.COMPANIES_ID_LIST)
        self.__db_manager = DBManager(constants.TABLES_LIST)

    def collect_data(self):
        self.__db_manager.update_tables(self.__site_discover)

    def get_companies_dict(self):
        companies_data = self.__db_manager.get_companies_and_vacancies_count()
        return dict(companies_data)

    def get_company_vacancies_list(self, company):
        return self.__db_manager.get_vacancies_by_company_name(company)

    def get_all_vacancies_list(self):
        return self.__db_manager.get_all_vacancies_data()

    def get_avg_salary(self):
        return int(self.__db_manager.get_avg_salary()[0])

    def get_vacancies_with_higher_salary(self):
        return self.__db_manager.get_vacancies_with_higher_salary()

    def get_vacancies_by_keyword(self, keyword):
        return self.__db_manager.get_vacancies_by_keyword(keyword)