import os
from google.appengine.api import memcache, users
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.template import render
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import oauth
import datetime
import sys
sys.path.insert(0, 'tweepy')
import tweepy
class TweetsTextDB(db.Model):
    createdAt             = db.DateTimeProperty(auto_now_add=True)
    logedInCustomer       = db.StringProperty()
    companyName           = db.StringProperty()
    tweetID               = db.StringProperty()
    tweetText             = db.StringProperty()
    tweetCreatedAt        = db.DateTimeProperty()
    authorScreenName      = db.StringProperty(required=False)
    authorName            = db.StringProperty(required=False)
    authorFriendsCount    = db.IntegerProperty(required=False)
    authorFollowersCount  = db.IntegerProperty(required=False)
    authorStatusesCount   = db.IntegerProperty(required=False)
    authorCreatedAt       = db.DateTimeProperty()
class UserDB(db.Model):
    userNickName  = db.StringProperty()
    userEmailID   = db.StringProperty()
    userID        = db.StringProperty()
    createdAt     = db.DateTimeProperty(auto_now_add=True)
    logedInAt     = db.DateTimeProperty(auto_now=True)

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # Update the UserDB
        UserDBTable = UserDB()
        if user:
            # Check that user already exist in our DB then update the logedInAt time
            userExist = UserDBTable.gql("WHERE userEmailID = :1", userEmailID=user.email())
            if userExist is None:
                userDB = UserDBTable(userNickName  = user.nickname(),
                                userEmailID   = user.email(),
                                userID        = user.user_id()
                              )
                userDB.logedInAt = datetime.datetime.now()
                userDB.put()
            # else:
            #   userExist.logedInAt = datetime.datetime.now()
            #   userExist.put()

        # Get the tweets
        tweetstext = memcache.get('tweetstextdb')
        if not tweetstext:
            tweetstext = TweetsTextDB.all().order('-createdAt').fetch(10)
            memcache.add('tweetstextdb', tweetstext)

        context = {
            'companyNameList': ['Coursera', 'Google', 'Airtel'],
            'companyName': 'Tweets Analyzer',
            'user':      user,
            'tweetstext': tweetstext,
            'login':     users.create_login_url(self.request.uri),
            'logout':    users.create_logout_url(self.request.uri),
        }
        tmpl = os.path.join(os.path.dirname(__file__), 'top10tweets.html')
        self.response.out.write(render(tmpl, context))

class GetTweets(webapp.RequestHandler):
    def post(self):
      # Create object of DB
      data = TweetsTextDB()
      # For time just inserting the dummy data
      user = users.get_current_user()
      if user:
          customerName = user.nickname()
      else:
          customerName = 'anonymous'

      data.logedInCustomer = customerName
      data.companyName    = 'kprasadiitd'
      data.tweetID        = 'test-1'
      data.tweetText      = self.request.get('companyName')
      data.tweetCreatedAt = datetime.datetime.now().replace(day=1)
      data.authorScreenName = 'screen name'
      data.authorName       = 'Author Name'
      data.authorFriendsCount = 40
      data.authorFollowersCount = 200
      data.authorStatusesCount = 20
      data.authorCreatedAt      = datetime.datetime.now().replace(year=2001)
      # Now store the data into TweetsText DB Model
      data.put()

      #######
         #For time beingOptional Real-World Project
      ######
      # Get the Tweets from twitter API or From TwitterHandler
      companyName = self.request.get('companyName')
      companyNameList =  ['Coursera', 'Google', 'Airtel']
      if companyName not in companyNameList:
          self.redirect('/')
      else:
          # Read from stored DB
          # Will add today
          self.redirect('/')
      # THandler = TwitterHandler()
      # THandler.setTwitterSearchTerm(companyName)
      # tweetTextCotainer = THandler.getTweetsText()
      # for tweetText in tweetTextCotainer:
      #   data.companyName = companyName
      #   data.tweetText = tweetText
      #   data.put()

      memcache.delete('tweetstextdb')
      self.redirect('/')

#class ImportTweetsFromJson(webapp.RequestHandler):
# date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

class TwitterHandler(object):
  def __init__(self):
    self.textTweet = []
    self.searchterms = ''
    #access key for twitter api
    self.consumer_key = "RXJWocF9m1fMfQnlP2ua7rG8v"
    self.consumer_secret = "mCg63ep6GA35KU5lYmd0NOmgb6q1iEP9Ywg03DTuiEYZc32Cd6"
    self.access_token = "283141461-x1XViSBImLaHxx5L6CwNlUoV5gVEQ562rjGTyrEA"
    self.access_token_secret = "DfXbSTG8v3lFRsJlRwaRjYxdi7NVFiNmX8VS0uV4ydOHZ"
  def setTwitterSearchTerm(self, companyName):
    self.searchterms = companyName
  # it's about time to create a TwitterSearch object with our secret tokens
  def getTweetsText(self):
    auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
    auth.set_access_token(self.access_token, self.access_token_secret)

    api = tweepy.API(auth)

    c = tweepy.Cursor(api.search, q='Airtel')
    for tweet in c.items():
        self.textTweet.append(tweet.text)

    return self.textTweet

    # tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    # tso.setKeywords([self.searchterms]) # let's define all words we would like to have a look for
    # tso.setLanguage('en') # we want to see German tweets only
    # tso.setCount(1) # please dear Mr Twitter, only give us 1 results per page
    # tso.setIncludeEntities(False) # and don't give us all those entity information
    #
    # ts = TwitterSearch(
    #   consumer_key = self.api_key,
    #   consumer_secret = self.api_secret,
    #   access_token = self.access_token_key,
    #   access_token_secret = self.access_token_secret
    #   )
    # for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
    #   #print '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']
    #   self.textTweet.append('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
    #
    # return self.textTweet

application = webapp.WSGIApplication([
    ( '/', MainHandler),
    ( '/gettweets', GetTweets),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
