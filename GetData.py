import tweepy
import re

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

def strip_links(text):
    link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], "")
    return text

def strip_tw_chars(text):
    x = text.replace("#", "")
    y = x.replace("@", "")
    z = y.replace("\n", " ")
    l = z.replace("&amp", "and")
    return l


def format_text(text):
    tweet = text
    tweet = strip_links(tweet)
    tweet = strip_tw_chars(tweet)
    return tweet

def hashtag_pull(query, amount):
    text = []
    parse = ""
    dup_check = ""
    tweets = twapi.search(q=query, lang="en", count=amount, tweet_mode="extended")
    for tweet in tweets:
        if 'retweeted_status' in dir(tweet):
            parse = format_text(tweet.retweeted_status.full_text)
            parse = format_text(parse)
            if parse == dup_check:
                pass
            else:
                text.append(parse)
                dup_check = parse
        else:
            parse = format_text(tweet.full_text)
            if parse == dup_check:
                pass
            else:
                text.append(parse)
                dup_check = parse

    return text
