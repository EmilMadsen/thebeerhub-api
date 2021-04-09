import requests
from contextlib import closing
import csv
import codecs


def update_tilt_data():
    return None
    # TODO:
    # fetch all brews & loop
    # find active tilt urls
    # if active - fetch
    # try update all rows on brew


def fetch_tilt_data(url):
    print('processing: ' + url)

    with closing(requests.get(url, stream=True)) as r:
        lines = codecs.iterdecode(r.iter_lines(), 'utf-8')
        reader = csv.reader(lines, delimiter=',', quotechar='"')
        for row in reader:
            print(row)
