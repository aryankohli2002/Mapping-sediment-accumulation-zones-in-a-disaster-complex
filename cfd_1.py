import numpy as np
import matplotlib.pyplot as plt
import ee
from IPython.display import Image

# Authenticate to Earth Engine
# ee.Authenticate()
ee.Initialize()

# Define the polygon geometry
geometry = ee.Geometry.Polygon(
    [[[78.39255300953737, 30.725195327338472],
      [78.59030691578737, 30.071355556874007],
      [79.32364431813112, 30.199624718563733],
      [79.59280935719362, 30.81251412719082],
      [78.72763601734987, 31.050466811126952]]])

# Load the SRTM dataset and clip it to the defined geometry
dataset = ee.Image('CGIAR/SRTM90_V4').clip(geometry)
elevation = dataset.select('elevation')

# Specify the number of chunks
num_chunks = 10

# Get the bounds of the geometry
bounds = geometry.bounds()

# Extract coordinates from the bounds
coordinates = bounds.coordinates().getInfo()[0]

# Create a grid of rectangles
grid = []
for i in range(num_chunks):
    for j in range(num_chunks):
        cell = ee.Geometry.Rectangle([
            coordinates[i][j],
            coordinates[i][j + 1],
            coordinates[i + 1][j + 1],
            coordinates[i + 1][j],
        ])
        grid.append(cell)




# Initialize elevation_array
elevation_array = np.array([])

# This modification adds a check to ensure that the 'features' key exists 
# and contains a non-empty list before attempting to access its elements. 
# It also prints a warning message for cases where the elevation data is empty or invalid.

# Sample elevation data for each grid cell
for cell in grid:
    cell_elevation = elevation.sample(region=cell, scale=300).getInfo()

    # Check if 'features' key exists and has non-empty list
    if 'features' in cell_elevation and cell_elevation['features']:
        cell_array = np.array(cell_elevation['features'][0]['properties']['elevation'])
        elevation_array = np.concatenate((elevation_array, cell_array))
    else:
        print("Warning: Empty or invalid elevation data for the current cell. Skipping.")


# Check if elevation_array is not empty
if elevation_array.size > 0:
    # Define the terrain profile using the elevation data
    terrain = elevation_array - np.min(elevation_array)

    # Define the initial fluid depth
    h = np.zeros_like(terrain)
    h[:30] = 1  # fluid to the left of the terrain

    # Define the fluid velocity
    u = np.zeros_like(terrain)

    # Define the time step and the gravitational acceleration
    dt = 0.01
    g = 9.81

    # Run the simulation for a certain number of steps
    for _ in range(1000):
        # Compute the fluxes
        hu = h * u
        h_flux = hu
        hu_flux = hu ** 2 / h + 0.5 * g * h ** 2

        # Update the fluid depth and velocity using a simple finite difference scheme
        h[1:-1] -= dt * (h_flux[2:] - h_flux[:-2])
        u[1:-1] -= dt * (hu_flux[2:] - hu_flux[:-2]) / h[1:-1]

        # Apply reflective boundary conditions
        h[0] = h[1]
        h[-1] = h[-2]
        u[0] = -u[1]
        u[-1] = -u[-2]

    # Plot the final fluid depth
    plt.plot(h)
    plt.xlabel('Distance (pixels)')
    plt.ylabel('Fluid Depth')
    plt.title('Fluid Depth Profile over Terrain')
    plt.show()
else:
    print("Error: Unable to retrieve valid elevation data from Earth Engine.")


