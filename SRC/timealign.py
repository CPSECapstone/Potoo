
import sys
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, ColorClip, concatenate_videoclips


def main():
      
   AUDIO_CLIP_PATH = sys.argv[1]
   VIDEO_CLIP_PATH = sys.argv[2]
   OUTPUT_FILENAME = sys.argv[3]

   audio = CompositeAudioClip([AudioFileClip(AUDIO_CLIP_PATH)])
   video = VideoFileClip(VIDEO_CLIP_PATH)

   filler = ColorClip(size=(460, 380), color=[0,0,0], duration=1)
   final_clip = concatenate_videoclips([video, filler])

   final_clip.audio = audio
   final_clip.write_videofile(OUTPUT_FILENAME)

main()