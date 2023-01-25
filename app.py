from pytube import YouTube
import os

with open('inputs.txt') as f:
    vid_list = f.readlines()


out_format = input('Please select <aud|vid>: ')

if out_format == 'aud':
    out_path = os.path.join('AUD')
    for vid in vid_list:
        yt = YouTube(vid)
        strms = yt.streams.filter(only_audio=True)
        strms[0].download(out_path)
        print(yt.title)
elif out_format == 'vid':
    out_path = os.path.join('VID')
    for vid in vid_list:
        yt = YouTube(vid)
        print(yt.streams)
        # strms = yt.streams.get_by_itag(137)
        # strms.download(out_path)
        # https://stackoverflow.com/questions/58184585/how-to-combine-audio-and-video-in-pytube
        print(yt.title)
else:
    print('something went wrong')
