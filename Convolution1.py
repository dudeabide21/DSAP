import numpy as np
import matplotlib.pyplot as plt

# Define range of n
n = np.arange(-5, 15)

# Define x[n] = (1/3)^n * u[n]
x = (1 / 3) ** n * (n >= 0)

# Define h[n] = u[n+2] - u[n-2] -> 1 for -2 <= n <= 1
h = np.logical_and(n >= -2, n <= 1).astype(float)

# Convolve
y = np.convolve(x, h)

# New range for y[n]
n_y = np.arange(n[0] + n[0], n[-1] + n[-1] + 1)

# Plot
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt=" ")
plt.title(r"$x[n] = \left(\frac{1}{3}\right)^n \cdot u[n]$")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h, basefmt=" ")
plt.title(r"$h[n] = u[n+2] - u[n-2]$")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n_y, y, basefmt=" ")
plt.title(r"$y[n] = x[n] * h[n]$")
plt.grid(True)

plt.tight_layout()
plt.show()
