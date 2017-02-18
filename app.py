import os
import json
from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import g
from flask import jsonify
from flask import redirect

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return render_template('stream.html')

@app.route('/bias')
def bias():
    return render_template('bias.html')

@app.route('/search')
def search():
    return render_template('bias.html')
    

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug = True