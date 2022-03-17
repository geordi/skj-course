import json
import re
import urllib.request, urllib.error, urllib.parse
import tc_auth
from dataclasses import dataclass

PINK = '\033[95m'
RESET = '\033[0m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'

@dataclass
class Tweet:

    from_user : str
    text : str

    def __repr__(self):
        tags = re.findall(r'\#\w+', self.text)
        text = self.text
        for tag in tags:
            text = text.replace(tag, GREEN+tag+RESET)
        return f'{PINK}{self.from_user}:{RESET} {text}'

class Twitter:

    base_search_url = 'https://api.twitter.com/1.1/search/tweets.json?q={}&count=5&tresult_type=popular'

    def __init__(self, *search):
        self.client = tc_auth.twitter_auth()
        self.search = search

    def create_search_url(self):
        escaped_search = []
        for word in self.search:
            escaped_search.append(word.replace('#', '%23'))
        search_str = '%20'.join(escaped_search)
        return Twitter.base_search_url.format(search_str)

    def download(self):
        url = self.create_search_url()
        self.response, self.data = self.client.request(url)

    def decode_json(self):
        self.decoded_json = json.loads(self.data.decode('utf-8'))

    def get_tweets(self):
        self.download()
        self.decode_json()

        statuses = self.decoded_json['statuses']

        for status in statuses:
            from_user = status['user']['name']
            text = status['text']

            yield Tweet(from_user, text)

t = Twitter('#django', '#python')
tweets = t.get_tweets()

for tweet in tweets:
    print(tweet)
