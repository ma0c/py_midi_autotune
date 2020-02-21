import numpy as np
import sounddevice as sd

sd.query_devices()

sd.default.device = 6

sample_rate = 16000
channels = 1

recording = sd.rec(sample_rate*3, samplerate=sample_rate, channels=1)
sd.wait()

print(np.max(recording))
print(recording)

sd.play(recording, sample_rate)