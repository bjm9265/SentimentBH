"""
The main file of our BrickHack 6 project
Team Members: Brian Mirabito, Evan Donohue, Sangu Mbekelu
"""
import credential_loader
import GetData
import analyze as anly
import visualize as vis

# Launching the program
def main():
    print("Project Starting!")
    credential_loader.load_creds()
    anly.set_keys(credential_loader.get_acs_creds())
    GetData.set_globals(credential_loader.get_twitter_creds())

    plot = vis.pie_chart(50, 50, "Feelings on Who Won the Superbowl")
    plot.show()


# Obligatory if-guard
if __name__ == '__main__':
    main()