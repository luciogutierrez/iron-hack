# %%
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import re
from bs4 import BeautifulSoup

content = requests.get('https://www.reforma.com/libre/estatico/rss/').content
soup = BeautifulSoup(content, 'xml')
# soup

# %%
rss = soup.select('div.btnRSS a')
rss

# %%
rss_re = [re.findall("(?=rss).*$", cat)[0] for cat in rss] 
rss_re

# %%
url = "https://www.reforma.com/rss/portada.xml"
# rss_cat = [url + rss for rss in rss_re]
# rss_cat
# %%
content = requests.get(url).content
soup = BeautifulSoup(content, 'xml')
root = ET.fromstring(content)
root

# %%
titles = soup.find_all('title')
titles

# %%
titles2 = [title.text for title in titles]
titles2[2:]
# %%
titles3 = [title.text for title in root.iter('title')]
titles3
# %%
