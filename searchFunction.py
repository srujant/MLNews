import requests
from ml import svm
import json
import NLProcessor as nlp
import lxml.html
from requests import get
from goose import Goose

def getSuggestions(query):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/suggestions/?q=' + query
    headers = {'Ocp-Apim-Subscription-Key':'854e8088bb8347418e6f934b996487af'}

    r = requests.get(url, headers = headers)

    results = []

    suggestions = r.json()['suggestionGroups']
    max = 3
    for suggestion in suggestions:
        s = suggestion['searchSuggestions']
        for term in s:
            if max == 0:
                break
            max-=1
            results.append(str(term['query'].encode("ascii", "ignore")))
    return results


def manualSearch(query):
    similarSearches = getSuggestions(query)
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/news/search'
    # query string parameters
    payload = {'q': query, 'freshness':'Week'}
    # custom headers
    headers = {'Ocp-Apim-Subscription-Key': '028fb806bc014b3baf2426e3ac1292dc'}
    r = requests.get(url, params=payload, headers=headers)
    links = []
    descriptions = []
    listOfArticles = r.json()['value']
    max = 5
    for article in listOfArticles:
        if('clusteredArticles' in article):
            information = article['clusteredArticles']
        else:
            information = article
        thisList = []
        if max == 0:
            break
        max-=1
        if(type(information) is dict):
            links.append(information['url'])
            descriptions.append(str(information['description'].encode("ascii", "ignore")))
    fin = []
    fin.append(similarSearches)
    rating = 0.0
    i = 0
    for link in links:
        thisDict = {}
        rating = svm.compute(link)
        thisDict['description'] = descriptions[i]
        thisDict['url'] = link
        thisDict['score'] = str(rating)
        i+=1
        fin.append(thisDict)

    return json.dumps(fin)

def processURL(url):
    toReturn = {}

    score = svm.compute(url)

    t = lxml.html.parse(url)

    title = t.find(".//title").text

    response = get(url)
    extractor = Goose()
    article = extractor.extract(raw_html=response.content)
    file = article.cleaned_text

    keywords = nlp.generateEntity(file)

    toReturn['title'] = title
    toReturn['score'] = score
    toReturn['keywords'] = keywords
    toReturn['url'] = url

    return json.dumps(toReturn)
