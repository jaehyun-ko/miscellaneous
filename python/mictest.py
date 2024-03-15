import pyaudio
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
p = pyaudio.PyAudio()

info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'),
              " - Channels", p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels'),
              " - Sample Rate", p.get_device_info_by_host_api_device_index(0, i).get('defaultSampleRate'))

# Set the device ID
device_id = 1

FORMAT = pyaudio.paInt16  # Set the format
RATE = 44100  # Set the rate

CHUNK = 1024  # Set the chunk size
RECORD_SECONDS = 5  # Set the number of seconds to record

# Get the number of channels for the device
channels = p.get_device_info_by_host_api_device_index(0, device_id).get('maxInputChannels')

# Open the stream with the specified device
streams = [p.open(format=FORMAT,
                  channels=channel+1,
                  rate=RATE,
                  input=True,
                  input_device_index=device_id,
                  frames_per_buffer=CHUNK) for channel in range(channels)]

frames = [[] for _ in range(channels)]

# Record for RECORD_SECONDS
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    for i in range(channels):
        data = streams[i].read(CHUNK)
        frames[i].append(data)

print("Finished recording")

# Stop the stream
for stream in streams:
    stream.stop_stream()
    stream.close()

# Terminate the PyAudio object
p.terminate()

for channel in range(channels):
    # Convert frames to an array for analysis
    frames_array = np.frombuffer(b''.join(frames[channel]), dtype=np.int16)

    # Create a spectrogram
    frequencies, times, spectrogram = signal.spectrogram(frames_array, RATE)

    # Plot the spectrogram
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title(f'Channel {channel+1} Spectrogram')

    # Plot the waveform
    plt.subplot(2, 1, 2)
    plt.plot(frames_array)
    plt.ylabel('Amplitude')
    plt.xlabel('Time [sec]')
    plt.title(f'Channel {channel+1} Waveform')
    plt.tight_layout()
    plt.show()

