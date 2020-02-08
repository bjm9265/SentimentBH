import tweepy
import credential_loader

credential_loader.load_creds()
credentials = credential_loader.get_twitter_creds()

consumer_key = credentials["tw_ck"]
consumer_secret = credentials["tw_cs"]
access_token = credentials["tw_act"]
access_token_secret = credentials["tw_acs"]

authInfo = tweepy.OAuthHandler(consumer_key, consumer_secret)
authInfo.set_access_token(access_token, access_token_secret)

twapi = tweepy.API(authInfo)

def set_keys(credentials):
    global consumer_key
    consumer_key = credentials["tw_ck"]
    global consumer_secret
    consumer_secret = credentials["tw_cs"]
    global access_token
    access_token = credentials["tw_act"]
    global access_token_secret
    access_token_secret = credentials["tw_acs"]

def hashtag_pull(hash, amount):
    for i in range(amount):
        tweets = twapi.search(hash)

    return tweets
