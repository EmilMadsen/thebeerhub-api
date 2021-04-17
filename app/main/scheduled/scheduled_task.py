import requests

running = False


def run():
    global running
    if not running:
        running = True
        print("running scheduled task")
        r = requests.post('http://127.0.0.1:5000/tilt_logs/start/jobs')
        running = False
    else:
        print("job already running - skipping")
