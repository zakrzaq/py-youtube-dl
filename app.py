# SOURCES:
# https://www.youtube.com/watch?v=CG12hJ3s6KI&list=WL&index=5
# https://stackoverflow.com/questions/58184585/how-to-combine-audio-and-video-in-pytube

# Author: Jake Zakrzewski

from pytube import YouTube
import os
import random
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description = "Download youtube video / audio by url")
    parser.add_argument('-u', help='list of urls', nargs='+', default = [])
    parser.set_defaults(func = app)
    args = parser.parse_args()
    args.func(args)


def app(args):
    if args:
        vid_list = args.u
    else:
        with open('inputs.txt') as f:
            vid_list = f.readlines()

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
            out_path = os.path.join('AUD')
            for vid in vid_list:
                yt = YouTube(vid)
                strms = yt.streams.filter(only_audio=True)
                typewrite('Download is starting ...\n')
                strms[0].download(out_path)
                completed(strms[0], yt)
        elif out_format == 'vid':
            out_path = os.path.join('VID')
            for vid in vid_list:
                yt = YouTube(vid)
                strms = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                typewrite('Download is starting ...\n')
                strms.download(out_path)
                completed(strms, yt)
    except:
        typewrite('Something went wrong')

if __name__ == "__main__":
    main()
