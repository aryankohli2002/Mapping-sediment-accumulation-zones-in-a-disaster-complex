
import numpy as np
import matplotlib.pyplot as plt

def van_rijn_sediment_transport(distance, dx, time_steps, dt, initial_concentration, velocity, sediment_density, sediment_diameter, bed_slope):
    # Calculate the number of spatial points and time steps
    num_points = int(distance / dx) + 1
    num_steps = int(time_steps / dt) + 1

    # Initialize arrays to store sediment concentration values at different time steps
    concentration = np.zeros((num_steps, num_points))

    # Set the initial concentration distribution
    concentration[0, :] = initial_concentration

    # Van Rijn parameters
    transport_coefficient = 0.05  # Sediment transport coefficient
    critical_shear_stress = 0.02  # Critical shear stress

    # Perform time-stepping using Van Rijn model
    for t in range(1, num_steps):
        for i in range(1, num_points - 1):
            # Calculate shear stress using Manning's equation
            shear_stress = bed_slope * velocity**2 / (sediment_density * sediment_diameter)

            # Calculate sediment transport rate using Van Rijn model
            transport_rate = transport_coefficient * (shear_stress - critical_shear_stress)**1.5

            # Update concentration at the current time step
            concentration[t, i] = concentration[t - 1, i] + transport_rate * dt

    return concentration

# Simulation parameters
distance = 10.0   # Total distance to simulate (in meters)
dx = 0.1         # Spatial step size (in meters)
time_steps = 100  # Number of time steps
dt = 0.01        # Time step size (in seconds)

# Initial concentration distribution
initial_concentration = np.zeros(int(distance / dx) + 1)
initial_concentration[int(2 / dx):int(3 / dx) + 1] = 1.0

# Fluid flow parameters
velocity = 0.1        # Flow velocity (in m/s)
bed_slope = 0.001     # Bed slope
sediment_density = 2650.0  # Sediment density (in kg/m^3)
sediment_diameter = 0.0002  # Sediment diameter (in meters)

# Run the sediment transport simulation using Van Rijn model
concentration_result = van_rijn_sediment_transport(distance, dx, time_steps, dt, initial_concentration, velocity, sediment_density, sediment_diameter, bed_slope)

# Plot the results at different time steps
time_values = np.arange(0, time_steps * dt + dt, dt)
for t in range(0, time_steps, 20):
    plt.plot(np.arange(0, distance + dx, dx), concentration_result[t, :], label=f"Time: {time_values[t]:.2f} s")

plt.xlabel("Distance (m)")
plt.ylabel("Sediment Concentration")
plt.legend()
plt.grid(True)
plt.show()
