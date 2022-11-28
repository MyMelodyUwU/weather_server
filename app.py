#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_mqtt import Mqtt

from os.path import join, dirname, realpath

import subscribe 

app = Flask(__name__)

@app.route('/')
def index():
	content = "Temperature right now is: " + subscribe.main()
	return content

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


