import tweepy
import pymongo
from bson import json_util
import json

consumer_key = "RXJWocF9m1fMfQnlP2ua7rG8v"
consumer_secret = "mCg63ep6GA35KU5lYmd0NOmgb6q1iEP9Ywg03DTuiEYZc32Cd6"
access_token = "283141461-x1XViSBImLaHxx5L6CwNlUoV5gVEQ562rjGTyrEA"
access_token_secret = "DfXbSTG8v3lFRsJlRwaRjYxdi7NVFiNmX8VS0uV4ydOHZ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


c = tweepy.Cursor(api.search, q='Airtel')
c.pages(10)

#Lets save the selected part of the tweets inot json
tweetJson = []
for tweet in c.items():
    if tweet.lang == 'en':
        createdAt = str(tweet.created_at)
        authorCreatedAt = str(tweet.author.created_at)
        tweetJson.append({'tweetText':tweet.text, 'tweetID':tweet.id, 'tweetCreatedAt':createdAt,
          'authorScreenName':tweet.author.screen_name,
          'authorName': tweet.author.name,
          'authorFriendsCount':tweet.author.friends_count,
          'authorStatusesCount':tweet.author.statuses_count,
          'authorCreatedAt': authorCreatedAt
        })

print json.dumps(tweetJson)
