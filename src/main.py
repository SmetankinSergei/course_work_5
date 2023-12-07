from flask import Flask

from src.work_session import WorkSession

app = Flask(__name__)
work_session = WorkSession()

import routes
