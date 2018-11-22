

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

test_video_id = 'sQYJJFLxaaw'
# A video that contains special characters to test encoding
test_video_id_containing_special_characters = 'Vzl93kp37oM'


def get_video_object(video_id)
    video_api_url = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id="
    video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
    print(video_api_request)
    response = urllib.request.urlopen(video_api_request)

    data = json.loads(response.read())
    data = str(data).encode("utf-8")

    # print(str(data).encode("utf-8"))
    print(data)
    f = open("channelobject.txt", "w+")
    f.write(str(data))
    f.close()

# video_id = test_video_id
# video_api_url = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id="
# video_api_request = video_api_url + video_id + "&key=" + GOOGLE_API_KEY
# print(video_api_request)
# response = urllib.request.urlopen(video_api_request)

# data = json.loads(response.read())
# data = str(data).encode("utf-8")

# print(str(data).encode("utf-8"))
# print(data)
# f = open("channelobject.txt", "w+")
# f.write(str(data))
# f.close()
