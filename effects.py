from moviepy.editor import *
import random

def apply_random_effects(clip):
    # Randomly choose from available effects
    effects = [
        lambda c: c.fx(vfx.invert_colors),
        lambda c: c.fx(vfx.mirror_x),
        lambda c: c.fx(vfx.painting, saturation=1.6),
        lambda c: c.fx(vfx.time_mirror),
        lambda c: c.fx(vfx.loop, n=2),
        lambda c: c.rotate(random.randint(0, 360)),
        lambda c: c.resize(random.uniform(0.5, 1.5)),
        lambda c: c.margin(20, color=random.choice(["blue", "green", "red"])),
        lambda c: c.set_fps(random.randint(15, 30))
    ]

    random_effect = random.choice(effects)
    return random_effect(clip)

# Example audio effects
def apply_random_audio_effects(audio_clip):
    audio_effects = [
        lambda a: a.volumex(random.uniform(0.5, 1.5)),  # Random volume
        lambda a: a.fx(afx.audio_fadein, random.uniform(1, 5)),
        lambda a: a.fx(afx.audio_fadeout, random.uniform(1, 5)),
        lambda a: a.fx(afx.audio_speedx, random.uniform(0.5, 1.5)),
    ]
    
    random_audio_effect = random.choice(audio_effects)
    return random_audio_effect(audio_clip)
