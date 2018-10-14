import tweepy
from tweepy import OAuthHandler
 
from takeshi_twitter_tokens import *
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# for status in tweepy.Cursor(api.home_timeline).items(100):
#     print(">>>" + status.text)


# for status in tweepy.Cursor(api.search, q="motorola").items():
	# print(">>>" + status.text)

for status in tweepy.Cursor(api.user_timeline, screen_name="tradersclubbr", since="2018-10-13").items(1):
	print(status)

