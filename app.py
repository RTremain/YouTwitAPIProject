import tweepy
from config import CONSUMER_KEY
from config import CONSUMER_SECRET
from config import ACCESS_KEY
from config import ACCESS_SECRET

print('This is my Twitter Bot')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

print(mentions[0].__dict__.keys())
