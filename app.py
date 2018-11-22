import tweepy
import time
import ytAPI
from config import CONSUMER_KEY
from config import CONSUMER_SECRET
from config import ACCESS_KEY
from config import ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


file_name = 'last_seen_id.txt'

# TODO integrate youtube api 3 into the twitter bot response


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
# If you want to test, paste 1065123470370111488 in the last_seen_id.txt


def reply_to_tweets():
    print("Initializing Reply")
    last_seen_id = retrieve_last_seen_id(file_name)

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        # Stores the last seen id in the txt
        # store_last_seen_id(last_seen_id, file_name)
        print(mention.__dict__)

        if '!details' in mention.full_text.lower():
            try:
                # This nightmare right here gets the expanded_url from a tweet.
                # If it fails to find a link, it hits an exception and asks for a proper link
                urls = str(mention.entities.get(
                    "urls")).split(",")
                expanded_url = urls[1]
                expanded_url = expanded_url[18:len(expanded_url)-1]
                print(expanded_url)
                if 'youtube.com/watch?v=' in expanded_url:
                    # If you want an @mention to go out from the bot, add the following to the update_status:
                    # '@' + mention.user.screen_name
                    # api.update_status("Functionality is not yet working for this feature.", last_seen_id)
                    video_id = expanded_url.split("youtube.com/watch?v=",1)[1]
                    print("Youtube Video Detected. " + video_id)
                    get_video_object(video_id)
                else:
                    # api.update_status("Please include a youtube link to a specific video.")
                    print(expanded_url)
            except:
                print("No subject content found.")
                print(expanded_url)
                # api.update_status("Please include a youtube link to analyze.", last_seen_id)
        else:
            print('No Request Found')
            # api.update_status("Please include one of the requests in my profile.", last_seen_id)


reply_to_tweets()
# Every 15 seconds get all new mentions, and run reply_to_tweets()
# while True:
#     reply_to_tweets()
#     time.sleep(15)
