import youtube_dl
import os

# input=' https://www.youtube.com/playlist?list=PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3'
print("Enter the url:")
url=' '+input()
print("Enter starting point of videos:")
start = int(input())
print("Enter number of videos:")
end = int(input())

# For fetching the title of the video in playlist
cmd_code1='python3 -m youtube_dl --no-check-certificate -e --playlist-start ' +str(start)+' --playlist-end '+str(end)+url
print("executed code to fetch title as " + cmd_code1)
title = os.popen(cmd_code1).read().splitlines()
#print(title[0])

# For fetching the id of that particular video in playlist
cmd_code2='python3 -m youtube_dl --no-check-certificate --get-id --playlist-start ' +str(start)+' --playlist-end '+str(end)+url
video_id = os.popen(cmd_code2).read().splitlines()

print('| Topic        |      Video     |  Presentation |')
print('| ------------- |:-------------:| -----:|')

for i in range(0, len(title)):
    print('|'+ title[i] +'|[Watch Here](https://www.youtube.com/watch?v='+video_id[i]+')|'+'-|')
