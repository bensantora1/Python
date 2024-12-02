import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write, read

# Task 1: Create a sine wave
sample_rate = 44100  # Hz
duration = 2  # seconds
frequency = 440  # Hz (A4)

# Time axis
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine wave
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Save the sine wave as a .wav file
output_file = "sine_wave.wav"
write(output_file, sample_rate, (sine_wave * 32767).astype(np.int16))

# Task 2: Read and save the sine wave plot as an image file
wav_sample_rate, wav_data = read(output_file)

# Save the waveform plot
plot_file = "sine_wave_plot.png"
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], sine_wave[:1000], label="Generated Sine Wave")
plt.title("Sine Waveform (First 1000 Samples)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.savefig(plot_file)  # Save the plot as a PNG file
plt.close()  # Close the plot to free resources

print(f"Sine wave .wav file saved as: {output_file}")
print(f"Sine wave plot saved as: {plot_file}")
