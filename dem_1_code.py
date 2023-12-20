import geemap.core as geemap
import ee

# Create a Map instance
Map = geemap.Map(center=[30.73, 78.98], zoom=8)

# Define the geometry
geometry = ee.Geometry.Polygon(
    [[[78.39255300953737, 30.725195327338472],
      [78.59030691578737, 30.071355556874007],
      [79.32364431813112, 30.199624718563733],
      [79.59280935719362, 30.81251412719082],
      [78.72763601734987, 31.050466811126952]]])

# Filter the image collection
dataset = ee.ImageCollection('COPERNICUS/DEM/GLO30').filterBounds(geometry)

# Select the 'DEM' band
elevation = dataset.select('DEM')

# Visualization parameters
elevationVis = {
    'min': 0.0,
    'max': 1000.0,
    'palette': ['0000ff', '00ffff', 'ffff00', 'ff0000', 'ffffff'],
}

# Calculate median and clip to the geometry
data = elevation.median().clip(geometry)

# Add the layer to the map
Map.addLayer(data, elevationVis, 'DEM')

# Display the map
Map