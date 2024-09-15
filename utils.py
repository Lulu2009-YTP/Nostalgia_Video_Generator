import os

def load_assets():
    video_file = 'assets/sample_video.mp4'  # Replace with your own video
    audio_files = [os.path.join('assets', f) for f in os.listdir('assets') if f.endswith('.mp3')]
    image_files = [os.path.join('assets', f) for f in os.listdir('assets') if f.endswith(('.png', '.jpg', '.gif'))]
    
    return video_file, audio_files, image_files
