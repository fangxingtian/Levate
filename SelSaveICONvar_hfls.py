# basics
import intake
import xarray as xr
import dask  # memory-efficient parallel computation and delayed execution (lazy evaluation).
import subprocess as sp
import getpass
import gem_helpers as gem


uid = getpass.getuser()
image_path = gem.make_tempdir("intake_demo_plots")
data_cache_path = gem.make_tempdir("intake_demo_data")

catalog_file = "/work/ka1081/Catalogs/dyamond-nextgems.json"
cat = intake.open_esm_datastore(catalog_file)

fre  = "3hour" #30minute
var  = "hfls" #tas, sst
rea  = "atm"

hits = cat.search(simulation_id=["ngc2009", "ngc2012","ngc2013"],  realm=rea, variable_id= var, frequency=fre)
simulation_id=["ngc2012","ngc2013"]
sim= simulation_id[0]        

catalog=hits.search(simulation_id=sim,frequency=fre, variable_id=var)
files=sorted(catalog.unique("uri")["uri"]["values"])
outfile = f"{data_cache_path}/{var}_daymean_{sim}.nc"

query = (
    [
        "cdo",
        "-P",
        "4",
#         "-remapcon,r360x180",
        "-daymean",
        "-sellonlatbox,300,310,5,17",   #-sellonlatbox,0,360,-30,30"
        "-cat",
        f"-apply,-selname,{var}",
        "[",
    ]
    + files[:20]
    + ["]", outfile]
)
# Note, we only use the first 10 files to save time (the [:10] in files[:10]). Remove the [:10] to compute over the whole experiment.
print(query)
sp.run(query)


