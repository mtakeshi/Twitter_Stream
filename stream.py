
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json

from takeshi_twitter_tokens import *
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

 
class MyListener(StreamListener):
 
    def on_data(self, data):
        tweet = json.loads(data)
        print(">>>[" + tweet['user']['screen_name'] + " : " + tweet['text'].replace('\n','') + "]<<< ")
        return True
 
    def on_error(self, status):
        print(status)
        return True

 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['motorola'])
# twitter_stream.filter(follow=['60810202'])


# http://gettwitterid.com/?user_name=takeshi_marcos&submit=GET+USER+ID
# tradersclubbr - 767763810409181188
# takeshi_marcos - 60810202
