"""
The main file of our BrickHack 6 project
Team Members: Brian Mirabito, Evan Donohue, Sangu Mbekelu
"""
import credential_loader

# Launching the program
def main():
    print("Project Starting!")
    credential_loader.load_creds()
    print(credential_loader.get_acs_creds())



# Obligatory if-guard
if __name__ == '__main__':
    main()