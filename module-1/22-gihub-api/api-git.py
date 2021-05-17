# %%
import requests
from github import Github
# %%
rep = g.get_repo('iron')
# %%
token = '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'
# %%
g = Github(token)
# %%
user = g.get_user()
user.login
# %%
repo = g.get_repo('ironhack-datalabs/scavenger')
content = repo.get_contents("")
# %%

# %%
content = repo.get_contents("15024")
# %%
lista_de_archivo = []
for contenido in content:
    if contenido.path != '.gitignore':
       contenido_adentro = repo.get_contents(contenido.path)
       for file in contenido_adentro:
           if file.path.endswith("scavengerhunt"):
               lista_de_archivo.append(file.path)

# %%
contenido_adentro = repo.get_contents(content[1].path)
# %%
lista_path = [carpeta.path for carpeta in content if carpeta.pth!='.gitignore']
# %%
contenido_adentro
# %%
for file in contenido_adentro:
    if file.path.endswith("scavengerhunt"):
        print(file.path)
# %%
