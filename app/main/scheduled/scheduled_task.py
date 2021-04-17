import requests


def run():
    print("running scheduled task")
    r = requests.post('http://127.0.0.1:5000/tilt_logs/start/jobs')
