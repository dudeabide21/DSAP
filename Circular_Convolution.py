import numpy as np
import matplotlib.pyplot as plt

# --- Input Sequences ---
x = np.array([1, 2, 3, 4])
h = np.array([1, 0, 1, 0])

# --- Padding to Equal Length ---
N = max(len(x), len(h))
x = np.pad(x, (0, N - len(x)))
h = np.pad(h, (0, N - len(h)))


# --- Manual Circular Convolution ---
def circular_convolution_manual(x, h):
    N = len(x)
    y = np.zeros(N)
    for n in range(N):
        for k in range(N):
            y[n] += x[k] * h[(n - k) % N]
    return y


y_manual = circular_convolution_manual(x, h)

# --- FFT-based Circular Convolution ---
X = np.fft.fft(x)
H = np.fft.fft(h)
Y = X * H
y_fft = np.fft.ifft(Y).real  # Remove small imaginary errors

# --- Plotting ---
fig, axs = plt.subplots(4, 1, figsize=(10, 10))

# 1. Input signal x[n]
axs[0].stem(range(N), x, basefmt=" ")
axs[0].set_title("Input Signal x[n]")
axs[0].set_xlabel("n")
axs[0].set_ylabel("x[n]")
axs[0].grid(True)

# 2. Impulse response h[n]
axs[1].stem(range(N), h, basefmt=" ", linefmt="orange", markerfmt="ro")
axs[1].set_title("Impulse Response h[n]")
axs[1].set_xlabel("n")
axs[1].set_ylabel("h[n]")
axs[1].grid(True)

# 3. Circular Convolution (Manual)
axs[2].stem(range(N), y_manual, basefmt=" ", linefmt="green", markerfmt="go")
axs[2].set_title("Circular Convolution (Manual)")
axs[2].set_xlabel("n")
axs[2].set_ylabel("y[n]")
axs[2].grid(True)

# 4. Circular Convolution (FFT-based)
axs[3].stem(range(N), y_fft, basefmt=" ", linefmt="red", markerfmt="mo")
axs[3].set_title("Circular Convolution (FFT-based)")
axs[3].set_xlabel("n")
axs[3].set_ylabel("y[n]")
axs[3].grid(True)

plt.tight_layout()
plt.show()
