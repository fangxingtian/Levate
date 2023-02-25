# import intake
import pandas as pd
import xarray as xr
import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm
import cmocean.cm as cmo
from scipy.interpolate import CloughTocher2DInterpolator, LinearNDInterpolator, NearestNDInterpolator
import gribscan
import intake
import numcodecs
import dask
dask.config.set(**{'array.slicing.split_large_chunks': True})
import cartopy.crs as ccrs
import sys

cat = intake.open_catalog("/home/b/b381639/nextGems_Cycle2/catalog.yaml")
#run = cat.IFS["tco2559-ng5"]
run = cat.IFS["tco1279-orca025"]
data2d = run.ICMGG_atm2d.to_dask()
data3d = run.ICMU_atm3d.to_dask()

print("cat ok") 


var='msl' # 10u, msl
data=data2d[var]#.isel({'time': slice(0,240)})
Varout=xr.zeros_like(data[0:2849,:])

print ( "select var ok")

outdata = data.resample(time="6H").mean(dim="time")
Varout.data=outdata
Varout.coords['time']=outdata.time

print("6h mean okey")
# sel WNP region, with index

model_lon= Varout.lon
model_lat = Varout.lat

IND1 = np.logical_and(100. <= model_lon, model_lon <= 180)
IND2 = np.logical_and(0. <= model_lat, model_lat <= 60.)
IND = np.logical_and(IND1, IND2)

VarWNP = Varout[:,IND]

print( "VarWNP region selected")

print (VarWNP)
#

## Import the ecco_v4_py library into Python
## =========================================


#import ecco_v4_py as ecco


VarWNP.to_netcdf('/work/bb1153/b381639/IFS/'+var+'_WNP_6hrouly_tco1279-orca025.nc')

