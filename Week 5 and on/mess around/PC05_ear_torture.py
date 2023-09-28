import turtle
import random
import simpleaudio as sa
import numpy as np
import time

def getNewNote(baseFreq,nSemitones):
	newFreq = float(baseFreq) * (float(nSemitones)/12)**2
	return newFreq

def generate_tone(freq, duration, fade_duration=0.1):
    """Generate a tone for a given frequency and duration with fade-in and fade-out."""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t)

    fade_samples = int(fade_duration * sample_rate)
    fade_in = (1 - np.cos(np.pi * np.linspace(0, 1, fade_samples))) * 0.5
    fade_out = (1 + np.cos(np.pi * np.linspace(0, 1, fade_samples))) * 0.5

    envelope = np.ones_like(t)
    envelope[:fade_samples] = fade_in
    envelope[-fade_samples:] = fade_out

    audio = tone * envelope
    audio = audio * (2**15 - 1) / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    return audio

def play_tone_based_on_coords(x, y):
    """Play a tone based on x,y coordinates."""
    
    # Determine the base frequency for each quadrant
    if x > 0 and y > 0:  # Quadrant I
        base_freq = 440
    elif x < 0 and y > 0:  # Quadrant II
        base_freq = 480
    elif x < 0 and y < 0:  # Quadrant III
        base_freq = 520
    else:  # Quadrant IV
        base_freq = 560

    freq = getNewNote(base_freq,(random.randint(1,5)*8))
    tone = generate_tone(freq, 1)
    sa.play_buffer(tone, 1, 2, 44100)

def draw_circle(_):
    """Draw a circle at a random position and play a tone based on its coordinates."""
    x = random.randint(int((-300+(_*5))), int((-250+(_*5))))
    y = random.randint(int((200-(_*5))), int((250-(_*5))))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)
    play_tone_based_on_coords(x, y)

# Setup the turtle environment
turtle.speed(0)
turtle.bgcolor("white")

# Draw 10 circles at random positions
for _ in range(100):
    draw_circle(_)
    time.sleep(0.25)
    draw_circle(_)
    time.sleep(0.5)
    

turtle.done()

