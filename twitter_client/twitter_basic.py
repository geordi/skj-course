import json
import urllib

import tc_auth

# https://dev.twitter.com/docs/api/1.1/get/search/tweets

client = tc_auth.twitter_auth()

searchURL = 'https://api.twitter.com/1.1/search/tweets.json?q=python&count=5&tresult_type=popular'

response, data = client.request(searchURL)

print(data)

decoded_json = json.loads(data.decode('utf-8'))

statuses = decoded_json['statuses']

for status in statuses:
    print('{}: {}'.format(status['user']['name'], status['text']))

