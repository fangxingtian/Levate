##############

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import iris
import numpy as np
import sys
sys.path.append('/pf/b/b381639')
import fxtian_function as fx
from iris.time import PartialDateTime
import datetime
import cf_units
import iris.coord_categorisation
import iris.quickplot as qplt
import matplotlib.pyplot as plt
import numpy as np
import xarray as ar


# %% list of data to read in
def data_dict(myid):
    if myid == 'sshf':
        mydict = {
            'indir': '/work/bb1153/b381639/ERA5',
            'infile': '/work/bb1153/b381639/ERA5/sshf_2020_tropical_ocean.nc',
            'key': iris.Constraint(cube_func=(lambda c: c.var_name == 'sshf'))
        }

    elif myid == 'slhf':
        mydict = {
            'indir': '/work/bb1153/b381639/ERA5',
            'infile': '/work/bb1153/b381639/ERA5/slhf_2020_tropical_ocean.nc',
            'key': iris.Constraint(cube_func=(lambda c: c.var_name == 'slhf'))
        }
    return(mydict)

## create correct time cubelist to save output data
cubelist_ct = iris.cube.CubeList()

##readin sfcwind
datasets=['slhf','sshf']  #['ERAI']  # ['u-bt405','u-bt406','u-bm213','u-be034','u-bd818']
for my_dataset in datasets:
    print('--> '+my_dataset)
    mydict = data_dict(my_dataset)
    datain = iris.load_cube(mydict['infile'],mydict['key'])
#    data_time= fx.correct_time(datain)

    cubelist_ct.append(datain)



#############################
##select region covers EURE4A
#############################
left = -180
right = 180
bottom = -20
top = 20
y=fx.selregion(cubelist_ct[0],bottom,top,left,right)
x=fx.selregion(cubelist_ct[1],bottom,top,left,right)
x=x[:,0,:,:]
y=y[:,0,:,:]

regyonx=fx.regress_yonx(x,y)
iris.save(regyonx,mydict['indir']+'/regress_slhf_sshf_ERA5.nc')






