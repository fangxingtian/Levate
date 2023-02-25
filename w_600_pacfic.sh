
dir=/work/bb1153/b381639/NorESM2
cdo sellonlatbox,30,270,-50,50 ${dir}/wap_timmean_600_lm.nc ${dir}/OMEGA_600.nc
dir=/work/bb1153/b381639/NorESM
cdo sellonlatbox,30,270,-50,50 ${dir}/OMEGA_150_timmean_600_lm.nc   ${dir}/OMEGA_600.nc
dir=/work/bb1153/b381639/ERA5
cdo sellonlatbox,30,270,-50,50 ${dir}/W_ERA5_1979-2021_timmean_600_lm.nc ${dir}/OMEGA_600.nc





