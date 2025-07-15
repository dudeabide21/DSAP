import matplotlib

matplotlib.use("TkAgg")  # Force GUI backend
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y_line_sin = np.sin(x)
y_line_cos = np.cos(x)
y_scatter_cos = np.cos(x)
y_scatter_sin = np.sin(x)

fig, axs = plt.subplots(4, 1, figsize=(4, 6))

axs[0].plot(x, y_line_sin, color="blue", label="Sine Wave")
axs[0].set_title("Line Plot - Sine Wave")
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x, y_line_cos, color="blue", label="Cosine")
axs[1].set_title("Line Plot - Cosine wave")
axs[1].set_xlabel("X-axis")
axs[1].set_ylabel("Y-axis")
axs[1].legend()
axs[1].grid(True)

axs[2].scatter(x, y_scatter_sin, color="red", label="Sine wave")
axs[2].set_title("Scatter Plot - Sine Wave")
axs[2].set_xlabel("X-axis")
axs[2].set_ylabel("Y-axis")
axs[2].legend()
axs[2].grid(True)


axs[3].scatter(x, y_scatter_cos, color="red", label="Cosine")
axs[3].set_title("Scatter Plot - Cosine")
axs[3].set_xlabel("X-axis")
axs[3].set_ylabel("Y-axis")
axs[3].legend()
axs[3].grid(True)


plt.tight_layout()
plt.show()
