# %% 
import requests

respuesta = requests.get("https://flask-zahid.herokuapp.com/recipes/1")
respuesta.json()
respuesta = requests.post("https://flask-zahid.herokuapp.com/recipes", json = { "description": "La receta de Zahid",
                                                                               "name": "Ponc al carbon"})
respuesta.json()


# %%
