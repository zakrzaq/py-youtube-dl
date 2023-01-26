# SOURCES:
# https://www.youtube.com/watch?v=CG12hJ3s6KI&list=WL&index=5
# https://stackoverflow.com/questions/58184585/how-to-combine-audio-and-video-in-pytube

# Author: Jake Zakrzewski

from pytube import YouTube
import os
import random
import time
import argparse

home = os.path.expanduser('~')
vid_out = os.path.join(home, 'Videos', 'youtube-dl-video')
aud_out = os.path.join(home, 'Videos', 'youtube-dl-audio')
input_file = os.path.join(home, 'Documents', 'youtube-dl-inputs.txt')

if not os.path.exists(vid_out):
    os.mkdir(vid_out)
if not os.path.exists(aud_out):
    os.mkdir(aud_out)


def main():
    parser = argparse.ArgumentParser(description = "Download youtube video / audio by url")
    parser.add_argument('-u', '--urls', help='list of urls', nargs='+', default = [])
    parser.add_argument('-l', '--local' help='txt file at ~/Documents/youtube-dl-inputs.txt')
    parser.set_defaults(func = app)
    args = parser.parse_args()
    args.func(args)


def app(args):
    if args.ursl:
        vid_list = args.u
        print(vid_list)
    elif args.local:
        with open(input_file) as f:
            vid_list =f.readlines()
        print(vid_list)
        

    def typewrite(txt: str, n1: float = 0.05, n2: float = 0.01):

        for char in txt:
            r = random.uniform(n1, n2)
            time.sleep(r)
            print(char, end='', flush=True)


    def completed(stream, yt):
        title = f"Title: {str(yt.title)}\n"
        length = f"Length: {str(yt.length)} seconds\n"
        size = f"File size: {str(stream.filesize_mb)} Mb\n"

        output = [title, length, size]

        for item in output:
            typewrite(item)



    out_format = input('Please select <aud|vid>: ')

    try:
        if out_format == 'aud':
            for vid in vid_list:
                yt = YouTube(vid)
                strms = yt.streams.filter(only_audio=True)
                typewrite('Download is starting ...\n')
                strms[0].download(aud_out)
                completed(strms[0], yt)
        elif out_format == 'vid':
            for vid in vid_list:
                yt = YouTube(vid)
                strms = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                typewrite('Download is starting ...\n')
                strms.download(vid_out)
                completed(strms, yt)
    except:
        typewrite('Something went wrong')

if __name__ == "__main__":
    main()
