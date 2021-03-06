# Code by Sumeet Khillare

import requests
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='YTAPI')
    parser.add_argument("-a", "--apikey", dest="apikey", help="Api Key")
    parser.add_argument("-c", "--channelid", dest="channelid", help="Channel Id")
    args = parser.parse_args()
    if not args.apikey:
        parser.error("[-] Please specify Api Key")
    elif not args.channelid:
        parser.error("[-] Please specify Channel Id")
    return args


options=get_arguments()
apikey=options.apikey
channelid=options.channelid

API_KEY = apikey
ChannelID = channelid
url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=' + ChannelID + '&maxResults=50&type=video&key=' + API_KEY
response = requests.get(url)
videos = response.json()
videoMetadata = []

for video in videos['items']:
    if video['id']['kind'] == 'youtube#video':
        videoMetadata.append(video['id']['videoId'])
for metadata in videoMetadata:
    print("Link: "+"https://www.youtube.com/watch?v=" + metadata)
    SpecificVideoID = metadata
    SpecificVideoUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=' + SpecificVideoID + '&key=' + API_KEY
    response = requests.get(SpecificVideoUrl)
    videos = response.json()
    videoMetadata = []
    for video in videos['items']:
        if video['kind'] == 'youtube#video':
            print("Name: " + video['snippet']['title'])
            print("Upload date:        " + video['snippet']['publishedAt'])
            print("Number of views:    " + video['statistics']['viewCount'])
            print("Number of likes:    " + video['statistics']['likeCount'])
            print("Number of dislikes: " + video['statistics']['dislikeCount'])
            print("Number of favorites:" + video['statistics']['favoriteCount'])
            print("Number of comments: " + video['statistics']['commentCount'])
            print("\n")
