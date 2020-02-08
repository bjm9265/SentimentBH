"""
The main file of our BrickHack 6 project
Team Members: Brian Mirabito, Evan Donohue, Sangu Mbekelu
"""
import credential_loader
import analyze
import GetData


# Launching the program
def main():
    print("Project Starting!")
    credential_loader.load_creds()
    analyze.set_keys(credential_loader.get_acs_creds())
    GetData.set_globals(credential_loader.get_twitter_creds())
    # print(credential_loader.get_acs_creds())


# Obligatory if-guard
if __name__ == '__main__':
    main()