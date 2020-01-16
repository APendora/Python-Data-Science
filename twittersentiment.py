import tweepy
import csv

from textblob import TextBlob

consumer_key = 'raCorkjUnTu3Lfanzlxbd2UyX'
consumer_secret = 'xJANBDPP9Z2OPEMoasmjgvsvLntjT6rsA8cFZm9szzRahmJ9To'

access_token = '834523339-lAXZqqEqenxsHntQFROgLFengY2fe5jetmEdqFjU'
access_token_secret = 'euIuKl1SZUGUgvqxvPVWadfc7yIlIuCQ5HEPcwUVnClnB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
