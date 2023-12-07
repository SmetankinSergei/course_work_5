from threading import Thread

from flask import render_template

from main import app, work_session


@app.route('/')
def start_page():
    return render_template('start_page.html')


@app.route('/main_page')
def main_page():
    work_session.collect_data()
    return render_template('main_page.html')
