import os

from google.appengine.api import memcache, users
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.template import render
from google.appengine.ext.webapp.util import run_wsgi_app

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

class GuestBook(webapp.RequestHandler):
    def post(self):
        data = TweetsText()
        data.companyName = 'Tweets Analyzer'
        data.tweetText = self.request.get('content')
        data.put()
        memcache.delete('tweetstext')
        self.redirect('/')

application = webapp.WSGIApplication([
    ( '/', MainHandler),
    ( '/sign', GuestBook),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
