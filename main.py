"""
The main file of our BrickHack 6 project
Team Members: Brian Mirabito, Evan Donohue, Sangu Mbekelu
"""
import credential_loader
import get_data
import analyze as anyl
import visualize as vis
import trending
import matplotlib.pyplot as plt
import os
import tweet


def clear_used_charts(name):
    if os.path.isfile(name):
        os.remove(name)
    else:
        print("Error: " + name + " not found.")


# Launching the program
def main():
    print("Project Starting!")
    credential_loader.load_creds()
    anyl.set_keys(credential_loader.get_acs_creds())
    get_data.set_globals(credential_loader.get_twitter_creds())
    trending.set_globals(credential_loader.get_twitter_creds())
    tweet.set_globals(credential_loader.get_twitter_creds())

    pngs = []
    trends = trending.top_ten_trending()
    for trend in trends:
        tweets = get_data.hashtag_pull(trend, 70)
        feels = anyl.sent_analysis(tweets)
        vis.piechart_gen(feels['positive'], feels['negative'], feels['neutral'], "Twitters feeling on " + trend,
                         trend)
        path = "out/" + trend + ".png"
        pngs.append(path)
        tweet.post_tweet(trend, path)

    for name in pngs:
        clear_used_charts(name)

    # vis.snapshot_gen(90)


# Obligatory if-guard
if __name__ == '__main__':
    main()
