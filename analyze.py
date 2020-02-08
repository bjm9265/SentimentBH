from azure.ai.textanalytics import single_analyze_sentiment
from azure.ai.textanalytics import single_detect_language

# Endpoint and key information for submitting text for analysis through
# Azure Cognitive Services [ACS]
ep = ""
key = ""
# The language code to check for, all others are discarded
lang_code = "en"


# tweets : contains the cleaned text from the data pulling class to perform sentiment analysis
def sent_analysis(tweets):
    # Check the data for the correct language
    concat_tweets = ""
    for tweet in tweets:
        resp = single_detect_language(endpoint=ep, credential=key, input_text=tweet)
        if resp.primary_language.iso6391 != "en":
            # Delete the tweet from the list
            print("Removing non-"+lang_code+" tweet")

        concat_tweets += (tweet + " ")

    # Performing analysis of all the text through ACS
    resp = single_analyze_sentiment(endpoint=ep, credential=key, input_text=concat_tweets)

    # Getting raw scores for the entire population of tweets
    pop_pos = resp.document_scores.positive
    pop_neg = resp.document_scores.negative
    pop_overall = resp.sentiment
    # Converting the raw score to a percentage
    pop_pos_per = pop_pos*100
    pop_neg_per = pop_neg*100

    print("Overall Sentiment: "+pop_overall)
    print("Positivity: "+pop_pos_per)
    print("Positivity: " + pop_neg_per)

