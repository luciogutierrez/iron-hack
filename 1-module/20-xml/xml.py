# %%
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import re
from bs4 import BeautifulSoup

response = requests.get('https://www.inegi.org.mx/rss/noticias/xmlfeeds?p=2,1')
response.status_code

inegi_news = response.content
# print(inegi_news)
# %%
with open('inegi_news_2021.xml', 'wb') as fw:
    fw.write(inegi_news)

# %%
tree = ET.parse('inegi_news_2021.xml')

# %%
tree = ET.fromstring(inegi_news)
tree

# %%
tree.tag
tree.attrib
# %%
tree[0][0]
for elem in tree:
    for subel in elem:
        for subsubel in subel:
            print(subsubel.text)


# %%
tree = ET.parse('inegi_news_2021.xml')
tree
# %%
root = tree.getroot()
root
# %%
for child in root:
    for grandchild in child:
        print(grandchild.tag, grandchild.attrib)
# %%
elements = [el.tag for el in root.iter()]
elements

# %%
for title in root.iter('title'):
    print(title.text)
# %%

