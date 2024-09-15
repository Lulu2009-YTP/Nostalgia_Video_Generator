import random
from moviepy.editor import *
import numpy as np
from effects import apply_random_effects
from utils import load_assets

# Load video, audio, and image assets
video_file, audio_files, image_files = load_assets()

# Load base video
video_clip = VideoFileClip(video_file)

# Apply random effects
video_clip = apply_random_effects(video_clip)

# Add random audio background
bg_audio = AudioFileClip(random.choice(audio_files))
video_with_audio = video_clip.set_audio(bg_audio)

# Export final video
video_with_audio.write_videofile("nostalgia_video_output.mp4", codec="libx264", audio_codec="aac")
