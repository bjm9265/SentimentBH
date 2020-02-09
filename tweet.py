import tweepy


#  setup functionality for tweepy api. See get_data for more documentation on the method
def set_globals(credentials):
    # Twitter dev account given consumer key
    global consumer_key
    consumer_key = credentials["tw_ck"]

    # Twitter dev account given secret consumer key
    global consumer_secret
    consumer_secret = credentials["tw_cs"]

    # Twitter dev account given access token
    global access_token
    access_token = credentials["tw_act"]

    # Twitter dev account given secret access token
    global access_token_secret
    access_token_secret = credentials["tw_acs"]

    # 0Auth Handler function for tweepy
    global authInfo
    authInfo = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authInfo.set_access_token(access_token, access_token_secret)

    # tweepy api object
    global twapi
    twapi = tweepy.API(auth_handler=authInfo, wait_on_rate_limit=True)


#  Simple one line method for posting a tweet automatically
def post_tweet(name):
    twapi.update_status(status="Twitters feelings on " + name, media_ids="/out/" + name + ".png")
