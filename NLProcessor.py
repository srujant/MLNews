from nltk.sentiment.vader import SentimentIntensityAnalyzer
from spacy import load     
from goose import Goose
from requests import get    
import requests
import re
import sys
import newspaper

reload(sys)  
sys.setdefaultencoding('utf8')
nlp = load('en')    

def generateEntity(text):
    seen = set()
    result = []
    index = 0
    processed_text = nlp(unicode(text))
    for ent in processed_text.ents:
        label = ent.label_
        if label == u'PERSON' or label == u'NORP' or label == u'ORG' or label == u'GPE':
            if label == u'PERSON':
                result.append(ent.text)
                seen.add(ent.text)
            elif not ent.text in seen:
                if index % 3 == 0:
                    result.append(ent.text)
                    seen.add(ent.text)
        index+=1
    return result

def countEntity(text):
    entityCount = []
    PERSON = 0
    NORP = 1
    FACILITY = 2
    ORG = 3
    GPE = 4
    LOC = 5
    PRODUCT = 6
    EVENT = 7
    WORK_OF_ART = 8
    LANGUAGE = 9
    DATE = 10
    TIME = 11
    PERCENT = 12
    MONEY = 13
    QUANTITY = 14
    ORDINAL = 15
    CARDINAL = 16
    OTHER = 17

    i = 0
    while( i < 18):
        entityCount.append(0)
        i+=1
    processed_text = nlp(unicode(text))
    for ent in processed_text.ents:
        if ent.label_ == u'PERSON':
            entityCount[PERSON]+=1
        elif ent.label_ == u'NORP':
            entityCount[NORP]+=1
        elif ent.label_ == u'FACILITY':
            entityCount[FACILITY] +=1
        elif ent.label_ == u'ORG':
            entityCount[ORG] +=1
        elif ent.label_ == u'GPE':
            entityCount[GPE] += 1
        elif ent.label_ == u'LOC':
            entityCount[LOC] +=1
        elif ent.label_ == u'PRODUCT':
            entityCount[PRODUCT] += 1
        elif ent.label_ == u'MONEY':
            entityCount[MONEY] +=1
        elif ent.label_ == u'QUANTITY':
            entityCount[QUANTITY] +=1
        elif ent.label_ == u'ORDINAL':
            entityCount[ORDINAL] +=1
        elif ent.label_ == u'CARDINAL':
            entityCount[CARDINAL] += 1
        else:
            entityCount[OTHER] += 1
    return entityCount

def getLocations(text):
    seen = set()
    locations = []
    processed_text = nlp(unicode(text))
    for ent in processed_text.ents:
        if ent.label_ == u'GPE':
            if not ent.text.upper() in seen:
                locations.append(str(ent.text.encode("ascii", "ignore").upper()))
                seen.add(ent.text.upper())
    return locations

def getNGrams(text):
    text = re.sub(r'[^\w]', ' ', text)
    N_GRAM_SIZE = 4
    ngrams = []
    processed_text = nlp(unicode(text))
    index = 0
    gramCount = 0
    for i in range(0,len(processed_text) - 3):
        localGram = []
        for i in range(0,4):    
            localGram.append(str(processed_text[index]).lower())
            index = index + 1
        gramCount+=1
        index = gramCount
        ngrams.append(localGram)
    return ngrams


def HTMLParser(url):
    response = get(url)
    extractor = Goose()
    article = extractor.extract(raw_html=response.content)
    text = article.cleaned_text
   
    results = getLocations(text)
    return results


def sentiment(textbody):
    neg = 0.0
    pos = 0.0
    neu = 0.0
    compound = 0.0
    total = 0

    sentences = nlp(unicode(textbody))

    sith = SentimentIntensityAnalyzer()

    for sentence in sentences.sents:
        score = sith.polarity_scores(sentence.text)
        neg += score['neg']
        neu += score['neu']
        pos += score['pos']
        compound += score['compound']
        total+=1

    results = []
    results.append(neg / total)
    results.append(pos / total)
    results.append(neu / total)
    results.append(compound / total)

    return results

def getMLP(textbody):
    send = []
    entities = countEntity(textbody)
    ngrams = getNGrams(textbody)
    sent = sentiment(textbody)


    send.append(entities)
    send.append(sent)
    return send


print(HTMLParser('http://www.cnn.com/2017/02/18/politics/donald-trump-florida-campaign-rally/index.html'))
