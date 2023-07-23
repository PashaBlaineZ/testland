import requests
import json
url = 'http://localhost:8000'
data = {'keyinput': 'hentai'}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.json()['keyinput'])