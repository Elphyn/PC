import numpy as np
from scipy.integrate import odeint

# Constants and initial conditions
g = 9.81  # gravitational acceleration (m/s^2)
L1 = 1.0  # length of the first rod (m)
L2 = 1.0  # length of the second rod (m)
m1 = 1.0  # mass of the first particle (kg)
m2 = 1.0  # mass of the second particle (kg)

# Define the equations of motion
def equations_of_motion(y, t):
    x1, y1, z1, x2, y2, z2, vx1, vy1, vz1, vx2, vy2, vz2 = y

    # First particle's acceleration
    ax1 = (L1 / (L1**2 + L2**2 - 2 * L1 * L2 * (x1 * x2 + y1 * y2 + z1 * z2))) * (m1 * g * x2 - m2 * g * x1)
    ay1 = (L1 / (L1**2 + L2**2 - 2 * L1 * L2 * (x1 * x2 + y1 * y2 + z1 * z2))) * (m1 * g * y2 - m2 * g * y1)
    az1 = (L1 / (L1**2 + L2**2 - 2 * L1 * L2 * (x1 * x2 + y1 * y2 + z1 * z2))) * (m1 * g * z2 - m2 * g * z1 - L1 * g)

    # Second particle's acceleration
    ax2 = (L2 / (L1**2 + L2**2 - 2 * L1 * L2 * (x1 * x2 + y1 * y2 + z1 * z2))) * (m2 * g * x1 - m1 * g * x2)
    ay2 = (L2 / (L1**2 + L2**2 - 2 * L1 * L2 * (x1 * x2 + y1 * y2 + z1 * z2))) * (m2 * g * y1 - m1 * g * y2)
    az2 = (L2 / (L1**2 + L2**2 - 2 * L1 * L2 * (x1 * x2 + y1 * y2 + z1 * z2))) * (m2 * g * z1 - m1 * g * z2 - L2 * g)

    return [vx1, vy1, vz1, vx2, vy2, vz2, ax1, ay1, az1, ax2, ay2, az2]

# Initial conditions
x1_0, y1_0, z1_0 = 0, L1, 0
x2_0, y2_0, z2_0 = L2, 0, 0
vx1_0, vy1_0, vz1_0 = 0, 0, 0
vx2_0, vy2_0, vz2_0 = 0, 0, 0

initial_conditions = [x1_0, y1_0, z1_0, x2_0, y2_0, z2_0, vx1_0, vy1_0, vz1_0, vx2_0, vy2_0, vz2_0]

# Time array
t = np.linspace(0, 10, 1000)  # 10 seconds with 1000 points

# Integrate the equations of motion
solution = odeint(equations_of_motion, initial_conditions, t)

# Extract the positions of the particles
x1, y1, z1, x2, y2, z2, _, _, _, _, _, _ = solution.T

# Plot the motion of the particles
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot(x1, y1, z1, label="Particle 1")
ax.plot(x2, y2, z2, label="Particle 2")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()

plt.show()

