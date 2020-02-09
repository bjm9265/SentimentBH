import tweepy


#  Duplicated code from get_data
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


#  get_trending function takes the top 50 trending in the United States using the WOE ID
def get_trending():
    trends = []
    US_woe_id = 23424977

    US_trends = twapi.trends_place(US_woe_id)
    for trend in US_trends:

        if trend in trends:
            pass
        else:
            trends.append(trend)

    return trends


#  top_ten_trending function cuts the top 50 down to 10, and puts their names in a list of
def top_ten_trending():
    Trends = []
    trends = Get_trending()
    tentrends = trends[0]["trends"][0:9]
    for i in range(len(tentrends)):

        Trends.append(tentrends[i]['name'])

    return Trends



