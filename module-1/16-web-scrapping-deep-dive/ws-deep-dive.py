# %%
import requests
# %%
r1 = requests.get('https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/the-html5-breakfast-site.html')
print(r1.status_code)
# %%
r2 = requests.get('https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/forbidden')
print(r2.status_code)
# %%
r3 = requests.get('http://google.com')
print(r3.history)
# %%
print(r3.history[0].text)

# %%
import requests
url = 'http://google.com'
r = requests.get(url)
if r.status_code < 200:
    print('request was not successful')
elif r.status_code >= 400 and r.status_code < 500:
    print('request failes because the resource either does not exists or is forbidden')
else:
    print('request failes because the response server encountered an error')    
        


# %%
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response.content)

# %%
import asyncio, requests

urls = [
   'https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/breakfast.jpg',
   'https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/forbidden',
   'https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/the-html5-breakfast-site.html'
]

async def main():
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(None, requests.get, url) for url in urls]
    for response in await asyncio.gather(*futures):
        print(response.status_code)
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# %%
import requests, time

urls = [
    'https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/breakfast.jpg',
    'https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/forbidden',
    'https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/documents/the-html5-breakfast-site.html'
]

for url in urls:
    response = requests.get(url)
    print(response.status_code)
    time.sleep(1)

# %%
