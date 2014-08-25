import tweepy

consumer_key = "RXJWocF9m1fMfQnlP2ua7rG8v"
consumer_secret = "mCg63ep6GA35KU5lYmd0NOmgb6q1iEP9Ywg03DTuiEYZc32Cd6"
access_token = "283141461-x1XViSBImLaHxx5L6CwNlUoV5gVEQ562rjGTyrEA"
access_token_secret = "DfXbSTG8v3lFRsJlRwaRjYxdi7NVFiNmX8VS0uV4ydOHZ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

c = tweepy.Cursor(api.search, q='Airtel')
for tweet in c.items():
    print tweet.screenname, tweet.text
