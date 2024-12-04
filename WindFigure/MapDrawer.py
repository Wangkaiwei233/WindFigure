import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import matplotlib.pyplot as plt
import numpy as np

class MapDrawer:
    figureSize: tuple[int, int]
    mapRange: tuple[float, float, float, float]


    def __init__(self):
        self.figsize = (12, 8)
        self.mapRange = (25, 85, 0, 40)

    def drawBaseMap(self):
        fig = plt.figure(figsize=(12,8))
        proj = ccrs.PlateCarree(central_longitude=180)
        
        leftlon, rightlon, lowerlat, upperlat = self.mapRange
        imgRange = [leftlon, rightlon, lowerlat, upperlat]

        ax = fig.add_axes([0.1, 0.1, 0.8, 0.6],projection = proj)
        ax.set_extent(imgRange, crs=ccrs.PlateCarree())
        ax.add_feature(cfeature.COASTLINE) 
        ax.set_xticks(np.arange(leftlon,rightlon,10), crs=ccrs.PlateCarree())
        ax.set_yticks(np.arange(lowerlat,upperlat,10), crs=ccrs.PlateCarree())
        lon_formatter = cticker.LongitudeFormatter()
        lat_formatter = cticker.LatitudeFormatter()
        ax.xaxis.set_major_formatter(lon_formatter)
        ax.yaxis.set_major_formatter(lat_formatter)
        return fig, ax
    
def main():
    """Test function for drawBaseMap"""
    drawer = MapDrawer()
    fig, ax = drawer.drawBaseMap()
    plt.show()

if __name__ == "__main__":
    main()
