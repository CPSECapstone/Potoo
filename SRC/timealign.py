
import sys
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip 

AUDIO_CLIP_PATH = sys.argv[1]
VIDEO_CLIP_PATH = sys.argv[2]
OUTPUT_FILENAME = sys.argv[3]

audio = CompositeAudioClip([AudioFileClip(AUDIO_CLIP_PATH)])
video = VideoFileClip(VIDEO_CLIP_PATH)

video.audio = audio
video.write_videofile(OUTPUT_FILENAME)


