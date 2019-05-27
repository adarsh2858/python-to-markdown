import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
video = ""

with ydl:
    yt_url=input()
    result = ydl.extract_info(yt_url, download=False) #We just want to extract the info

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries']

        print('| Topic        |      Video     |  Presentation |')
        print('| ------------- |:-------------:| -----:|')

        #loops entries to grab each video_url
        for i, item in enumerate(video):
            video = result['entries'][i]
            # fetch the url and title of video
            print('|'+ result['entries'][i]['title'] +'|[Watch Here]('+result['entries'][i]['webpage_url']+')|'+'-|')
            
#Alternate method
import youtube_dl
import os

start = 101;
end = 154;

# For fetching the title of the video in playlist
cmd_code1='py -m youtube_dl -e --playlist-start ' +str(start)+' --playlist-end '+str(end)+' https://www.youtube.com/playlist?list=PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3'
title = os.popen(cmd_code1).read().splitlines()
#print(title[0])

# For fetching the id of that particular video in playlist
cmd_code2='py -m youtube_dl --get-id --playlist-start ' +str(start)+' --playlist-end '+str(end)+' https://www.youtube.com/playlist?list=PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3'
video_id = os.popen(cmd_code2).read().splitlines()

print('| Topic        |      Video     |  Presentation |')
print('| ------------- |:-------------:| -----:|')

for i in range(0, len(title)):
    print('|'+ title[i] +'|[Watch Here](https://www.youtube.com/watch?v='+video_id[i]+')|'+'-|')
