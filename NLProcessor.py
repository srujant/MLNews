from spacy import load                       # See "Installing spaCy"
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
            print(ent.text.upper())
    return locations

