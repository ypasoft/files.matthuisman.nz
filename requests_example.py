import sys
import requests
from requests.exceptions import RequestException

# Usually GET or POST
method = 'GET'

# The URL to request
url = 'http://www.example.com'

# User-agent etc
headers = {

}

# Used for GET requests
params = {

}

# Used for POST requests
payload = {
    
}

try:
    response = requests.request(method, url, params=params, data=payload, headers=headers)
except RequestException as e:
    print(e)
    sys.exit(0)

print(response.text)

print("{0} code".format(response.status_code))

if response.ok:
    print("OK!")
else:
    print("ERROR")

try:
    print(response.json())
except:
    print("Not JSON data")
