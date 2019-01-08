import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob



consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


print("Searching for tweets")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Modi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)

	if (analysis.sentiment.polarity>0):
		print("positive ssentiments are",(analysis.sentiment))

	elif (analysis.sentiment.polarity<0):
		print("negatve sentiments are:",(analysis.sentiment) )

	else:
		print("neutral sentiments",(analysis.sentiment))



