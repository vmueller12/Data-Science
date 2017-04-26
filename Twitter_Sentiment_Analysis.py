import tweepy
from textblob import TextBlob


consumer_key = 'tweeter.com'
consumer_secret = 'tweeter.com'

access_token = 	'tweeter.com'
access_token_secret = 'tweeter.com'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Create Tweets
# Delete Tweets
# Find Twitter Users

# We will collect tweets with certain keyword

public_tweets = api.search('AKBA')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
