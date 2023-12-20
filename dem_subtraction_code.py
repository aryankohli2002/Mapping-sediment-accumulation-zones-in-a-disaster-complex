import ee
import geemap.core as geemap

# Authenticate to Earth Engine
ee.Authenticate()
ee.Initialize()

# Create a Map instance
Map = geemap.Map(center=[30.73, 78.98], zoom=8)

# Define the geometry
geometry = ee.Geometry.Polygon(
    [[[78.39255300953737, 30.725195327338472],
      [78.59030691578737, 30.071355556874007],
      [79.32364431813112, 30.199624718563733],
      [79.59280935719362, 30.81251412719082],
      [78.72763601734987, 31.050466811126952]]])

# Filter the image collection for COPERNICUS DEM
dataset1 = ee.ImageCollection('COPERNICUS/DEM/GLO30').filterBounds(geometry)
elevation1 = dataset1.select('DEM').median().clip(geometry)

# Load the SRTM dataset and clip it to the defined geometry
dataset2 = ee.Image('CGIAR/SRTM90_V4').clip(geometry)
elevation2 = dataset2.select('elevation')

# Subtract the SRTM data from the COPERNICUS DEM data
subtracted = elevation1.subtract(elevation2)

# Visualization parameters
subtractedVis = {
    'min': -500.0,
    'max': 500.0,
    'palette': ['0000ff', 'ffffff', 'ff0000'],
}

# Add the layer to the map
Map.addLayer(subtracted, subtractedVis, 'DEM Subtraction')

# Display the map
Map