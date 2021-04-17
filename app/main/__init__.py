from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_apscheduler import APScheduler
from .scheduled import scheduled_task

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
scheduler = APScheduler()


def create_app(config_name):
    print("app config_name: ", config_name)
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    with app.app_context():
        db.create_all()
    flask_bcrypt.init_app(app)
    scheduler.add_job(id='Scheduled Task', func=scheduled_job, trigger="interval", seconds=10)
    scheduler.start()

    return app



def scheduled_job():
    print("running job")
    print(datetime.now())
#  scheduled_task.run()
