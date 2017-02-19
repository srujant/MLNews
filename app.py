import os
import json
from ml import svm
from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import g
from flask import jsonify
from flask import redirect
import download_corpora
import NLProcessor
import otherAPIs
import scraper
import searchFunction
import stream

svm.read()
svm.train()

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return render_template('stream.html')

@app.route('/bias', methods = ['POST', 'GET'])
def bias():
    #article_info = {"keywords": ["George Takei", "the United States", "CNN", "Franklin D. Roosevelt", "US", "Donald Trump", "Trump", "Remembrance Day", "America"], "url": "http://www.cnn.com/2017/02/18/opinions/george-takei-japanese-american-internment-day-of-remembrance/index.html", "score": 0.31700051999477097, "title": "George Takei: On this Remembrance Day, I hear terrible echoes of the past  - CNN.com"}
    if request.method == 'POST':
        article_url = request.form["article_url"]
        article_info = processURL(article_url)
        return render_template('bias.html', article_info = article_info)
    return render_template('bias.html', article_info = article_info)


@app.route('/search', methods = ['POST', 'GET'])
def search():
    #articles_info = [{"url": "http://www.cnn.com/2017/02/18/politics/donald-trump-florida-campaign-rally/index.html", "title": "Trump gets what he wants in Florida: Campaign-level adulation - CNNPolitics.com", "score": "72", "id": "1", "description": "Melbourne, Florida (CNN)President Donald Trump, after a month of arduous and, at times, turbulent governing, got what he came for Saturday during a dusk rally here: Campaign-level adulation. Trump, who just months ago finished campaigning for the office he ..."}, {"url": "http://www.firstpost.com/entertainment/saturday-night-live-female-icons-and-impersonation-in-the-time-of-donald-trump-3289726.html", "title": "Saturday Night Live, female icons, and impersonation in the time of Donald Trump", "score": "60", "id": "2", "description": "And its truly a stranger than fiction reality we live in right now  where orange-tinted reality stars are presidents of countries and climate change scientists are being referred to as a glassy-eyed cult. Alec Baldwins completely on-point ..."}, {"url": "http://www.cnn.com/2017/02/18/politics/trump-gene-huber-rally/index.html", "title": "Trump hands mic to supporter at Florida rally - CNNPolitics.com", "score": "76", "id": "3", "description": "(CNN)In what appeared to be an improvised moment, President Donald Trump invited one of his supporters to join him on stage and take the microphone during a rally in Melbourne, Florida, on Saturday night. As the man climbed up, the President addressed ..."}, {"url": "http://www.politico.com/story/2017/02/trump-florida-rally-campaign-mode-235183", "title": "Four weeks into his presidency, Trump returns to campaign mode - POLITICO", "score": "63", "id": "4", "description": "Melbourne, Fla.  President Donald Trump's rally here featured all the classic signatures of his campaign: boasts about his poll numbers and magazine appearances, grandiose promises of quick action, protesters lining the streets, stinging attacks on the ..."}, {"url": "http://irregulartimes.com/2017/02/18/donald-trump-is-the-upside-down-of-stranger-things/", "title": "Donald Trump is the Upside Down of Stranger Things \u2013 Irregular Times", "score": "35", "id": "5", "description": "This week, when David Cicilline rose to express resistance to the cruel fascism being imposed by the White House under Donald Trump, he invoked the sinister threat depicted in the TV show Stranger Things. Cicilline explained, Like the main characters in ..."}]
    
    if request.method == 'POST':
        if (request.form != None and request.form["search_query"] != None):
            query = request.form["search_query"]
            articles_info = manualSearch(query)
        
        return render_template('search.html', articles_info = articles_info)
        
    return render_template('search.html', articles_info = articles_info)


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8081)))

if __name__ == '__main__':
    app.run()
    app.debug = True
