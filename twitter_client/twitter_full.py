import json
import re
import urllib.request, urllib.error, urllib.parse
import tc_auth

PINK = '\033[95m'
RESET = '\033[0m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'

class Tweet(object):

    def __init__(self, from_user, text, geo):
        self.from_user = from_user
        self.text = text
        self.geo = geo

    def __repr__(self):
        tags = re.findall(r"\#\w+", self.text)
        text = self.text
        for tag in tags:
            text = text.replace(tag, GREEN+tag+RESET)
        out = "{0}, Text: {1}, Geo: {2}".format(self.from_user, text, self.geo)
        return PINK + "From: " + RESET + out

class Twitter(object):

    base_search_url = 'https://api.twitter.com/1.1/search/tweets.json?q={}&count=5&tresult_type=popular'

    def __init__(self, *search):
        self.client = tc_auth.twitter_auth()
        
        self.search = search
        self.decoded_json = None

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

        tweets = []
        for status in statuses:
            from_user = status['user']['name']
            text = status['text']
            geo = status['geo']
            tweet = Tweet(from_user, text, geo)
            tweets.append(tweet)
        return tweets


t = Twitter('#django', '#python')
tweets = t.get_tweets()

for tweet in tweets:
    print(tweet)
