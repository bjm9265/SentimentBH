import tweepy

"""
Function to get the key/token credentials passed from the main. Sets global variables needed for pulling tweets
and instantiates the tweepy api.
"""


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
    twapi = tweepy.API(authInfo)


def hashtag_pull(tag, amount):
    text = []
    for i in range(amount):
        tweets = twapi.search(tag)
        for tweet in tweets:
            text.append(tweet.text)

    return text
