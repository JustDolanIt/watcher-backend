#!/usr/bin/env python3
# ex: ts=4 sw=4 et

import flask
from monitor import getData


app = flask.Flask(__name__)

@app.route('/ping')
def ping():
    return(flask.jsonify(**{"reply": "pong"}))

@app.route('/info')
def info():
    return(flask.jsonify(**getData()))

if __name__=='__main__':

    app.run(host='127.0.0.1', port=36484, debug=True)
