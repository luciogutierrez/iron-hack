# %%
from bs4 import BeautifulSoup
import requests
import json
# %%
if __name__ == "__main__":
    url = 'https://www.google.com.mx'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content

file = open('google.html','wb')
file.write(content)
file.close()
# %%
if __name__ == "__main__":
    url = 'http://httpbin.org/get?nombre=Lucio&curso=python'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# %%
if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    args = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        content = response.content

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# %%
if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    args = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        response_json = response.json()

print(json.dumps(response_json, indent=2))
origin = response_json['origin']
print(origin)

# %%
if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    args = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        response_json = json.loads(response.text)

print(json.dumps(response_json, indent=2))
origin = response_json['origin']
print(origin)

# %%
# Metodo Post
if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    # payload = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    # response = requests.post(url, json=payload)

    data = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        content = response.content

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# print(json.dumps(response_json, indent=2))
# origin = response_json['origin']
# print(origin)

# %%
# enviar encabezados al servidor
if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    payload = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    headers = {'Content-Type':'application/json','Access-Token':'12345'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        content = response.content

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# %%
# recibir encabezados del servidor
if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    payload = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    headers = {'Content-Type':'application/json','Access-Token':'12345'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
print(server)
# print(headers_response)

# %%
# Metodo put 
if __name__ == "__main__":
    url = 'http://httpbin.org/put'
    payload = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    headers = {'Content-Type':'application/json','Access-Token':'12345'}
    response = requests.put(url, json=payload)

    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
print(server)
# print(headers_response)

# %%
# Metodo delete 
if __name__ == "__main__":
    url = 'http://httpbin.org/delete'
    payload = {'nombre':'Lucio','curso':'python','nivel':'intermedio'}
    headers = {'Content-Type':'application/json','Access-Token':'12345'}
    response = requests.delete(url, json=payload)

    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
print(server)
# print(headers_response)

# %%
if __name__ == "__main__":
    url = "https://www.harley-davidson.com/content/dam/h-d/images/category-images/2021/hero-cards-3-up/street-motorcycle-1x1.jpg"

    # el parametro strema realiza la petición sin descargar el contenido
    # deja la conexion abierta para bajar el contenido posteriomente
    response = requests.get(url, stream=True)

    with open('image.jpg','wb') as file:
        # el metodo iter_conten baja poco a poco el contenido
        for chunk in response.iter_content():
            file.write(chunk)
    response.close()