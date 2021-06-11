# %%
import requests
import time
import calendar
from datetime import datetime
import re

# %%
def ruta(*args):
    url = 'https://api.github.com/'
    return url + '/'.join(args)

# %%
respuesta = requests.get(ruta('users','herguejuan'))
respuesta.json()
# %%
respuesta.headers
# %%
respuesta.headers['X-RateLimit-Remaining']
# %%
respuesta.headers['Date']
# %%
reset = respuesta.headers['X-RateLimit-Remaining']
reset
# %%
time.ctime(int(reset))
# %%
def traducir_hora(hora):
    try:
        hora = float(hora)
    except:
        hora = re.findall(r"\d.*\d",hora)[0]
        hora = datetime.strptime(hora, "%d %b %Y %X").utctimetuple()
        hora = calendar.timegm(hora)
    return time.ctime(hora)
# %%
traducir_hora(respuesta.headers['Date'])    
# %%
directories = ('users', 'herguejuan', 'repos')
print(ruta(directories))
repos = requests.get(ruta(directories))
print(repos)

# %%
repos = requests.get(ruta('users', 'Herguejuan', 'repos'))
repos.json()
# %%
ruta('repos', 'herguejuan', 'lab-web-scrapping','contents','your-code')
your_code = requests.get(ruta('users', 'Herguejuan', 'repos'))
your_code.json()

# %%
for file in your_code.json():
    print(file['path'])
# %%
# PyGitHub

