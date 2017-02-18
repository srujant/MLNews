import requests

keywords = ['politics', 'us', 'world', 'technology', 'sports', 'business', 'entertainment', 'science', 'health']

# format of return will be:
# [general, technology, sports, business, entertainment, science]
# within each element of this list, you will have:
# [name of article, url, provider, description]

def bing_search(query):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/news?category='+query+'&mkt=en-us'
    # query string parameters
    payload = {'q': query}
    # custom headers
    headers = {'Ocp-Apim-Subscription-Key': '028fb806bc014b3baf2426e3ac1292dc '}
    # make GET request
    r = requests.get(url, params=payload, headers=headers)
    # get JSON response
    listOfArticles = r.json()['value']
    masterList = []
    for article in listOfArticles:
    	if('clusteredArticles' in article):
    		information = article['clusteredArticles']
    	else:
    		information = article
    	thisList = []
    	if(type(information) is dict):
	    	thisList.append(article.get('name'))
	    	thisList.append(information['url'])
	    	provider = information['provider'][0]
	    	thisList.append(provider['name'])
	    	thisList.append(str(information['description'].encode("ascii", "ignore")))
		masterList.append(thisList)
    return masterList

def generateResponse():
	politicsList = bing_search('politics')
	usList = bing_search('us')
	worldList = bing_search('world')

	generalList = politicsList + usList + worldList
	techList = bing_search('technology')
	sportsList = bing_search('sports')
	buisnessList = bing_search('business')
	entertainmentList = bing_search('entertainment')
	scienceList = bing_search('science')
	scienceList += bing_search('health')


	masterList = []

	masterList.append(generalList)
	masterList.append(techList)
	masterList.append(sportsList)
	masterList.append(buisnessList)
	masterList.append(entertainmentList)
	masterList.append(scienceList)

	return masterList






bing_search('politics')