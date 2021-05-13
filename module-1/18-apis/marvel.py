# %%
import requests
import json
from bs4 import BeautifulSoup

# %%
def get_superheros():
    url = 'http://gateway.marvel.com/v1/public/characters'
    args = {'apikey':'af18b752302271b4b7597d2abfb4c037',
            'ts': '1',
            'hash': '9d3c743d434a92951b6710ba2afa5d29'}
    headers = {'Content-Type':'application/json'}
    response = requests.get(url, params=args, headers=headers)

    print(response.status_code)
    if response.status_code== 200:
        response_json = response.json()

    return response_json

if __name__ == '__main__':
    None

# %%
superheros = get_superheros()
print(superheros)

# %%
# print(len(superheros))
# print(type(superheros))
# print(superheros.items())
print(superheros.keys())
# print(superheros.values())


# %%
list_sh = superheros['data']['results']
list_sh
    
# %%
print(type(list_sh[0]))
# %%
print(list_sh[0].keys())
# %%
print(list_sh[0].values())
# %%
beat = list_sh[0]
beat
# %%
hero = list_sh[0]['urls']
urlHero = hero[0]
urlHero    
# %%
urlHero = []
for hero in list_sh[0]['urls']:
    urlHero.append(hero['url'])
urlHero    

# %%
# 3 levels
urlHero = []
for hero in list_sh:
    for item in hero['urls']:
        print(item['url'])
    # urlHero.append(hero['url'])
urlHero    

# %%
# 2 levels
for hero in list_sh:
    print(hero['id'], hero['name'], hero['description'])

# %%
number = 4
print('id           : ' + str(list_sh[number]['id']))
print('name         : ' + list_sh[number]['name'])
print('description  : ' + list_sh[number]['description'])

# %%
