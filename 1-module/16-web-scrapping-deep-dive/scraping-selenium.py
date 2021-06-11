# %%
## Alies Parson Project
import time
import re
import sys
import requests
import numpy as np
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# %%
url = 'https://sale.aliexpress.com/es/__pc/global_selection_pc.htm?spm=a2g0o.home.01002.3.39a670e51lwa26'
aliexpress = requests.get('https://sale.aliexpress.com/es/__pc/global_selection_pc.htm?spm=a2g0o.home.01002.3.39a670e51lwa26').content
# %%
world_selection = BeautifulSoup(aliexpress,'html')
# %%
world_selection
# %%
driver = webdriver.Chrome()
# %%
driver.get(url)
# %%
page_source = driver.page_source
driver.quit()
# quit cierra la pestaña no el driver
# %%
world_selection = BeautifulSoup(page_source,'lxml')
# %%
link_to_product = world_selection.select('div.gs-item-inner a[href]')
# %%
link_to_product
# %%
links = [link['href'] for link in link_to_product]
links
# %%
len(links)
# %%
driver = webdriver.Chrome()
driver.get(url)
# %%
ActionChains(driver).send_keys(Keys.END).perform()
time.sleep(3)
ActionChains(driver).send_keys(Keys.END).perform()
time.sleep(3)
ActionChains(driver).send_keys(Keys.END).perform()
time.sleep(3)
page_source = driver.page_source
driver.quit()
# %%
world_selection = BeautifulSoup(page_source, 'lxml')

# %%
# print(world_selection.prettify())
# %%
sys.getsizeof(world_selection)
# %%
link_to_product = world_selection.select('div.gs-item-inner a[href]')
# %%
type(link_to_product)
# %%
sys.getsizeof(link_to_product)
# %%
links = [str(link['href']) for link in link_to_product]
links
# %%
len(links)
# %%
protocol = 'https:'
links_with_protocol = [protocol + link for link in links]
# %%
first_product = links_with_protocol[0]
first_product
# %%
driver = webdriver.Chrome()
driver.get(first_product)
time.sleep(5)
ActionChains(driver).send_keys(Keys.END).perform()
time.sleep(5)
page_source = driver.page_source
driver.quit()
# %%
prod_world_selection = BeautifulSoup(page_source, 'lxml')
# %%
sys.getsizeof(world_selection)
# %%
product_name = prod_world_selection.find('div', class_='product-title').get_text()
product_name
# %%
product_price = prod_world_selection.find('span', class_='product-price-value').get_text()
product_price

# %%
product_order = prod_world_selection.find('div', class_='product-reviewer')
product_order

# %%
text = [x.text for x in product_order]
text
# %%
avg_rating = re.findall(r'\d\.\d', text[0])
avg_rating
# %%
num_reviewer = re.findall(r'\d+', text[1])
num_reviewer
# %%
num_order = re.findall(r'\d+', text[2])
num_order
# %%
def get_links(url:str):
    randint = np.random.randint
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(10)
    ActionChains(driver).send_keys(Keys.END).perform()
    time.sleep(randint(5, high=10))
    ActionChains(driver).send_keys(Keys.END).perform()
    time.sleep(randint(5, high=10))
    ActionChains(driver).send_keys(Keys.END).perform()
    page_source = driver.page_source
    driver.quit()
    return page_source    


# %%
def source_parsing(page_source:str):
    world_selection = BeautifulSoup(page_source, 'lxml')
    links_to_product = world_selection.select('div-gs-item-inner a[href]')
    links =  ['https:'+link['href'] for link in links_to_product]
    return links_with_protocol
# %%
source = get_links(url=url)
# %%
list_of_links = source_parsing(source)
# %%
list_of_links[:2]
# %%
def random_keypress_generator():
    keys = [Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_UP,\
            Keys.ARROW_RIGHT, Keys.DOWN, Keys.END, Keys.PAGE_UP]
    action = np.random.choice(keys, p=[0.3,0.05,0.05,0.1,0.2,0.2,0.1])
    return action   
# %%
def web_content(link:str):
    random =  np.random.choice
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(random(10))
    for ran in range(random(7)):
        ActionChains(driver).send_keys(random_keypress_generator).perform()
        time.sleep(3)
    page_source = driver.page_source
    driver.close()        
    return page_source
# %%
