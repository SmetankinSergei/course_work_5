from flask import render_template, request

from main import app, work_session


@app.route('/')
def start_page():
    return render_template('start_page.html')


@app.route('/main_page/<string:load_status>', methods=['GET', 'POST'])
def main_page(load_status):
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        vacancies_list = work_session.get_vacancies_by_keyword(keyword)
        return render_template('company_vacancies_page.html', vacancies=vacancies_list)
    if load_status == 'update':
        work_session.collect_data()
    elif load_status == 'avg_salary':
        avg_salary = work_session.get_avg_salary()
        return render_template('main_page.html', avg_salary=avg_salary)
    return render_template('main_page.html')


@app.route('/all_companies_page')
def all_companies_page():
    companies_dict = work_session.get_companies_dict()
    return render_template('all_companies_page.html', companies_data=companies_dict)


@app.route('/company_vacancies_page/<string:company>')
def company_vacancies_page(company):
    vacancies_list = work_session.get_company_vacancies_list(company)
    return render_template('company_vacancies_page.html', company=company, vacancies=vacancies_list)


@app.route('/all_vacancies_page/<string:load_status>')
def all_vacancies_page(load_status):
    if load_status == 'avg_salary':
        vacancies_list = work_session.get_vacancies_with_higher_salary()
    else:
        vacancies_list = work_session.get_all_vacancies_list()
    return render_template('company_vacancies_page.html', vacancies=vacancies_list)
