from TwitterSearch import *
try:
    print "started"
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['Airtel']) # let's define all words we would like to have a look for
    tso.setLanguage('en') # we want to see German tweets only
    tso.setCount(50) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information
    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = "RXJWocF9m1fMfQnlP2ua7rG8v",
        consumer_secret = "mCg63ep6GA35KU5lYmd0NOmgb6q1iEP9Ywg03DTuiEYZc32Cd6",
        access_token = "283141461-x1XViSBImLaHxx5L6CwNlUoV5gVEQ562rjGTyrEA",
        access_token_secret = "DfXbSTG8v3lFRsJlRwaRjYxdi7NVFiNmX8VS0uV4ydOHZ"
     )

    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
