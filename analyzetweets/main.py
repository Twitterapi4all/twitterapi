import os


from google.appengine.api import memcache, users
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.template import render
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import oauth

class TweetsText(db.Model):
    createdAt   = db.DateTimeProperty(auto_now_add=True)
    author      = db.UserProperty()
    companyName = db.StringProperty(required=False)
    tweetText   = db.TextProperty(required=False)

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        tweetstext = memcache.get('tweetstext')
        if not tweetstext:
            tweetstext = TweetsText.all().order('-createdAt').fetch(10)
            memcache.add('tweetstext', tweetstext)
        context = {
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
      data = TweetsText()
      # Get the company name
      companyName = self.request.get('companyName')
      # Get the Tweets from twitter API or From TwitterHandler
      THandler = TwitterHandler()

      tweetTextCotainer = THandler.getTweetsText(companyName)

      for tweetText in tweetTextCotainer:
        #print tweetText
        data.companyName = companyName
        data.tweetText = tweetText
        data.put()

      memcache.delete('tweetstext')
      self.redirect('/')

class TwitterHandler():
  import urllib2 as urllib
  #access key for twitter api
  api_key = "RXJWocF9m1fMfQnlP2ua7rG8v"
  api_secret = "mCg63ep6GA35KU5lYmd0NOmgb6q1iEP9Ywg03DTuiEYZc32Cd6"
  access_token_key = "283141461-x1XViSBImLaHxx5L6CwNlUoV5gVEQ562rjGTyrEA"
  access_token_secret = "DfXbSTG8v3lFRsJlRwaRjYxdi7NVFiNmX8VS0uV4ydOHZ"
  _debug = 0
  oauth_token    = oauth.token(key=access_token_key, secret=access_token_secret)
  oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)
  signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
  http_method = "GET"
  http_handler  = urllib.HTTPHandler(debuglevel=_debug)
  https_handler = urllib.HTTPSHandler(debuglevel=_debug)
  def __init__(self):
    #self.companyName = companyName
    self.tweetsText = []

  def getTweetsText(self, companyName):
    if companyName is None:
      companyName = 'Airtel'
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%23" + companyName
    parameters = []
    response = self.twitterreq(url, "GET", parameters)
    for line in response:
      #print line.strip()
      self.tweetsText.append(line.strip())
    return self.tweetsText

  def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                               token=oauth_token,
                                               http_method=http_method,
                                               http_url=url,
                                               parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
      encoded_post_data = req.to_postdata()
    else:
      encoded_post_data = None
      url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response


application = webapp.WSGIApplication([
    ( '/', MainHandler),
    ( '/gettweets', GetTweets),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
