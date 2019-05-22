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
            print('|'+ result['entries'][i]['title'] +'|[Watch]('+result['entries'][i]['webpage_url']+')|'+'-|')