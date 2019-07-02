import youtube_dl
import os

# input=' https://www.youtube.com/playlist?list=PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3'
url=' '+input()
start = 1
print("Enter number of videos:")
end = int(input())

# For fetching the title of the video in playlist
cmd_code1='py -m youtube_dl -e --playlist-start ' +str(start)+' --playlist-end '+str(end)+url
title = os.popen(cmd_code1).read().splitlines()
#print(title[0])

# For fetching the id of that particular video in playlist
cmd_code2='py -m youtube_dl --get-id --playlist-start ' +str(start)+' --playlist-end '+str(end)+url
video_id = os.popen(cmd_code2).read().splitlines()

print('| Topic        |      Video     |  Presentation |')
print('| ------------- |:-------------:| -----:|')

for i in range(0, len(title)):
    print('|'+ title[i] +'|[Watch Here](https://www.youtube.com/watch?v='+video_id[i]+')|'+'-|')
