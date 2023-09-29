def play_tone(x, y, radius):
    # Map x and y coordinates to frequencies
    base_frequency = 220.0  # Adjust as needed

    #BRADS COMMENT: Instead of basing the frequency on its x,y location
    #we will compute a frequency using our getNewNote(baseFreq,nSemitones)
    #function and we can use the two lists of semitones below, which will
    #always give us the notes of a major (the first list) or minor pentatonic
    #scale, which will always sound somewhat consonant

    semitoneListMajor = [0,2,4,7,9,12,16,19] #major pentatonic scale
    semitoneListMinor = [0,3,5,7,10,12,15,17] #minor pentatonic scale

    #We can get rid of all of this
    x_scale = 5.0  # Adjust to change the scale of the x-axis mapping
    y_scale = 2.0  # Adjust to change the scale of the y-axis mapping
    frequency = base_frequency + x * x_scale + y * y_scale
    #And replace it with:
    #frequency = getNewNote(base_frequency,
    # random.choice(semiToneListMajor or semiToneListMinor))

    # Calculate the duration based on circle radius

    #BRADS COMMENT: This is not the radius but the distance to the
    #center. Since we are specifying a radius for our circle
    #either explictly or through a random number generator
    #lets just change the function and pass in the radius
    #as an argument and delete the radius assignment below

    radius = math.sqrt(x ** 2 + y ** 2)

    #this will make the tone duration longer with a bigger radius
    duration = radius * 0.005  # Adjust the scale as needed, 0.005 is lowest you should go

    # Generate a sine wave with fade-in and fade-out
    sample_rate = 44100  # Sample rate in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    fade_duration = 0.05  # Adjust the fade-in/fade-out duration as needed
    fade_samples = int(fade_duration * sample_rate)

    # Create a fade-in and fade-out envelope
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)

    # Generate the sine wave
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Apply fade-in and fade-out
    wave[:fade_samples] *= fade_in
    wave[-fade_samples:] *= fade_out

    # Play the sine wave
    play_obj = sa.play_buffer((wave * 32767).astype(np.int16), 1, 2, sample_rate)
    play_obj.wait_done()