import oauth2 as oauth
import urllib

# Register on Twitter to obtain your keys
CONSUMER_KEY=''
CONSUMER_SECRET=''
ACCESS_KEY='136577499-Iw71gSAtAXA0NdltH8EGb9wj0GeHtU6eQL920N0k'
ACCESS_SECRET='tdzTRgoudJ9w6W6Vt8a2p9mUwEp2X0olELF9o6DmBw'

def twitter_auth():
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)

    return client

