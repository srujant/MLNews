import os
import json
import algorithm
from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import g
from flask import jsonify
from flask import redirect

app = Flask(__name__)

finalArrayData = []


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/splash')
def splash():
    return render_template('splash.html')
    
@app.route('/results')
def results():
    return render_template('results.html')
    
@app.route('/test')
def test():
    return render_template('test.html')
    
@app.route('/compute-result',methods=['POST'])
def compute():
    jsdata = request.form
    print jsdata
    finalArrayData = algorithm.mainAlgorithm(str(jsdata))
    return render_template("results.html")

@app.route('/return-result', methods=['GET'])
def return_result():
    return json.dumps(finalArrayData)



app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug = True