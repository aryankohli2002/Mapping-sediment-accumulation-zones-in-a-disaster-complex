import ee
import geemap.core as geemap
# Authenticate to Earth Engine
ee.Authenticate()
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

# Calculate slope
slope = ee.Terrain.slope(elevation)

m = geemap.Map()
# Set the map center and add the layer
m.set_center(78.98, 30.73, 8)
m.add_layer(slope, {'min': 0, 'max': 60}, 'slope')
m



