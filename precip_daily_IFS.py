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
data = run.ICMGG_atm2d.to_dask()

#But fluxes are accumulated from start of the month, or for Jan 2020, it would be Jan 20th. 
#So we need to take the difference from day after to current day. 

yyyys=2020
yyyye=2021
yr=yyyys
#day=4
mms=1
mme=12
cdatearr=[]
dayarr=[]

while yr<=yyyye:
    yyyy=str(yr)
    mth=mms
    if yr==yyyye:
        mthe=mme
    else:
        mthe=12
    while mth<=mthe:
        if mth<10:
            mm='0'+str(mth)
        else:
            mm=str(mth)
        if mth==1 or mth==3 or mth==5 or mth==7 or mth==8 or mth==10 or mth==12:
            daye=31
        elif mth==4 or mth==6 or mth==9 or mth==11:
            daye=30
        if (yr%4)==0 and mth==2:
            daye=29
        elif (yr%4)!=0 and mth==2:
            daye=28
        if yr==2020 and mth==1:
            days=20
        else:
            days=1
        day=days
        tidx=0
        while day<=daye:
            if day<10:
                dd='0'+str(day)
            else:
                dd=str(day)
            cdatearr.append(yyyy+'-'+mm+'-'+dd)
            dayarr.append(day)
            #print(data.cp.sel(time=yyyy+'-'+mm+'-'+dd+'T00:00:00.000000000').time)
            day=day+1
            #cidx=cidx+1
        mth=mth+1
    yr=yr+1

print(np.shape(cdatearr)[0]-1)
#print(cdatearr)

SHFarray=[]
cidx=0
while cidx<=np.shape(cdatearr)[0]-2:
    cdate=cdatearr[cidx]
    cdatep=cdatearr[cidx+1]
    #print(dayarr[cidx+1])
    #dlen=len(dayarr[cidx+1])
    if dayarr[cidx+1]==2 or cidx==0:
        #print('Use only '+cdatep)
        #print('datestamp='+cdate+'T00:00:00.000000000')
        SHFarray.append(data.cp.sel(time=cdatep+'T00:00:00.000000000').reset_coords('time', drop=True)*1000)
        #print(SHF.max())
    else:
        #print('Use '+cdatep+' - '+cdate)
        SHFarray.append((data.cp.sel(time=cdatep+'T00:00:00.000000000')-data.cp.sel(time=cdate+'T00:00:00.000000000') )*1000)    
        #SHFarray.append(SHF)
    cidx=cidx+1

xarraySHF=xr.concat(SHFarray,dim='time')

xarraySHF.to_netcdf('/scratch/b/b381639/IFS/CP_daily_tco1279-orca025.nc')




