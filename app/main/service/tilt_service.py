from datetime import datetime

import requests
import logging
import csv
import codecs
from contextlib import closing
from app.main.model.tilt_log import TiltLog
from app.main import db
from app.main.service import brew_service


def update_all_tilt_data():
    brews = brew_service.get_all_tiltable_brews()
    for brew in brews:
        fetch_tilt_data(brew)


# test: "https://docs.google.com/spreadsheets/d/1XWo5ZkoweSnvKIlnR0X1tuKgKaq7UcQgQrDI0cA_KpQ/export?format=csv&gid=734290882"
def update_brew_tilt_data(brew_id):
    brew = brew_service.get_a_brew(brew_id)
    if brew.tilt_url is not None:
        fetch_tilt_data(brew)
    else:
        logging.warning('No tilt_url found on brew: ' + brew_id)


def fetch_tilt_data(brew):
    print('processing: ' + brew.brew_name + " url: " + brew.tilt_url)
    with closing(requests.get(brew.tilt_url, stream=True)) as r:
        lines = codecs.iterdecode(r.iter_lines(), 'utf-8')
        reader = csv.reader(lines, delimiter=',', quotechar='"')
        for row in reader:
            if '/' in row[2]:
                tilt_log = build_log(row, brew)
                existing = TiltLog.query.filter_by(id=tilt_log.id).first()
                if not existing:
                    logging.info('storing tilt log: ' + tilt_log.__repr__())
                    save(tilt_log)


def build_log(row, brew):
    date_string = row[2]
    d = datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S')
    gravity = int(row[3].replace(".", ""))
    temp = row[4]
    if "." not in temp:
        # celsius = (temp - 32) * 5/9
        temperature = float((temp - 32) * 5/9)
    else:
        temperature = float(temp)

    _id = str(int(d.timestamp())) + '_' + str(brew.id)

    return TiltLog(id=_id, parent_id=brew.id, timestamp=d, gravity=gravity, temperature=temperature)


def get_tilt_logs_by_brew_id(brew_id):
    return TiltLog.query.filter_by(parent_id=brew_id).all()


def save(data):
    db.session.add(data)
    db.session.commit()
