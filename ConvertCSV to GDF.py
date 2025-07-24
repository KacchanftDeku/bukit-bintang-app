import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Step 1: Read the CSV file
df = pd.read_csv(r"C:\Users\User\Documents\2025 Master UiTM\Sem 1\GES 716 Programming\SLIDE\INDIVIDUAL PROJECT\Test Koordinat Kedai.csv", encoding='ISO-8859-1')

# Step 2: Create Point geometries from latitude and longitude
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

# Step 3: Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# To show full table
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows
pd.set_option('display.max_colwidth', None) # Show full content in each cell

# Optional: print or save to check
print(gdf.head())
