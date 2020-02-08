

def load_creds():
    creds = []
    with open("credentials.txt") as file:
        for line in file:
            creds.append(line)

    global endpoint
    endpoint = creds[0]
    global acs_key
    acs_key = creds[1]
    global tw_act
    tw_act = creds[3]
    global tw_acs
    tw_acs = creds[4]
    global tw_ck
    tw_ck = creds[5]
    global tw_cs
    tw_cs = creds[6]


def get_