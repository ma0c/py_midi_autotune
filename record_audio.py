import numpy as np
import wave
import sounddevice as sd


def record_audio():
    print(sd.query_devices())

    selected_device = int(input("Select the device: "))

    sd.default.device = selected_device

    sample_rate = 16000
    channels = 1

    recording = sd.rec(sample_rate*2, samplerate=sample_rate, channels=channels)
    sd.wait()

    print(recording.shape)

    # sd.play(recording, sample_rate)
    AH_440 = wave.open("AH_440.wav", "wb")
    AH_440.setnchannels(channels)
    AH_440.setsampwidth(4)
    AH_440.setframerate(sample_rate)
    AH_440.writeframes(recording)
    AH_440.close()


if __name__ == '__main__':
    record_audio()