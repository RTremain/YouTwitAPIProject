import tweepy
import time
import json
from ytAPI import get_video_tags
from ytAPI import get_video_channel
from ytAPI import get_video_upload_time
from ytAPI import get_video_upload_date
from ytAPI import get_video_dislikes
from ytAPI import get_video_title
from ytAPI import get_video_views
from ytAPI import get_video_likes
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
        # DO NOT FORGET TO ADD THIS BACK IN
        store_last_seen_id(last_seen_id, file_name)
        # print(mention)

        if '!details' in mention.full_text.lower():
            try:
                # If it fails to find a link, it hits an exception and asks for a proper link
                for item in mention.entities['urls']:
                    expanded_url = item['expanded_url']

                if 'youtube.com/watch?v=' in expanded_url:
                    # If you want an @mention to go out from the bot, add the following to the update_status:
                    # '@' + mention.user.screen_name
                    video_id = expanded_url.split("youtube.com/watch?v=", 1)[1]

                    api.update_status('@' + mention.user.screen_name + " " +
                                      'Title: ' + get_video_title(video_id) +
                                      '\nChannel: ' + get_video_channel(video_id) +
                                      '\nViews: ' + get_video_views(video_id) +
                                      '\nLikes: ' + get_video_likes(video_id) +
                                      '\nDislikes: ' + get_video_dislikes(video_id) +
                                      '\nPublish Date: ' + get_video_upload_date(video_id) +
                                      '\nPublish Time: ' + get_video_upload_time(video_id), last_seen_id)
                else:
                    api.update_status('@' + mention.user.screen_name + " " +
                                      "Please include a youtube link to a specific video.", last_seen_id)

            except Exception as e:
                print(e)
                api.update_status('@' + mention.user.screen_name + " " +
                                  "An error has occurred.", last_seen_id)

        if'!tags' in mention.full_text.lower():
            try:
                for item in mention.entities['urls']:
                    expanded_url = item['expanded_url']

                    if 'youtube.com/watch?v=' in expanded_url:
                        # If you want an @mention to go out from the bot, add the following to the update_status:
                        video_id = expanded_url.split(
                            "youtube.com/watch?v=", 1)[1]
                        # print(video_id)
                        api.update_status('@' + mention.user.screen_name + " " +
                                          'Tags: ' + get_video_tags(video_id), last_seen_id)
                    else:
                        print('Error in getting tags')
                        api.update_status('@' + mention.user.screen_name + " " +
                                          "Please include a youtube link to a specific video.", last_seen_id)
            except Exception as e:
                print(e)
                api.update_status('@' + mention.user.screen_name + " " +
                                  "No tags found.", last_seen_id)
        else:
            api.update_status('@' + mention.user.screen_name + " " +
                              "Please include one of the requests in my profile.", last_seen_id)


# reply_to_tweets()
# Every 15 seconds get all new mentions, and run reply_to_tweets()
while True:
    reply_to_tweets()
    time.sleep(15)
