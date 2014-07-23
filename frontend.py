#!/usr/bin/env python3
# ex: ts=4 sw=4 et

import json
from flask import Flask
from monitor import getData


app = Flask('SCP Monitor Frontend')

@app.route('/ping')
def ping():
    return('{"reply": "pong"}')

@app.route('/info')
def info():
    return(json.dumps(getData()))

app.run(host='0.0.0.0')
