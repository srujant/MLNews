import urllib2
import pprint
import json
import requests
import time
import ast
import NLProcessor as nlp

def getArticles():
	articles = urllib2.urlopen("https://newsapi.org/v1/sources").read()
	articles = ast.literal_eval(articles)
	articles = articles.items()[1]
	articles = articles[1]
	text_file = open("Output.txt", "w")
	for x in range(0, len(articles)):
		articleid = articles[x]['id']
		payload = {'source': articleid, 'apiKey': '6f62a98cbb734492abbdba50a4bdff86', 'sortBy': 'top'}
		r = requests.get('https://newsapi.org/v1/articles', params=payload)
		if str(r.json()['status']) == 'ok':
			presentArticles = json.dumps(r.json()['articles'])
			jsonReceived = json.loads(presentArticles)[0]
			url = jsonReceived[u'url']
			text = nlp.HTMLParser(url)
			print text
			text_file.write('\n\n\n\n')
			

	text_file.close()

def main():
	getArticles()


if __name__ == "__main__":
  main()