

from config import GOOGLE_API_KEY
import json
import urllib.request
# encoding: utf-8
test_video_id = 'sQYJJFLxaaw'
# A video that contains special characters to test encoding
test_video_id_containing_special_characters = 'Vzl93kp37oM'
video_id = test_video_id
api_url = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id="

api_request = api_url + video_id + "&key=" + GOOGLE_API_KEY
print(api_request)
response = urllib.request.urlopen(api_request)

data = json.loads(response.read())
data = str(data).encode("utf-8")

# print(str(data).encode("utf-8"))
print(data)
f = open("channelobject.txt", "w+")
f.write(str(data))
f.close()
