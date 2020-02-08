# Takes all the credential information from a txt file, keeping those secure
def load_creds():
    creds = []
    with open("credentials") as file:
        for line in file:
            creds.append(line)

    global endpoint
    endpoint = creds[0].strip("\n")
    global acs_key
    acs_key = creds[1].strip("\n")
    global tw_act
    tw_act = creds[3].strip("\n")
    global tw_acs
    tw_acs = creds[4].strip("\n")
    global tw_ck
    tw_ck = creds[5].strip("\n")
    global tw_cs
    tw_cs = creds[6].strip("\n")


# Dictionary with TW-API creds
def get_twitter_creds():
    return {"tw_act": tw_act, "tw_acs": tw_acs, "tw_ck": tw_ck, "tw_cs": tw_cs}

# Dictionary with ACS creds
def get_acs_creds():
    return {"endpoint": endpoint, "key": acs_key}

