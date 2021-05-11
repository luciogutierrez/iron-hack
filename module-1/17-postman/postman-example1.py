# %%
import requests
url = "http://localhost:8000/api/customers/"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "1432412f-9bc5-be13-a8a4-6f93e31feba4"
    }
response = requests.request("POST", url, headers=headers)
print(response.text)
# %%
