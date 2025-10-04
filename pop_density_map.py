import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import contextily as ctx

df = pd.read_csv("C:/Users/nikit/Downloads/are_general_2020.csv")

geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

gdf = gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(8,8))
gdf.plot(
    ax=ax, 
    column="are_general_2020", 
    cmap="magma_r", 
    legend=True, 
    markersize=50,
    vmin=0,
    vmax=25
)

ctx.add_basemap(ax, crs=gdf.crs)

plt.title("Population Density in UAE")
plt.show()