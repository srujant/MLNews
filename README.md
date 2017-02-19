![logo-image](https://raw.githubusercontent.com/srujant/MLNews/master/static/img/logo3.png)

An app that lets you discover the top news in locations around the world and discover the credibility of any article using machine learning.

## What is it?
- BiPartisan is an app that lets you view news in a meaningful way by discovering the most truthful news from the right places.
- BiPartisan allows you to see the top news in every region of the world using the [NewStream](https://hophacks-bipartisan-rachitag22.c9users.io/stream)
- You can even analyze specific articles using our [BiScore](https://hophacks-bipartisan-rachitag22.c9users.io/bias)

## APIs Used
- [Bing News Search](https://www.microsoft.com/cognitive-services/en-us/bing-news-search-api) and [News API] (https://newsapi.org)
	- Retrieval of news articles for NewStream
- [Bing Web Search](https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api) and [Bing AutoSuggest] (https://www.microsoft.com/cognitive-services/en-us/bing-autosuggest-api)
	- Web search of articles for BiScore
- [Google Maps Geolocation API](https://developers.google.com/maps/documentation/geolocation/intro)
  - Mapping regions to ares on NewStream
- [Twitter Search API] (https://dev.twitter.com/rest/public/search)
	- Counting tweets to determine topic popularity for NewStream

## Libraries Used
- [Cesium](https://cesiumjs.org)
  - Visualization of news on globe for NewStream
- [spaCy](https://spacy.io)
  - Natural language processing to determine bias of news article for NewStream
- [Requests] (http://docs.python-requests.org/en/master/)
	- HTTP requests
- [Twython] (https://github.com/ryanmcgrath/twython)
	- Python wrapper for Twitter data
- [NLTK](http://www.nltk.org/)
  - Natural Language processing for determining the topic of articles in NewStream
- [Goose](https://github.com/GravityLabs/goose/wiki)
	- NLP
- [pandas](http://pandas.pydata.org/)
	- Data
- [Tweepy](https://github.com/tweepy/tweepy)
	- Twitter for Python
