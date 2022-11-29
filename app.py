#!/usr/bin/env python3

from flask import Flask

import subscribe  #References the subscribe script. 

app = Flask(__name__)

@app.route('/')
def index():
	content = subscribe.main() 
	# this function calls the subscibe script. 
	return content

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


