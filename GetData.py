import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

authInfo = tweepy.OAuthHandler(consumer_key, consumer_secret)
authInfo.set_access_token(access_token, access_token_secret)

twapi = tweepy.API(authInfo)

'tweets = twapi.search("")'
