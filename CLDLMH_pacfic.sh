
#dir=/work/bb1153/b381639/NorESM2
#cdo mul ${dir}/clt_Amon_NorESM2-LM_historical_r3i1p1f1_gn_200001-200912_timmean.nc ${dir}/landmask_LR.nc ${dir}/clt_lm.nc
#cdo sellonlatbox,30,270,-50,50 ${dir}/clt_lm.nc ${dir}/clt.nc
dir=/work/bb1153/b381639/NorESM
cdo mul ${dir}/CLDLOW_150_timmean.nc ${dir}/landmask_SR.nc ${dir}/CLDLOW_150_timmean_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/CLDLOW_150_timmean_lm.nc   ${dir}/CLDLOW.nc
cdo mul ${dir}/CLDMED_150_timmean.nc ${dir}/landmask_SR.nc ${dir}/CLDMED_150_timmean_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/CLDMED_150_timmean_lm.nc   ${dir}/CLDMED.nc
cdo mul ${dir}/CLDHGH_150_timmean.nc ${dir}/landmask_SR.nc ${dir}/CLDHGH_150_timmean_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/CLDHGH_150_timmean_lm.nc   ${dir}/CLDHGH.nc
dir=/work/bb1153/b381639/ERA5
cdo mul ${dir}/CLD_HML_ERA5_monthly_1979-2021_timmean.nc  ${dir}/maskland.nc ${dir}/CLDHML_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/CLDHML_lm.nc ${dir}/CLDHML.nc





