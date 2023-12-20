import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Sediment properties
sediment_density = 10  # Sediment density (kg/m^3)
sediment_diameter = 10.002  # Sediment diameter (m)
settling_velocity = 100 # Sediment settling velocity (m/s)

# Channel properties
channel_length = 100  # Length of the channel (m)
channel_width = 100  # Width of the channel (m)
channel_slope = 10  # Slope of the channel (dimensionless)
channel_flow_velocity = 20000  # Flow velocity in the channel (m/s)

# Initial conditions
initial_sediment_concentration = 1 # Initial sediment concentration (kg/m^3)

# Time steps
t_steps = 10000
t_end = 20000 # Total simulation time (s)
time = np.linspace(0, t_end, t_steps)

# Function to compute sediment concentration change over time
def sediment_transport(concentration, t):
    # Compute sediment transport rate using Einstein-Brown equation
    sediment_transport_rate = sediment_density * (settling_velocity - channel_flow_velocity) * \
                             concentration / (channel_width * sediment_diameter)

    # Compute sediment concentration change using Exner equation
    d_concentration_dt = - sediment_transport_rate / (channel_length * channel_width)

    return d_concentration_dt

# Initial sediment concentration distribution
sediment_concentration_initial = np.full(t_steps, initial_sediment_concentration)

# Numerical integration using scipy's odeint
sediment_concentration_result = odeint(sediment_transport, sediment_concentration_initial, time)

# Plot the results
plt.plot(time, sediment_concentration_result)
plt.xlabel('Time (s)')
plt.ylabel('Sediment Concentration (kg/m^3)')
plt.title('Sediment Concentration in the Channel over Time')
plt.show()
