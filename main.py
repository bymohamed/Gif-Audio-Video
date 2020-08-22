from moviepy.editor import *
import sys

audioName = sys.argv[1]
gifName = sys.argv[2]

print(audioName)

audioclip = AudioFileClip(audioName)

audioDuration = audioclip.duration

gif = VideoFileClip(gifName)

gif = gif.loop( duration=audioDuration)

gif_with_audio = gif.set_audio(audioclip)

gif_with_audio.write_videofile('output.mp4',fps=30 , threads=1)

#finalVideo = CompositeVideoClip([audioclip, gif], size=(1920,1080))

#finalVideo.write_videofile('output.mp4', fps=30, threads=1)

