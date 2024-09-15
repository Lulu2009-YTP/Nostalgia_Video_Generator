from pydub import AudioSegment

def random_pitch_shift(audio_clip):
    shift = random.uniform(-5.0, 5.0)  # Random pitch shift in semitones
    return audio_clip.set_frame_rate(int(audio_clip.frame_rate * (2.0 ** (shift / 12.0))))
