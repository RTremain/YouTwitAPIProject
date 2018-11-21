import tweepy
import time
from config import CONSUMER_KEY
from config import CONSUMER_SECRET
from config import ACCESS_KEY
from config import ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file_name = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print("Initializing Reply")
    last_seen_id = retrieve_last_seen_id(file_name)

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, file_name)

        if '!details' in mention.full_text.lower():
            try:
                # This nightmare right here gets the expanded_url from a tweet.
                # If it fails to find a youtube link, it hits an exception and asks for a proper link
                urls = str(mention.entities.get(
                    "urls")).split(",")
                expanded_url = urls[1]
                expanded_url = expanded_url[18:len(expanded_url)-1]
                api.update_status(
                    "Functionality is not yet working for this feature.", last_seen_id)
                # print(expanded_url)
            except:
                # print("No subject content found.")
                api.update_status(
                    "Please include a youtube link to analyze.", last_seen_id)
        else:
            #print('No Request Found')
            api.update_status(
                "Please include one of the requests in my profile.", last_seen_id)


reply_to_tweets()
# Every 15 seconds get all new mentions, and run reply_to_tweets()
# while True:
# reply_to_tweets()
# time.sleep(15)
