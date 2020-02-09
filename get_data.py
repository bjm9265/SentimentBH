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


"""
Method to remove links from tweet text.
returns plaintext
"""


def strip_links(text):
    link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], "")
    return text


"""
Method for removing the #,@,\n characters in the tweet but keeping the string for the tag. Also fixes & signs appearing
as &amp
returns plaintext
"""


def strip_tw_chars(text):
    x = text.replace("#", "")
    y = x.replace("@", "")
    z = y.replace("\n", " ")
    l = z.replace("&amp", "and")
    return l


"""
Formatting helper method that makes both text strip calls
returns plaintext
"""


def format_text(text):
    tweet = text
    tweet = strip_links(tweet)
    tweet = strip_tw_chars(tweet)
    return tweet


"""
Main method that is responsible for querying the type of tweets
returns list of tweets as plaintext
"""


def hashtag_pull(query, amount):
    # Instantiate used variables
    text = []
    parse = ""
    # api tweet pull
    for tweet in tweepy.Cursor(twapi.search, q=query, count=100, lang="en", tweet_mode="extended").items(amount):
        if 'retweeted_status' in dir(tweet):
            parse = format_text(tweet.retweeted_status.full_text)
            parse = format_text(parse)
            if parse in text:
                pass
            else:
                text.append(parse)
        else:
            parse = format_text(tweet.full_text)
            if parse in text:
                pass
            else:
                text.append(parse)
    # list of pulled tweets as strings
    return text
