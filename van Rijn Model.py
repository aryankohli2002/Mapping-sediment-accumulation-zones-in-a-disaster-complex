import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Sediment properties
sediment_density = 2650  # Sediment density (kg/m^3)
sediment_diameter = 0.002  # Sediment diameter (m)
settling_velocity = 0.1  # Sediment settling velocity (m/s)

# Fluid properties
fluid_density = 1000  # Fluid density (kg/m^3)

# Channel properties
channel_length = 1000  # Length of the channel (m)
channel_width = 5  # Width of the channel (m)
channel_slope = 0.001  # Slope of the channel (dimensionless)
channel_flow_velocity = 2  # Flow velocity in the channel (m/s)

# Van Rijn model parameters
alpha = 0.055  # Empirical coefficient
beta = 0.085  # Empirical coefficient
p = 1.3  # Exponent for bed load sediment transport
q = 2.5  # Exponent for suspended load sediment transport

# Critical shear stress calculation
tau_c = (sediment_density - fluid_density) * g * sediment_diameter

# Function to compute sediment concentration change over time using Van Rijn model
def sediment_transport(concentration, t):
    # Compute shear stress using Manning's equation (simplified)
    flow_area = channel_width * concentration
    hydraulic_radius = flow_area / (2 * (channel_width + concentration))
    tau = (1 / channel_slope) * (channel_flow_velocity ** 2) * (hydraulic_radius ** (2/3))

    # Define the dimensionless coefficient C for sediment characteristics and bed roughness
    C = 0.025  # You may adjust this value based on your specific case and data

    # Compute total sediment transport rate using the Van Rijn equation
    q_s = (alpha * channel_flow_velocity * C / sediment_density) * (tau - tau_c) ** p * \
          np.sqrt(tau / fluid_density) + (beta * channel_flow_velocity * C / sediment_density) * (tau - tau_c) ** q

    # Compute sediment concentration change using Exner equation
    d_concentration_dt = - q_s / (channel_length * channel_width)

    return d_concentration_dt

# Initial sediment concentration
initial_sediment_concentration = 0.05  # Choose an appropriate initial value (kg/m^3)

# Time steps
t_steps = 10
t_end = 3600  # Total simulation time (s)
time = np.linspace(0, t_end, t_steps)

# Initial sediment concentration distribution
initial_sediment_concentration = np.full(t_steps, initial_sediment_concentration)

# Numerical integration using scipy's odeint
sediment_concentration_result = odeint(sediment_transport, initial_sediment_concentration, time)

# Plot the results
plt.plot(time, sediment_concentration_result)
plt.xlabel('Time (s)')
plt.ylabel('Sediment Concentration (kg/m^3)')
plt.title('Sediment Concentration in the Channel over Time (Van Rijn Model)')
plt.show()
