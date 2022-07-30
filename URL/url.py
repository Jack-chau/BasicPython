# Read a url content
# Method 1: Build-in urllib.request
'''import  urllib.request as request
url = 'https://kfsoft.info/'
conn = request.urlopen(url)
result = conn.read()
print(result)

for key,value in conn.getheaders():
    print(key + " : " + value)'''

'''# Method 2: Requests

import requests
url = 'https://kfsoft.info/'
response = requests.get(url)
#rint(response.text)

for key, value in response.headers.items():
    print(key + " : " + value)'''










