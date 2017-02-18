import requests
from ml import svm

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
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/news?category='+query+'&mkt=en-us'
    # query string parameters
    payload = {'q': query}
    # custom headers
    headers = {'Ocp-Apim-Subscription-Key': '028fb806bc014b3baf2426e3ac1292dc'}

    links = []
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
    
    return links



