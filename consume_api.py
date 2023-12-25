import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/badges?order=desc&sort=rank&site=stackoverflow')
for data in response.json()['items']:
    if data['award_count'] > 5:
        print(data['rank'])
        print(data['link'])
    else:
        print('skipped')