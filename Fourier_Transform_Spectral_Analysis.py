import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
Fs = 1000  # Sampling frequency (Hz)
T = 1 / Fs  # Sampling interval
N = 1024  # Number of samples
t = np.arange(N) * T  # Time vector

# Signal: sum of two cosines
f1 = 50  # Hz
f2 = 120  # Hz
x = 3 * np.cos(2 * np.pi * f1 * t) + 2 * np.cos(2 * np.pi * f2 * t)

# Compute FFT
X = np.fft.fft(x)
X_mag = np.abs(X) / N  # Magnitude
X_phase = np.angle(X)  # Phase
f = np.fft.fftfreq(N, T)

# Only plot positive frequencies
half_N = N // 2
plt.figure(figsize=(14, 6))

# Magnitude Spectrum
plt.subplot(1, 2, 1)
plt.plot(f[:half_N], 2 * X_mag[:half_N])
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|X(f)|")
plt.grid()

# Phase Spectrum
plt.subplot(1, 2, 2)
plt.plot(f[:half_N], X_phase[:half_N])
plt.title("Phase Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.grid()

plt.tight_layout()
plt.show()
