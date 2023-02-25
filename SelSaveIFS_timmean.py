


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
#run = cat.IFS["tco2559-ng5"]
run = cat.IFS["tco1279-orca025"]
data = run.ICMU_atm3d.to_dask()




var='u'
timmean = data[var].mean(dim="time") #.compute()

timmean.to_netcdf('/scratch/b/b381639/IFS/u_timmean_tco1279-orca025.nc')


