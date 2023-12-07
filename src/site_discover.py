import json
from statistics import mean
from abc import ABC, abstractmethod

import requests

from src import constants


class SiteDiscover(ABC):

    @abstractmethod
    def get_tables_data(self, tables_names):
        pass


class HeadHunterDiscover(SiteDiscover):
    def __init__(self, companies_id_list):
        self.__companies_id_list = companies_id_list
        self.__data_set = {'companies': self.__get_companies_list,
                           'vacancies': self.__get_vacancies_list}

    def get_tables_data(self, tables_names):
        tables = [table for table in tables_names if table in self.__data_set]
        return {table: self.__data_set[table]() for table in tables}

    def __get_vacancies_list(self):
        vacancies_list = []
        for company_id in self.__companies_id_list:
            vacancies_info = requests.get(constants.HH_COMPANY_VACANCIES_URL + company_id)
            vacancies_info = json.loads(vacancies_info.text)['items']
            for vacancy in vacancies_info:
                vacancy = [vacancy['name'], self.__set_salary(vacancy['salary']), vacancy['url'], company_id]
                vacancies_list.append(vacancy)
        return vacancies_list

    def __get_companies_list(self):
        companies_list = []
        for company_id in self.__companies_id_list:
            company_name = requests.get(constants.HH_COMPANY_URL + company_id)
            company_name = json.loads(company_name.text)['name']
            companies_list.append([company_id, company_name])
        return companies_list

    @staticmethod
    def __set_salary(salary_info):
        if salary_info:
            low_border = salary_info['from'] if salary_info['from'] is not None else salary_info['to']
            high_border = salary_info['to'] if salary_info['to'] is not None else salary_info['from']
            return str(mean([low_border, high_border]))
        return 'No data'
