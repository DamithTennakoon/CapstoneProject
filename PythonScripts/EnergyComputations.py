# Library imports
import numpy as np
import math
import matplotlib.pyplot as plt

# Parameters (SI Units)
min = 0
max = 800
step = 0.1
h = np.arange(min, max, step) # Depth in meters (+ive down)
r = 1 # Radius in meters
m = 1.3 # Kg
g = 9.81 # Force of gravity
ro = 997 # Density of water (kg/m^3)

A = 4 * np.pi * r**2

lakeOntario = 250
ideaDepth = 500

# Factors
kilo = 1000
mega = 10**6

# Labels
xLabel = "Depth (m)"
yLabels = ["Pressure (kPa)", "Force (kN)","Work (Mega Joules)"]
graphTitles = ["Pressure vs Depth", "Force vs Depth", "Work vs Depth"]

# Compute pressure, force, and work
P = np.array(ro * g * h)
F = np.array(A * P)
W = np.array(F * h)

# Plot graphs
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))
axes[0].plot(h, P / kilo, 'orange')
axes[1].plot(h, F / kilo, 'blue')
axes[2].plot(h, W / mega, 'red')

# Label axis
for i in range(len(axes)):
    axes[i].set(xlabel=xLabel, ylabel=yLabels[i], title=graphTitles[i])

# Plot values at key depths
axes[0].plot(h[np.where(h == lakeOntario)], P[np.where(h == lakeOntario)] / kilo, 'o')
axes[0].plot(h[np.where(h == ideaDepth)], P[np.where(h == ideaDepth)] / kilo, 'o')
axes[1].plot(h[np.where(h == lakeOntario)], F[np.where(h == lakeOntario)] / kilo, 'o')
axes[1].plot(h[np.where(h == ideaDepth)], F[np.where(h == ideaDepth)] / kilo, 'o')
axes[2].plot(h[np.where(h == lakeOntario)], W[np.where(h == lakeOntario)] / mega, 'o')
axes[2].plot(h[np.where(h == ideaDepth)], W[np.where(h == ideaDepth)] / mega, 'o')

plt.show()