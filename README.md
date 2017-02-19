![logo-image](https://raw.githubusercontent.com/srujant/MLNews/master/static/img/logo3.png)

An app that lets you discover the top news in locations around the world and discover the credibility of any article using machine learning.

## What is it?
- Bipartisan is an app that lets you view news in a meaningful way by discovering the most truthful news from the right places.
- Bipartisan allows you to see the top news in every region of the world using the [B-Stream](https://hophacks-bipartisan-rachitag22.c9users.io/stream)
- You can even analyze specific articles using our [B-Score](https://hophacks-bipartisan-rachitag22.c9users.io/bias)

## APIs Used
- [Bing News Search](https://www.microsoft.com/cognitive-services/en-us/bing-news-search-api) and [News API] (https://newsapi.org)
	- Retrieval of news articles for B-Stream
- [Bing Web Search](https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api) and [Bing AutoSuggest] (https://www.microsoft.com/cognitive-services/en-us/bing-autosuggest-api)
	- Web search of articles for B-Score
- [Google Maps Geolocation API](https://developers.google.com/maps/documentation/geolocation/intro)
  - Mapping regions to ares on B-Stream
- [Twitter Search API] (https://dev.twitter.com/rest/public/search)
	- Counting tweets to determine topic popularity for B-Stream

## Libraries Used
- [Cesium](https://cesiumjs.org)
  - Visualization of news on globe for B-Stream
- [spaCy](https://spacy.io)
  - Natural language processing to determine bias of news article for B-Stream
- [Requests] (http://docs.python-requests.org/en/master/)
	- HTTP requests
- [Twython] (https://github.com/ryanmcgrath/twython)
	- Python wrapper for Twitter data
- [NLTK](http://www.nltk.org/)
  - Natural Language processing for determining the topic of articles in B-Stream
- [Goose](https://github.com/GravityLabs/goose/wiki)
	- Natural Language processing for determining the topic of articles in B-Stream
-[Scikit-learn] (https://github.com/scikit-learn/scikit-learn)
	- Natural Language processing for determining the topic of articles in B-Stream
- [pandas](http://pandas.pydata.org/)
	- Data
- [Tweepy](https://github.com/tweepy/tweepy)
	- For accessing Twitter API with Python
