import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming your data is already loaded into a DataFrame called 'df'
# Replace the example data with your actual dataset

# Example data
data = {
    'River flow velocity': [5, 8, 10, 6, 7],
    'River width and depth': [20, 25, 30, 18, 22],
    'River gradient (slope)': [1.5, 2.0, 1.8, 1.2, 1.7],
    'Sediment transport capacity of the river': [50, 45, 55, 40, 60],
    'Floodwater discharge': [1000, 1200, 800, 1500, 1100],
    'Duration of the flood event': [2, 3, 2.5, 2, 4],
    'Sediment size and distribution': [2, 1.8, 2.2, 1.5, 2.5],
    'Sediment density': [2.5, 2.2, 2.8, 2.0, 3.0],
    'Sediment concentration in the water': [20, 18, 22, 15, 25],
    'Channel roughness': [0.02, 0.03, 0.025, 0.015, 0.02],
    'Channel shape': [0, 1, 0, 1, 1],
    'Elevation and slope of surrounding land': [10, 12, 9, 15, 11],
    'Vegetation cover and land use': [0.5, 0.6, 0.4, 0.7, 0.55]
}

df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()