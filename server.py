from __future__ import print_function
from sys import stderr
# steps:
# install flask
# pip install flask
# Run server:
# FLASK_DEBUG=1 FLASK_APP=server.py flask run
import flask
from flask import Flask, request
from optimization2 import *


app = Flask(__name__)

@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route("/lat_lng")
def lat_lng():
  a = float(request.args.get('a'))
  b = float(request.args.get('b'))
  c = float(request.args.get('c'))
  d = float(request.args.get('d'))
  direct = float(request.args.get('direct'))

  return flask.jsonify(getMyGeoJSON(lat = lat, lng = lng, path = 'document.csv', metric = metric, a = a, b = b, c = c, d = d, direct = direct))

def getMyGeoJSON(lat,lng, path, metric, a, b, c, d, direct):
  points = getServiceArea((lat,lng), path, metric,  a, b, c, d, direct)
  return points

if __name__ == '__main__':
    app.run()
