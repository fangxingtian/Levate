# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import iris
import numpy as np
import sys
#sys.path.append('/home/users/bi913747/MJO/mjo_utils')
#import mjo_functions as mjo
from iris.time import PartialDateTime
import datetime
import cf_units
import iris.coord_categorisation
import iris.quickplot as qplt
import matplotlib.pyplot as plt
import numpy as np
import xarray as ar


'''
### correct time for ICON atm
'''
def correct_time(datain,starttime='{} since 2020-01-29 00:00:00'):
    t_coord = datain.coord('time')
    t_coord.points
    t_unit = t_coord.attributes['invalid_units']
    timestep, _, t_fmt_str = t_unit.split(' ')
    new_t_unit_str = '{} since 2020-01-29 00:00:00'.format(timestep)
    new_t_unit = cf_units.Unit(new_t_unit_str, calendar=cf_units.CALENDAR_STANDARD)
    
    datastr=t_coord.points.astype(str)
    new_datetimes = [datetime.datetime(int(dt[:4]),int(dt[4:6]),int(dt[6:8])) for dt in datastr]
    new_dt_points = [new_t_unit.date2num(new_dt) for new_dt in new_datetimes]
    new_t_coord = iris.coords.DimCoord(new_dt_points, standard_name='time', units=new_t_unit)
    
    t_coord_dim = datain.coord_dims('time')
    datain.remove_coord('time')
    datain.add_dim_coord(new_t_coord,t_coord_dim) # space before t_coord_dim is horrible
    return(datain)

'''
#################

###########################
### used for select region
##########################
'''
def selregion(cubein,lat_min,lat_max,lon_min,lon_max):
    variable_constraint = iris.Constraint(latitude=lambda cell: lat_min <= cell <= lat_max, \
                                          longitude=lambda cell: lon_min <= cell <= lon_max)
    cube_ext=cubein.extract(variable_constraint)
    return(cube_ext)



###############################
# %%%Point to Point Regress y_cube on x_cube
########################################
'''
## The coefficient of X in the line of regression of Y on X is called the regression coefficient of Y on X. \ 
## It represents change in the value of dependent variable (Y) corresponding to unit change in the value of \
## independent variable (X).
'''
def regress_yonx(x_cube,y_cube,lag_min=0,lag_max=0):
    import iris
    from scipy.stats import linregress

    lags = range(lag_min,lag_max+1)
    nlags = len(lags)
    lag_coord = iris.coords.DimCoord(lags,var_name='lag_time',long_name='Lag time')
    
        #baselon = base_cube.coord('longitude').points

    lon_coord = y_cube.coord('longitude')
    lat_coord = y_cube.coord('latitude')
    nlon = len(lon_coord.points)
    nlat = len(lat_coord.points)
    
    # create a new cube to save regressed data
    regress_cube = iris.cube.Cube(np.zeros((nlags,nlat,nlon),dtype=np.float32),\
                                  dim_coords_and_dims=[[lon_coord,2],[lat_coord,1],[lag_coord,0]],\
                                  var_name='hfls_wind_p2p_regressions',\
                                  long_name='hfls_wind_point to point_regressions')
 
    for y,lat in enumerate(y_cube.coord('latitude').points):
        for t,t_slice in enumerate(y_cube[:,y,:].slices(['time'])):
            for l,lag in enumerate(lags):

                s,i,r,p,e = linregress(x_cube.data[:,y,t],np.roll(t_slice.data,-lag))

                regress_cube.data[l,y,t] = s
  

    return(regress_cube)



def correlation_yonx(x_cube,y_cube,lag_min=0,lag_max=0):
    import iris
    from scipy.stats import linregress

    lags = range(lag_min,lag_max+1)
    nlags = len(lags)
    lag_coord = iris.coords.DimCoord(lags,var_name='lag_time',long_name='Lag time')
    
        #baselon = base_cube.coord('longitude').points

    lon_coord = y_cube.coord('longitude')
    lat_coord = y_cube.coord('latitude')
    nlon = len(lon_coord.points)
    nlat = len(lat_coord.points)
    
    # create a new cube to save regressed data
    correlation_cube = iris.cube.Cube(np.zeros((nlags,nlat,nlon),dtype=np.float32),\
                                  dim_coords_and_dims=[[lon_coord,2],[lat_coord,1],[lag_coord,0]],\
                                  var_name='hfls_wind_p2p_regressions',\
                                  long_name='hfls_wind_point to point_regressions')
 
    for y,lat in enumerate(y_cube.coord('latitude').points):
        for t,t_slice in enumerate(y_cube[:,y,:].slices(['time'])):
            for l,lag in enumerate(lags):

                s,i,r,p,e = linregress(x_cube.data[:,y,t],np.roll(t_slice.data,-lag))

                correlation_cube.data[l,y,t] = r
  

    return(correlation_cube)
