"""
The main file of our BrickHack 6 project
Team Members: Brian Mirabito, Evan Donohue, Sangu Mbekelu
"""
import credential_loader
import GetData
import analyze as anyl
import visualize as vis
import matplotlib.pyplot as plt


# Launching the program
def main():
    print("Project Starting!")
    credential_loader.load_creds()
    anyl.set_keys(credential_loader.get_acs_creds())
    GetData.set_globals(credential_loader.get_twitter_creds())

    title = "Twitter's Feelings on KC Winning the Superbowl"
    labels = 'Positive', 'Negative', 'Neutral'  # 'Positive', 'Negative', 'Neutral'
    plot = vis.pie_chart(30, 45, 25, title, labels)
    # plt.show()
    print(plt.style.available)
    vis.image_gen(90)


# Obligatory if-guard
if __name__ == '__main__':
    main()
