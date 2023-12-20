import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Sediment properties
sediment_density = 985  # Sediment density (kg/m^3)
sediment_diameter = 1.5  # Sediment diameter (m)
settling_velocity = 0.1  # Sediment settling velocity (m/s)

# Channel properties
channel_length = 1000  # Length of the channel (m)
channel_width = 5  # Width of the channel (m)
channel_slope = 0.001  # Slope of the channel (dimensionless)
channel_flow_velocity = 2  # Flow velocity in the channel (m/s)

# Meyer-Peter Müller model parameters
Cs = 0.025  # Dimensionless coefficient related to sediment characteristics and bed roughness
n = 1.5  # Exponent related to flow regime
beta = 6  # Dimensionless constant influencing suspension of fine sediments

# Critical shear stress calculation
tau_c = (sediment_density - 1000) * g * sediment_diameter

# Time steps
t_steps = 10
t_end = 60  # Total simulation time (s)
time = np.linspace(0, t_end, t_steps)

# Initial sediment concentration
initial_sediment_concentration = 0.05  # Choose an appropriate initial value (kg/m^3)

# Function to compute sediment concentration change over time using Meyer-Peter Müller model
def sediment_transport(concentration, t):
    # Compute shear stress using Manning's equation (simplified)
    flow_area = channel_width * concentration
    hydraulic_radius = flow_area / (2 * (channel_width + concentration))
    tau = (1 / channel_slope) * (channel_flow_velocity ** 2) * (hydraulic_radius ** (2/3))

    # Compute sediment transport rate using Meyer-Peter Müller equation
    q_s = (Cs * (tau - tau_c) ** n) / (1 + beta * sediment_diameter * (tau - tau_c))

    # Compute sediment concentration change using Exner equation
    d_concentration_dt = - q_s / (channel_length * channel_width)

    return d_concentration_dt

# Initial sediment concentration distribution
initial_sediment_concentration = np.full(t_steps, initial_sediment_concentration)

# Numerical integration using scipy's odeint
sediment_concentration_result = odeint(sediment_transport, initial_sediment_concentration, time)

# Plot the results
plt.plot(time, sediment_concentration_result)
plt.xlabel('Time (s)')
plt.ylabel('Sediment Concentration (kg/m^3)')
plt.title('Sediment Concentration in the Channel over Time (Meyer-Peter Müller Model)')
plt.show()
