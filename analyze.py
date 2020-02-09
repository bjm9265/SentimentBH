from azure.ai.textanalytics import single_analyze_sentiment
from azure.ai.textanalytics import single_detect_language

# The language code to check for, all others are discarded
lang_code = "en"


# creds : dict - The dictionary containing the endpoint and ACS key to perform analysis
def set_keys(creds):
    global ep; ep = creds["endpoint"]
    global key; key = creds["key"]


# tweets : iterate-able - The list of tweets that will be checked and analyzed
def sent_analysis(tweets):
    # Check the data for the correct language
    concat_tweets = ""  # A long string containing all the tweet text, so that it only takes one call to analyze
    for tweet in tweets:
        resp = single_detect_language(endpoint=ep, credential=key, input_text=tweet)
        if resp.primary_language.iso6391 != "en":
            # Delete the tweet from the list
            print("Removing non-"+lang_code+" tweet")

        concat_tweets += (tweet + " ")

    # Performing analysis of all the text through ACS
    resp = single_analyze_sentiment(endpoint=ep, credential=key, input_text=concat_tweets)

    # Getting raw scores for the entire population of tweets (double)
    pop_pos = resp.document_scores.positive
    pop_neg = resp.document_scores.negative
    pop_neu = resp.document_scores.neutral
    pop_overall = resp.sentiment  # The overall sentiment is  a string, positive/neutral/negative
    # Converting the raw score to a percentage
    pop_pos_per = pop_pos*100
    pop_neg_per = pop_neg*100

    sentiments = {"sentiment": pop_overall, "positive": pop_pos, "negative": pop_neg, "neutral": pop_neu}
    return sentiments
