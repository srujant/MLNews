import json
import requests
from eventregistry import *

topics = ['general', 'technology', 'sport', 'business', 'entertainment', 'gaming', 'music', 'science-and-nature']

def getEventsAPI():
    er = EventRegistry()
    