import geopandas as gpd
  
# Reading the world shapefile
world_data = gpd.read_file(r'world.shp')
  
world_data.plot()
