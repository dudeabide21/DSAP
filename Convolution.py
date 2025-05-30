import numpy as np
import matplotlib.pyplot as plt

# Define the range for n
n = np.arange(-5, 10)

# Define x[n] = δ[n] + 2δ[n-1] - δ[n-3]
x = np.zeros_like(n)
x[n == 0] = 1
x[n == 1] = 2
x[n == 3] = -1

# Define h[n] = 2δ[n+1] + 2δ[n-1]
h = np.zeros_like(n)
h[n == -1] = 2
h[n == 1] = 2

# Perform discrete convolution
y = np.convolve(x, h)

# Define output index range (starts at n_start_x + n_start_h)
n_y = np.arange(n[0] + n[0], n[0] + n[0] + len(y))

# Plot x[n], h[n], and y[n]
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt=" ")
plt.title("x[n] = δ[n] + 2δ[n-1] - δ[n-3]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h, basefmt=" ")
plt.title("h[n] = 2δ[n+1] + 2δ[n-1]")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n_y, y, basefmt=" ")
plt.title("y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)

plt.tight_layout()
plt.show()
