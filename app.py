import tweepy
from textblob import TextBlob

consumer_key = 'LYKDxCiX6qkPz5Izsrlpv4eQ3'
consumer_secret = 'qtXchtEvBds62zkSD3RZsNwKdjcCwqnlyENWeIFyghzbnSMQse'

access_token = 	'749646152816099328-ik1RjWpx2912StzTWilnDnqCJ1sfNRT'
access_token_secret = 'ih5EXzOGLMelw0eaamuIiywTSLWMFg42XpaEZyt1Oqikz'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

term = input("What do you want to analyse ? ")

public_tweets = api.search(term)

#for tweet in public_tweets:
#	print(tweet.text)
analysis = TextBlob(term)
print(analysis.sentiment)
