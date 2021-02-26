import subprocess
from datetime import datetime
from flask import Flask, send_file, request
import psutil

app = Flask(__name__)


@app.route('/')
def hello_world():
    return send_file('index.html')

@app.route('/memory_info')
def memory_info():
    pid, line = pid_by_name(request.args.get('process'))
    if pid == -1:
        return {}

    maps = psutil.Process(pid).memory_maps()

    result = {}
    for f in maps[0]._fields:
        if f != 'path':
            result[f] = sum(int(getattr(m, f)) for m in maps) // (1024**2)

    return dict(
        t=(datetime.now().second),
        line=line,
        data=result,
    )

@app.route('/add_gb')
def add_gb():
    if not hasattr(app, 'gb'):
        app.gb = []

    app.gb.append('.' * (1024 ** 3))

    return {}

def pid_by_name(name):
    if not name:
        return None, None

    process = subprocess.Popen([
        'bash',
        '-c',
        f"ps ax | grep '{name}' | grep -v grep | head -n 1"
    ], stdout=subprocess.PIPE)
    output, error = process.communicate() 

    line = output.decode('latin1')
    pid = int(line.split()[0]) if line else -1

    return pid, line
