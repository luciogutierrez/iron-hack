# %%
import requests
import base64
from urllib.parse import urlencode

# get credentials
def get_key(key):
    with open('C:/Windows/AppsKeys/Spotify/'+key+'.txt', 'r') as file_read:
        app_key = file_read.readline()
    return app_key

client_id = get_key('client_id')
client_secret = get_key('client_secret')

credentials_developer = f'{client_id}:{client_secret}'
print(type(credentials_developer))

# %%
credentials_developer_b64 = base64.b64encode(credentials_developer.encode())
print(type(credentials_developer_b64))

# %%
token_url = 'https://accounts.spotify.com/api/token'
method = "POST"

datos_token = {'grant_type': 'client_credentials'}
token_headers = {'Authorization':f'Basic {credentials_developer_b64.decode()}'} 


# %%
request = requests.post(token_url, data=datos_token,headers=token_headers)
print(request.json())
# %%
datos = request.json()
datos.keys()
# %%
datos['access_token']
# %%
# https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V
authorization = {'Authorization': f'Bearer {datos["access_token"]}'}
authorization
# %%
query = urlencode({"q":"jbalvin","type":"artist"})
query
# %%
endpoint = "https://api.spotify.com/v1/search"
# %%
url_solicitud = f"{endpoint}?{query}"
url_solicitud

# %%
busca = requests.get(url_solicitud, headers=authorization)
busca.json()
# %%
resultado = busca.json()
# %%
import pandas as pd
df = pd.json_normalize((resultado['artists']['items']))
df

# %%
