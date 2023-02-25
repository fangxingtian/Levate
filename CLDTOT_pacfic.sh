
dir=/work/bb1153/b381639/NorESM2
cdo mul ${dir}/clt_Amon_NorESM2-LM_historical_r3i1p1f1_gn_200001-200912_timmean.nc ${dir}/landmask_LR.nc ${dir}/clt_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/clt_lm.nc ${dir}/clt.nc
dir=/work/bb1153/b381639/NorESM
cdo mul ${dir}/CLDTOT_150_timmean.nc ${dir}/landmask_SR.nc ${dir}/CLDTOT_150_timmean_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/CLDTOT_150_timmean_lm.nc   ${dir}/CLDTOT.nc
dir=/work/bb1153/b381639/ERA5
cdo mul ${dir}/CLDTOT_ERA5_monthly_1979-2021.nc  ${dir}/maskland.nc ${dir}/CLDTOT_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/CLDTOT_lm.nc ${dir}/CLDTOT.nc





