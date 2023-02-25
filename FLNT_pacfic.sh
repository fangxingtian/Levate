
dir=/work/bb1153/b381639/NorESM2
cdo mul ${dir}/rlut_Amon_NorESM2-LM_historical_r3i1p1f1_gn_200001-200912_timmean.nc ${dir}/landmask_LR.nc ${dir}/rlut_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/rlut_lm.nc ${dir}/rlut.nc
dir=/work/bb1153/b381639/NorESM
cdo mul ${dir}/FLNT_150_timmean.nc ${dir}/landmask_SR.nc ${dir}/FLNT_150_timmean_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/FLNT_150_timmean_lm.nc   ${dir}/FLNT.nc
dir=/work/bb1153/b381639/ERA5
cdo mul ${dir}/OLR_ERA5_monthly_1979-2021.nc  ${dir}/maskland.nc ${dir}/OLR_lm.nc
cdo sellonlatbox,30,270,-50,50 ${dir}/OLR_lm.nc ${dir}/OLR.nc





