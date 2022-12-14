import numpy as np
from sys import argv
from netCDF4 import Dataset
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap 
from mpl_toolkits.basemap import Basemap

input_dir="/home/alper/proj/landsaf/input/"
output_dir="/home/alper/proj/landsaf/output/"
latcorners = [33,45]
loncorners = [23,48]

flist_=glob.glob(input_dir+"*nc")
for file in flist_:
    file_ds=Dataset(file)
    lai_lat=file_ds.variables["lat"][:]
    lai_lon=file_ds.variables["lon"][:]
    latli = np.argmin( np.abs( lai_lat - latcorners[0] ) )
    latui = np.argmin( np.abs( lai_lat - latcorners[1] ) ) 
    # longitude lower and upper index
    lonli = np.argmin( np.abs( lai_lon - loncorners[0] ) )
    lonui = np.argmin( np.abs( lai_lon - loncorners[1] ) )  
    trk_lai = file_ds.variables["LAI"][:,latui:latli,lonli:lonui]
    #plt.imshow(lai_data[lat1:lat0,lon0:lon1])
    #plt.show()
    trk_masked=trk_lai.data[0]
    trk_masked[np.where(trk_lai.mask[0]==True)]=np.nan
    m = Basemap(resolution='h',\
                llcrnrlat=latcorners[0],urcrnrlat=latcorners[1],\
                llcrnrlon=loncorners[0],urcrnrlon=loncorners[1])
    m.drawcoastlines()
    m.drawcountries()
    m.imshow(trk_masked[::-1],vmin=.1,vmax=6.9,cmap="YlGn")
#    m.colorbar()
    jpeg_name=file.split("/")[-1].split(".")[0].split("_")[-1]
    plt.axis('off')
    plt.savefig(output_dir+"Turk_LAI_"+jpeg_name+".png", transparent=True,\
                dpi=200, bbox_inches='tight', pad_inches = 0)
    plt.cla()
    plt.clf()
    plt.close()