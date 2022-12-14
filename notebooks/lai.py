import numpy as np
from sys import argv
from netCDF4 import Dataset
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap 
from mpl_toolkits.basemap import Basemap

input_dir="/home/alper/proj/landsaf/input/"
latcorners = [33,45]
loncorners = [23,48]

flist_=glob.glob(input_dir+"*nc")

file_ds=Dataset(flist_[0])

lai_data=file_ds.variables["LAI"][:].data[0]
lai_lat=file_ds.variables["lat"][:]
lai_lon=file_ds.variables["lon"][:]
lai_mask=file_ds.variables["quality_flag"][:].mask[0]
lai_qf=file_ds.variables["quality_flag"][:].data


lat0=np.where(lai_lat<=latcorners[0])[0].min()
lat1=np.where(lai_lat<=latcorners[1])[0].min()
lon0=np.where(lai_lon<=loncorners[0])[0].max()
lon1=np.where(lai_lon<=loncorners[1])[0].max()
lai_latlon=np.meshgrid(lai_lat,lai_lon)

trk_data=lai_data[lat1:lat0,lon0:lon1]

#plt.imshow(lai_data[lat1:lat0,lon0:lon1])
#plt.show()

lonlat_= np.meshgrid(np.linspace(loncorners[0],loncorners[1],int((loncorners[1]-loncorners[0])/.05)),\
                     np.linspace(latcorners[0],latcorners[1],int((latcorners[1]-latcorners[0])/.05)))