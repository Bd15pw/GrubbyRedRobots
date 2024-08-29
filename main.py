import requests

r = requests.get('https://rickandmortyapi.com/api/character')

content = r.json()
characters = content['results']



for x in characters:
  print(x['name'] +": "+ x['location']['name']['name'])
  print(x['name'])