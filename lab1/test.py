import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

G = 6.67430e-11  # m³/kg·s²
M = 5.97219e24   # kg
R = 6371000      # m
v1 = np.sqrt(G * M / R)

def rocket_equations(t, y, F_thrust, u):
    m, v = y
    dm_dt = -F_thrust / u
    dv_dt = F_thrust / m - g
    return [dm_dt, dv_dt]

m0_values = np.linspace(1000, 100000, 100)
F_thrust_values = np.linspace(1e3, 1e7, 100)

X, Y = np.meshgrid(m0_values, F_thrust_values)
Z = np.zeros_like(X)

for i in range(len(m0_values)):
    for j in range(len(F_thrust_values)):
        m0 = m0_values[i]
        F_thrust = F_thrust_values[j]
        u = 3000  # m/s
        g = 9.81  # m/s²
        m1 = m0 - F_thrust / u * 100  # approximate engine operation time - 100 s
        delta_v = u * np.log(m0 / m1)

        if delta_v >= v1:
            Z[j, i] = 1

plt.contourf(X, Y, Z, levels=[-0.5, 0.5, 1.5], colors=['white', 'blue'], alpha=0.5)
plt.xlabel('m0 (kg)')
plt.ylabel('F_thrust (N)')
plt.title('Phase Diagram for Reaching First Cosmic Velocity')
plt.show()
