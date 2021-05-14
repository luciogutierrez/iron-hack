# %%
import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, render_template

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

app = Flask(__name__)

@app.route('/')
def home():
    superheros = get_superheros()
    list_sh = superheros['data']['results']

    heros = {"data":[]}
    def add_hero(hero):
        heros["data"].append(hero)

    for hero in list_sh:
        imageUrl = ''
        imageUrl += hero['thumbnail']['path']
        imageUrl += '.'
        imageUrl += hero['thumbnail']['extension']
        item = {}
        item['hero_name'] = hero['name']
        item['hero_desc'] = hero['description']
        item['hero_img'] = imageUrl
        item['hero_url'] = hero['urls'][0]['url']
        add_hero(item)

    longitud = len(list_sh)

    return render_template('home.html', heros=heros, longitud=longitud)

@app.route('/about') 
def about():
    notas = ("nota1","nota2","nota3","nota4","nota5","nota6")
    return render_template('about.html', notas=notas)

if __name__ == '__main__':
    app.run(debug=True)
