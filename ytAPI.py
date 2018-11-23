

from config import GOOGLE_API_KEY
import json
import urllib.request
# encoding: utf-8
# https://www.googleapis.com/youtube/v3/channels?part=id,+snippet&id=CHANNEL_ID&key=API_KEY
# Following is a search function I don't completely understand
# channelid can be changed to videoid, although I don't understand why it retrieves the channels or videos it does.
# Retrieved information seems to have nothing to do with the videoid or channelid provided
# https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=CHANNEL_ID&key=API_KEY
#
# https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id=VIDEO_ID&key=API_KEY

test_video_id = 's0xXx8oR7JY'
# A video that contains special characters to test encoding
test_video_id_containing_special_characters = 'Vzl93kp37oM'
channel_api_url = "https://www.googleapis.com/youtube/v3/channels?part=id,+snippet&id="
video_api_url = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id="
video_stats_api_url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&key="


def get_video_title(video_id):
    video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        snippet = item['snippet']['title']
        return snippet


def get_video_views(video_id):
    video_api_request = video_stats_api_url + GOOGLE_API_KEY + "&id=" + video_id
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        views = item['statistics']['viewCount']

        return views


def get_video_likes(video_id):
    video_api_request = video_stats_api_url + GOOGLE_API_KEY + "&id=" + video_id
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        likes = item['statistics']['likeCount']
        return likes


def get_video_dislikes(video_id):
    video_api_request = video_stats_api_url + GOOGLE_API_KEY + "&id=" + video_id
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        dislikes = item['statistics']['dislikeCount']
        return dislikes


def get_video_upload_date(video_id):
    video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        publishedAt = item['snippet']['publishedAt']
        publishedAt = publishedAt.split('T')
        return publishedAt[0]


def get_video_upload_time(video_id):
    video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        publishedAt = item['snippet']['publishedAt']
        publishedAt = publishedAt.split('T')
        return publishedAt[1][:-5]


def get_video_channel(video_id):
    video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())

    for item in data['items']:
        channelTitle = item['snippet']['channelTitle']
        return channelTitle


def get_video_tags(video_id):
    video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
    response = urllib.request.urlopen(video_api_request)
    data = json.loads(response.read())
    tweet_length = 15
    tag_tweet = ''
    tag_index = 0
    for item in data['items']:
        tags = item['snippet']['tags']
        # While loop condition doesn't work so I put an if statement inside
        while tweet_length < 100:
            for tag in tags:
                tweet_length = tweet_length + len(tag)
                tag_index += 1
                tag_tweet += tag + ", "

                if tweet_length >= 100:
                    break

            return tag_tweet
