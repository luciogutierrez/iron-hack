# %%
import requests
import json

# %%
def get_pokemons(url = "http://pokeapi.co/api/v2/pokemon-form", offset=0):
    args = {'offset':offset} if offset else {}
    response = requests.get(url, params=args)
    
    if response.status_code== 200:
        payload = response.json()
        pokemons = payload.get('results',[])

        if pokemons:
            for pokemon in pokemons:
                name = pokemon['name']
                print(name)
        next = input('Continuar listando [y/n]').lower()
        if next == 'y':
            get_pokemons(offset=offset+20)

if __name__ == '__main__':
    url = "http://pokeapi.co/api/v2/pokemon-form"
    get_pokemons()

# %% 
import requests
import json

# %% 
client_id = 'f8ddb5fff9280f805b83'
client_secret = '1aba387d460278e6b8beb54960f2619db70b9440'
code = '58f1db7bc9921633310b'
access_token = ''

#https://github.com/login/oauth/authorize?client_id=f8ddb5fff9280f805c83&scope=response
if __name__ == '__main__':
    url = 'https://gateway.marvel.com/'
    # payload = {'client_id': client_id, 'client_secret':client_secret, 'code':code}
    # headers = {'Accept': 'application/json'}
    # response = requests.post(url, json=payload, headers=headers)
    response = requests.post(url)
    print(response.status_code)
    if response.status_code == 200:
        response_json = json.loads(response.text)  #response.json()
        print(response_json)


# %%
url= 'http://gateway.marvel.com/v1/public/comics'
response = requests.get(url)
Params: {
  "apikey": "your api key",
  "ts": "a timestamp",
  "hash": "your hash"
}
Headers: {
  'Accept':'*/*'
}