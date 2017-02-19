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

@app.route('/bias', methods = ['POST', 'GET'])
def bias():
    article_info = {"keywords": ["George Takei", "the United States", "CNN", "Franklin D. Roosevelt", "US", "Donald Trump", "Trump", "Remembrance Day", "America"], "url": "http://www.cnn.com/2017/02/18/opinions/george-takei-japanese-american-internment-day-of-remembrance/index.html", "score": 0.31700051999477097, "title": "George Takei: On this Remembrance Day, I hear terrible echoes of the past  - CNN.com"}
    if request.method == 'POST':
        article_url = request.form["article_url"]
        article_info = {"keywords": ["George Takei", "the United States", "CNN", "Franklin D. Roosevelt", "US", "Donald Trump", "Trump", "Remembrance Day", "America"], "url": "http://www.cnn.com/2017/02/18/opinions/george-takei-japanese-american-internment-day-of-remembrance/index.html", "score": 0.31700051999477097, "title": "George Takei: On this Remembrance Day, I hear terrible echoes of the past  - CNN.com"}
        #article_info = processURL(article_url)
        return render_template('bias.html', article_info = article_info)
    return render_template('bias.html', article_info = article_info)


@app.route('/search', methods = ['POST', 'GET'])
def search():
    articles_info = [{"url": "https://www.bing.com/cr?IG=091F46A9EE294B76B5D3C69881B36C3A&CID=20E70A5E79DC670F1C47007078ED668E&rd=1&h=EGqHJ5yrPEl8aXDg7845VZcGkAW3p7eGM_7DtlGOG6E&v=1&r=https%3a%2f%2fwww.nytimes.com%2f2017%2f02%2f18%2fworld%2fmiddleeast%2ftrump-dubai-vancouver.html&p=DevEx,5026.1", "score": "19", "id": "1", "description": "Hussain, thank you so much for your love, your friendship. Donald Trump Jr. praised Sheikh Mohammed bin Rashid al-Maktoum, the ruler of Dubai, saying it was his vision for the country that allowed such projects to succeed. Its a great example ..."}, {"url": "http://www.bing.com/cr?IG=091F46A9EE294B76B5D3C69881B36C3A&CID=20E70A5E79DC670F1C47007078ED668E&rd=1&h=mmg_SdJjtcrZ7YPfzkpSdmgiaA0zkv5IEaucOk98PTE&v=1&r=http%3a%2f%2fwww.politico.com%2fstory%2f2017%2f02%2ftrump-florida-rally-campaign-mode-235183&p=DevEx,5028.1", "score": "25", "id": "2", "description": "Melbourne, Fla.  President Donald Trump's rally here featured all the classic signatures of his campaign: boasts about his poll numbers and magazine appearances, grandiose promises of quick action, protesters lining the streets, stinging attacks on the ..."}, {"url": "http://www.bing.com/cr?IG=091F46A9EE294B76B5D3C69881B36C3A&CID=20E70A5E79DC670F1C47007078ED668E&rd=1&h=Bq-KvKuaUTgDMN2xEUDC_ZQoglRnNMukVxfd3Y1Zb8g&v=1&r=http%3a%2f%2fwww.wdsu.com%2farticle%2ftrump-delivers-speech-at-florida-rally%2f8952400&p=DevEx,5030.1", "score": "77", "id": "3", "description": "Just four weeks into his administration, President Donald Trump appeared at a campaign rally that mirrored the months leading up to Election Day, complete with promises to repeal the health care law, insults for the news media and a playlist highlighted by ..."}, {"url": "http://www.bing.com/cr?IG=091F46A9EE294B76B5D3C69881B36C3A&CID=20E70A5E79DC670F1C47007078ED668E&rd=1&h=-Ly5C5cYcXFIZovhiEpIsn96hZ_4StmKotA1i03kQR8&v=1&r=http%3a%2f%2fwww.huffingtonpost.com%2fentry%2fgene-huber-trump-cardboard-cutout_us_58a91337e4b045cd34c2689d&p=DevEx,5032.1", "score": "90", "id": "4", "description": "Gene Huber is so devoted to President Donald Trump, he salutes and talks to a cardboard cutout of Trump every day. Huber, 47, revealed that bizarre ritual during an interview with CNN, held after he was invited to join the president on stage during a ..."}, {"url": "http://www.bing.com/cr?IG=091F46A9EE294B76B5D3C69881B36C3A&CID=20E70A5E79DC670F1C47007078ED668E&rd=1&h=o4hWdx5B5k5RTzMmdRB5AsZ1RvSlIMiJBCA_nr_6Wm8&v=1&r=http%3a%2f%2fwww.palmbeachpost.com%2fnews%2fnational-govt--politics%2ftrump-returns-campaign-mode-brings-boynton-man-stage%2fGJhEvJ60TO2gZy6rXmRgDI%2f&p=DevEx,5034.1", "score": "15", "id": "5", "description": "For those who somehow missed candidate Donald Trumps raucous 2016 campaign rallies, Trump  now the 45th president of the United States  reprised most of his greatest hits Saturday in a campaign-style appearance before 9,000 cheering supporters at ..."}]
    if request.method == 'POST':
        query = request.form["search_query"]
        #articles_info=""
        #articles_info = manualSearch(query)
        return render_template('search.html', articles_info = articles_info)
    return render_template('search.html', articles_info = articles_info)


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug = True