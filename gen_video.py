#!/usr/bin/python
## Author: sumanth
## Date: November 22, 2017
# generates video from the images in sequence

import imageio

# install ffmpeg if not installed already
imageio.plugins.ffmpeg.download()

import glob
import os
from moviepy.editor import ImageSequenceClip
import argparse


def main(ip_dir, video):
    # generate the video, from the images in sequence
    vimages = [str(filename) for filename in sorted(glob.glob(os.path.join(ip_dir+'/*.jpg')))]
    clip = ImageSequenceClip(ip_dir, fps=25)
    clip.write_videofile(ip_dir+'/'+video+'.mp4', fps=25)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate video')
    parser.add_argument(
        '--ip_dir',
        type=str,
        default="",
        help='give the directory of the images'
    )
    parser.add_argument(
        '--video',
        type=str,
        default="yes",
        help='video name'
    )
    args = parser.parse_args()

main(args.ip_dir, args.video,)