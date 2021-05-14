# %%
import requests
import base64
from urllib.parse import urlencode
# %%
client_id = '0ae93242eb074d1a8479c8072ede701a'
client_secret = '137093eb58fe477388bfc713ab927c9a'

# %%
credentials_developer = f'{client_id}:{client_secret}'
# %%
print(type(credentials_developer))
# %%
credentials_developer_b64 = base64.b64encode(credentials_developer.encode())
type(credentials_developer_b64)

# %%
credentials_developer_b64
# %%
{
    "access_token": "BQB1HyRzFCkWj8xmxKA5IfsdklZOTqRA5udXiozGOMJYL1W2yTGnl7tiKoRU_CVjvDEuyJsXQp9aHnkNk-k",
    "token_type": "Bearer",
    "expires_in": 3600
}

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
