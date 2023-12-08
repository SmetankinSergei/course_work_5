COMPANIES_ID_LIST = ['87021', '1740', '5325', '6093775', '1083758', '60377', '114735', '4233', '4634258', '24947']
HH_COMPANY_URL = 'https://api.hh.ru/employers/'
HH_COMPANY_VACANCIES_URL = 'https://api.hh.ru/vacancies?employer_id='
TABLES_LIST = ['companies', 'vacancies']

HOST = 'localhost'
DATABASE = 'homework_17_4'
USER = 'postgres'
PASSWORD = '1111'

ALL_COMPANIES_REQUEST = 'SELECT company_name, COUNT(vacancy_name) ' \
                        'FROM companies JOIN vacancies USING (company_id) GROUP BY company_name'
ALL_VACANCIES_REQUEST = 'SELECT vacancy_name, salary, vacancy_link FROM vacancies'
GET_AVG_SALARY = 'SELECT AVG(salary) FROM vacancies'
ABOVE_AVG_SALARY_REQUEST = 'SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies)'
