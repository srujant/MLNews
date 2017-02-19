import json
import geojson

file = "./template.json"

with open(file, 'r') as f:
	read_data = f.read()

x =  geojson.loads(read_data)

x['features'][0]['properties']['name'] = 'Afghanistan'

x['features'][0]['properties']['info'] = {'dfesf': {'fesfes': 'feaf'}}


test = './test.geojson'
with open(test, 'w') as outfile:
	geojson.dump(x, outfile)
