import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Number of samples
n = np.arange(20)

# FIR example: y[n] = x[n] + 0.7x[n-1]
# Coefficients: b = [1, 0.7] (FIR), a = [1] (no feedback)
b_fir = [1, 0.7]
a_fir = [1]

# IIR example: y[n] = x[n] + 0.7y[n-1]
# Coefficients: b = [1], a = [1, -0.7]
b_iir = [1]
a_iir = [1, -0.7]

# Compute impulse response
impulse = np.zeros(20)
impulse[0] = 1  # δ[n]
h_fir = signal.lfilter(b_fir, a_fir, impulse)
h_iir = signal.lfilter(b_iir, a_iir, impulse)

# Plot
plt.stem(n, h_fir, linefmt="b-", markerfmt="bo", basefmt="k", label="FIR")
plt.stem(n, h_iir, linefmt="r-", markerfmt="ro", basefmt="k", label="IIR")
plt.legend()
plt.xlabel("n")
plt.ylabel("h[n]")
plt.title("Impulse Response: FIR vs IIR")
plt.grid(True)
plt.show()
