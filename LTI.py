import matplotlib

matplotlib.use("TkAgg")  # Force GUI backend

import numpy as np
import matplotlib.pyplot as plt

# Constants
a1 = 3
a2 = -7

# Define signal domain
n = np.arange(-3, 3.1, 0.1)

# Input signals
x1 = n
x2 = np.sin(n)

# System output for individual inputs
y1 = x1**2
y2 = x2**2

# Linearity test
y3 = a1 * y1 + a2 * y2
x3 = a1 * x1 + a2 * x2
y4 = x3**2

# Plotting
plt.figure(figsize=(10, 6))

# Subplot 1: y3
plt.subplot(2, 1, 1)
plt.stem(n, y3)  # removed use_line_collection
plt.xlabel("n\nfig1(a)")
plt.ylabel("y3[n]")
plt.title("Linearity Check: y3[n] = a1*y1[n] + a2*y2[n]")
plt.grid(True)

# Subplot 2: y4
plt.subplot(2, 1, 2)
plt.stem(n, y4)  # removed use_line_collection
plt.xlabel("n\nfig1(b)")
plt.ylabel("y4[n]")
plt.title("Linearity Check: y4[n] = (a1*x1[n] + a2*x2[n])^2")
plt.grid(True)

# Show plots
plt.tight_layout()
plt.show()
