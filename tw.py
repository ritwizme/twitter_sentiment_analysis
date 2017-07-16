import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob



consumer_key = '5bYzFEwwmu4v0IB5YoQJJ39d8'
consumer_secret = 'kVHTrEzdZDhBy6h91YuoGUMCszaL1Ah0zwmT7R7shej2P7DWIc'

access_token = '843373452945903616-lUDFJIeSPSPbmq4FGwTOKpM7KoYYdBp'
access_token_secret = 'pR9g0wXM2M0GyIDA2JWaqtiCp937cvbiy5MXrxMsEWVpa'


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



