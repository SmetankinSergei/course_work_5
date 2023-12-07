from flask import render_template

from main import app


@app.route('/')
def start_page():
    return render_template('start_page.html')
