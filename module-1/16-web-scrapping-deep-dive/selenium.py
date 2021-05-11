# %%
import pandas as pd
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# %%
driver = webdriver.Chrome('D:\Portable\chromedriver\chromedriver.exe')
# %%
driver.get('http://www.python.org/')
# %%
assert "Python" in driver.title
# %%
# esperar 5 segundos
time.sleep(5)
# %%
elem = driver.find_element_by_name('q')
# %%
elem.clear()
# %%
elem.send_keys('pycon')
# %%
elem.send_keys(Keys.RETURN)
# %%
assert "No results foud." not in driver.page_source
# %%
time.sleep(5)
# %%
driver.close()
# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
# %%
