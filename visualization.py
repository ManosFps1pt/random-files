"""
This program visualizes the data from an experiment for calculating the density of steel (~7.874 g/cm³). We measured
the mass and the volume of 4 different steel objects and this program applies a linear regression algorithm in order
to calculate the density of steel by compensating on the error of the measurements. It also visualizes
"""

import matplotlib.pyplot as plt
import numpy as np

# steel data for comparation
target_density = 7.874 # g/cm³
target_x = np.linspace(0, 2, 4)
target_y = target_density * target_x

# Example data (replace with your own)
x = np.array([0.1, 0.3, 1, 2])  # mass
y = np.array([1, 2.1, 4.6, 15]) # volume

# Reshape x for lstsq
A = x[:, np.newaxis]  # column vector

# Solve for slope a in y = a*x
a, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
a = a[0]

# Calculate fitted values
y_fit = a * x
y_target_fit = target_density * x
errors = target_y - y_fit

# --- Show numerical error next to each point ---
for xi, yi, err in zip(x, y, errors):
    plt.text(xi, yi + 0.2, f"{err:.2f}", color="purple", fontsize=9, ha="center")

# Plot
plt.scatter(x, y, label="Δεδομένα", color="blue")
plt.plot(x, y_fit, color="red", label=f"Πυκνότητα: {a:.2f} g/cm³")
plt.plot(target_x, target_y, label=f"Πραγματική πυκνότητα", color="green")
plt.vlines(x, y_target_fit, y, color="gray", linestyle="dotted", label="Error")
plt.xlabel("Μάζα (g)")
plt.ylabel("Όγκος (cm³)")
plt.title("Υπολογισμός Πυκνότητα σιδήρου")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Slope (a): {a:.3f}")
print(f"errors {errors}")