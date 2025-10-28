"""
This program visualizes the data from an experiment for calculating the density of steel (~7.874 g/cm³).
We measured the mass and the volume of 4 different steel objects. The program applies a linear regression
algorithm to calculate the density of steel by compensating for measurement errors. It also visualizes:
- the experimental data,
- the fitted density line,
- the reference (given) density line,
- the residuals for both fitted and given equations.
"""
import os

import numpy as np
import matplotlib.pyplot as plt

# --- Reference (true) density of steel ---
target_density = 7.874  # g/cm³

# --- Experimental data ---
# Volume (cm³) measured for each object
volume = np.array([0.1, 0.3, 1.0, 2.0])
# Mass (g) measured for each object
mass = np.array([1.0, 2.1, 4.6, 15.0])

# --- Quick per-point densities for reference ---
point_densities = mass / volume
print("Per-point densities (g/cm³):", np.round(point_densities, 3))
print("Mean per-point density:", np.round(np.mean(point_densities), 3))

# --- Linear regression (fit mass = density * volume, through origin) ---
A = volume[:, np.newaxis]  # column vector for lstsq
a, *_ = np.linalg.lstsq(A, mass, rcond=None)
rho = float(a[0])  # calculated density

# --- Calculate fitted mass values and reference mass values ---
mass_fit = rho * volume         # predicted by fitted density
mass_ref = target_density * volume  # predicted by reference density

# --- Calculate residuals/errors ---
residual_fit = mass - mass_fit        # measurement - fitted
residual_ref = mass - mass_ref        # measurement - reference
error_to_ref = mass_ref - mass_fit    # difference between fitted and reference

print(f"Fitted density: {rho:.4f} g/cm³")
print("Residuals (measurement - fitted):", np.round(residual_fit, 4))
print("Residuals (measurement - reference):", np.round(residual_ref, 4))

# --- Plotting ---
plt.figure(figsize=(9,6))

# Scatter experimental data
plt.scatter(volume, mass, color="blue", label="Δεδομένα")

# Plot fitted density line
plt.plot(volume, mass_fit, color="red", label=f"Πυκνότητα: {rho:.2f} g/cm³")

# Plot reference density line
plt.plot(volume, mass_ref, color="green", linestyle="--", label=f"Πραγματική πυκνότητα: {target_density:.3f} g/cm³")

# Dotted vertical lines showing residuals to fitted line
plt.vlines(volume, mass_fit, mass, color="gray", linestyle="dotted", label="Λάθη")

# Display numeric residuals for both fitted and reference lines
for v, m, rf, rr, pd in zip(volume, mass, residual_fit, residual_ref, point_densities):
    plt.text(v, m + 0.5, f"Err(fit)={rf:.2f}\nErr(ref)={rr:.2f}\n",
             fontsize=9, ha="center", color="purple")

# Labels, title, legend, grid
plt.xlabel("Όγκος (cm³)")
plt.ylabel("Μάζα (g)")
plt.title("Πυκνότητα")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("image.png", dpi=600, bbox_inches='tight')
print(f"saved in {os.getcwd()}")
plt.show()
