#!/usr/bin/python3
import sys
import time
#print(sys.path)
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Hello world!</h1>

    <iframe src="https://www.youtube.com/embed/YQHsXMglC9A" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)