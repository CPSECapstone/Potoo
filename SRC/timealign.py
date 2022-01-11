from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip 

AUDIO_CLIP_PATH = None
VIDEO_CLIP_PATH = None

audio = CompositeAudioClip([AudioFileClip(AUDIO_CLIP_PATH)])
video = VideoFileClip(VIDEO_CLIP_PATH)

video.set_audio(audio)
video.write_videofile("merged.mp4")


