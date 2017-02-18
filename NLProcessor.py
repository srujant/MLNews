from spacy import load     
from goose import Goose
from requests import get    
import requests
nlp = load('en')    

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
    locations = []
    processed_text = nlp(unicode(text))
    for ent in processed_text.ents:
        if ent.label_ == u'GPE':
            locations.append(ent.text.upper())
    return locations

def getNGrams(text):
    N_GRAM_SIZE = 4
    ngrams = []
    processed_text = nlp(unicode(text))
    index = 0
    gramCount = 0
    for i in range(0,len(processed_text) - 3):
        localGram = []
        for i in range(0,4):
            localGram.append(processed_text[index])
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

    return text