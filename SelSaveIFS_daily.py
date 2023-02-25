# import intake
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
import cartopy.crs as ccrs

cat = intake.open_catalog("/home/b/b381639/nextGems_Cycle2/catalog.yaml")
run = cat.IFS["tco2559-ng5"]
#run = cat.IFS["tco1279-orca025"]
data = run.ICMGG_atm2d.to_dask()


#data1=data.u10.isel({'time': slice(0,240)})
#u10, 10u, 10v

var='10u'
daily_mean = data[var].resample(time="1D").mean(dim="time") #.compute()

daily_mean.to_netcdf('/scratch/b/b381639/IFS/u10_daily_tco2559-ng5.nc')


