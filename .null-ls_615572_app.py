from pytube import YouTube
import os

with open('inputs.txt') as f:
    vid_list = f.readlines()


out_format = input('Please select <aud|vid>: ')

if out_format == 'aud':
    out_path = os.path.join('AUD')
    for vid in vid_list:
        yt = YouTube(vid)
        strms = yt.streams.filter(only_audio=True).all()
        strms[0].download(out_path)
elif out_format == 'vid':
    out_path = os.path.join('VID')
    for vid in vid_list:
        yt = YouTube(vid)
        strms = yt.streams.get_highest_resolution()
        strms.download(out_path)
else:
    print('something went wrong')
