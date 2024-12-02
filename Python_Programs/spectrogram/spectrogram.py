import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# Read the audio file
sample_rate, audio_data = read("sine_wave.wav")

# Normalize the audio data
audio_data = audio_data / 32767.0

# Plot the spectrogram
plt.figure(figsize=(10, 6))
plt.specgram(audio_data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='viridis')
plt.title("Audio Spectrogram")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.colorbar(label="Intensity [dB]")
plt.savefig("spectrogram.png")
plt.close()

print("Spectrogram saved as: spectrogram.png")
