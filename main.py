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


def clear_used_charts(name):
    file = "/out/" + name + ".png"
    if os.path.isfile(file):
        os.remove(file)
    else:
        print("Error: " + file + "not found.")


# Launching the program
def main():
    print("Project Starting!")
    credential_loader.load_creds()
    anyl.set_keys(credential_loader.get_acs_creds())
    get_data.set_globals(credential_loader.get_twitter_creds())
    trending.set_globals(credential_loader.get_twitter_creds())
    txt = "bitch boy slap fight"
    txt = get_data.swap_curses(txt)
    print(txt)

    trends = trending.top_ten_trending()
    for trend in trends:
        tweets = get_data.hashtag_pull(trend, 70)
        feels = anyl.sent_analysis(tweets)
        vis.piechart_gen(feels['positive'], feels['negative'], feels['neutral'], "Twitters feeling on " + trend,
                         trend)

    # vis.snapshot_gen(90)


# Obligatory if-guard
if __name__ == '__main__':
    main()
