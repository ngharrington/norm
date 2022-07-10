import time
from multiprocessing import Process
import keyboard

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play

# PREPARING THE AUDIO DATA

# Audio file, .wav file
wavFile = "sample-audio.wav"

# Retrieve the data from the wav file
data, samplerate = sf.read(wavFile)

n = len(data)  # the length of the arrays contained in data
Fs = samplerate  # the sample rate

# Working with stereo audio, there are two channels in the audio data.
# Let's retrieve each channel seperately:
ch1 = np.array([data[i][0] for i in range(n)])  # channel 1
ch2 = np.array([data[i][1] for i in range(n)])  # channel 2

# x-axis and y-axis to plot the audio data
time_axis = np.linspace(0, n / Fs, n, endpoint=False)
sound_axis = ch1

# plt.plot(time_axis, sound_axis)
# plt.show()

def playing_audio():
    song = AudioSegment.from_wav(wavFile)
    play(song)

def write_time():
    print(time.now())

def register_end_of_joke():
    keyboard.on_press_key("space", write_time)



if __name__ == "__main__":
    # p1 = Process(target=playing_audio, args=())
    # p1.start()
    # p2 = Process(target=register_end_of_joke, args=())
    # p2.start()
    # p1.join()
    # p2.join()
    keyboard.on_press_key("t", lambda x: print(5))

