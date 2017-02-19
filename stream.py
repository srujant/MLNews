import urllib2
import json
import requests
import ast
import sys
import NLProcessor as nlp
import otherAPIs as api
sys.path.append('./ml/data/')
sys.path.append('./ml/')
from ml import svm
from iso3166 import countries
import re
import geojson
from collections import OrderedDict
import boto3

dynamodb = boto3.resource('dynamodb')
aggregatedDict = {}
table = dynamodb.Table('hophacks')

stateCodes = {
	    'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def insertDict(date, dict):
    table.put_item(
        Item={
        'dictionary': date,
        'dict': dict
         }
    )
def insertJson(date, json):
    table.put_item(
        Item={
        'dictionary': date,
        'json': json
         }
    )
def getItem(date):
        reponse=table.get_item(
                Key={'dictionary': date}
        )
        return reponse['Item']


def getNewsAPI():
	articles = urllib2.urlopen("https://newsapi.org/v1/sources").read()
	articles = ast.literal_eval(articles)
	articles = articles.items()[1]
	articles = articles[1]
	counter = 0
	for x in range(0, len(articles)):
		articleid = articles[x]['id']
		topic = articles[x]['category']
		if topic == 'entertainment' or (topic == 'gaming') or topic == 'music':
			topic = 'entertainment'
		if topic == 'science-and-nature':
			topic = 'science'
		payload = {'source': articleid, 'apiKey': '6f62a98cbb734492abbdba50a4bdff86', 'sortBy': 'top'}
		r = requests.get('https://newsapi.org/v1/articles', params=payload)
		if str(r.json()['status']) == 'ok':
			presentArticles = json.loads(json.dumps(r.json()['articles']))
			for y in range(0, len(presentArticles)):
				jsonReceived = presentArticles[y]
				title = jsonReceived[u'title']
				author = jsonReceived[u'author']
				url = jsonReceived[u'url']
				credRating = -1
				try:
					locations = nlp.HTMLParser(url)
					for z in range(0, len(locations)):
						location = str(getAddress(str(locations[z])))
						if location not in aggregatedDict:
							aggregatedDict[location] = []
						listInfo = aggregatedDict[location]
						tempDict = {}
						tempDict['url'] = url
						tempDict['author'] = author
						tempDict['title'] = title
						tempDict['credRating'] = svm.compute(url)
						tempDict['topic'] = topic
						listInfo.append(tempDict)
						aggregatedDict[location] = listInfo
				except:
					None
def addToDict():
	masterList = api.generateResponse()
	for x in range(0, len(masterList)):
		for y in range(0, len(masterList[x])):
			for z in range(0, 4):
				try:
					locations = nlp.HTMLParser(masterList[x][y][1])
					for z in range(0, len(locations)):
						location = str(getAddress(str(locations[z])))
						if location not in aggregatedDict:
							aggregatedDict[location] = []
						listInfo = aggregatedDict[location]
						tempDict = {}
						tempDict['url'] = masterList[x][y][1]
						tempDict['author'] = masterList[x][y][2]
						tempDict['title'] = masterList[x][y][0]
						tempDict['credRating'] = svm.compute(masterList[x][y][1])
						if x is 0:
							tempDict['topic'] = 'general'
						if x is 1:
							tempDict['topic'] = 'technology'
						if x is 2:
							tempDict['topic'] = 'sports'
						if x is 3:
							tempDict['topic'] = 'business'
						if x is 4:
							tempDict['topic'] = 'entertainment'
						if x is 5:
							tempDict['topic'] = 'science'
						listInfo.append(tempDict)
						aggregatedDict[location] = listInfo
				except:
					None


def getAddress(toSearch):
	addresses = []
	toSearch = str(toSearch)
	payload = {'address': toSearch, 'components':'administrative_area_level_1', 'key': 'AIzaSyBW5C6SvSUUebg5Atsj3beYMtDgwbIR6PI'}
	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?', params=payload)
	json = r.json()[u'results'][0]
	if len(json[u'address_components']) >= 2:
		if str(json[u'address_components'][len(json[u'address_components']) - 1][u'short_name']) == 'US':
			prepend = "USA-"
			string = str(json[u'address_components'][len(json[u'address_components']) - 2][u'short_name'])
			addresses.append(prepend+string)
		else:
			addresses.append(str(json[u'address_components'][len(json[u'address_components']) - 1][u'short_name']))
	else:
		addresses.append(str(json[u'address_components'][len(json[u'address_components']) - 1][u'short_name']))
	return addresses[0]

def main():
	
	getNewsAPI()
	addToDict()
	fileDict = {}
	with open('completedJson.txt','r') as inf:
		fileDict = eval(inf.read())
		for key in fileDict.keys():
			try:
				key = countries.get(key).alpha3
			except:
				key = key
	# with open("template.json", 'r') as f:
	# 	read_data = f.read()
	data = json.load(open('template.json'), object_pairs_hook=OrderedDict)
	data = data[u'features']
	for x in range(0, len(data)):
		line = data[x]
		topics = {}
		country = line[u'id']
		country = str(country)
		name = line[u'properties'][u'name']
		name = str(name)
		try:
			if country in fileDict:
				for y in range(0, len(fileDict[country])):
					topic = fileDict[country][y]['topic']
					href = "<a target='_blank' href='" + fileDict[country][y]['url'] + "'>" + str(fileDict[country][y]['title']) + '</a>'
					if topic not in topics:
						topics[topic] = []
					eachTopic = topics[topic]
					credibility = {}
					author = {}
					article = {}
					credibility['Credibility'] = str(fileDict[country][y]['credRating'])
					author['Author'] = str(fileDict[country][y]['author'])
					article[str(href)] = []
					article[str(href)].append(credibility)
					article[str(href)].append(author)
					eachTopic.append(article)
					topics[topic] = eachTopic
			elif countries.get(country).alpha2 in fileDict:
				for y in range(0, len(fileDict[countries.get(country).alpha2])):
					topic = fileDict[countries.get(country).alpha2][y]['topic']
					href = "<a target='_blank' href='" + fileDict[countries.get(country).alpha2][y]['url'] + "'>" + str(fileDict[countries.get(country).alpha2][0]['title']) + '</a>'
					if topic not in topics:
						topics[topic] = []
					eachTopic = topics[topic]
					credibility = {}
					author = {}
					article = {}
					credibility['Credibility'] = str(fileDict[countries.get(country).alpha2][y]['credRating'])
					author['Author'] = str(fileDict[countries.get(country).alpha2][y]['author'])
					article[str(href)] = []
					article[href].append(credibility)
					article[href].append(author)
					eachTopic.append(article)
					topics[topic] = eachTopic
			a = ""
			for topic in topics.keys():
				for article in topics[topic]:
					for element in article:
						for y in range(0, len(article[element])):
							for key in article[element][y]:
								a += article[element][y] + '\n'
								line[u'properties'][topic] = {element:{'info':a}}					
		except:
			None
	test = './test.geojson'
	with open('data.txt', 'w') as outfile:
		json.dump(data, outfile)
	insertJson('2/19', str(data))
	with open('final.txt', 'w') as outfile:
		json.dump(aggregatedDict, outfile)
if __name__ == "__main__":
  main()
