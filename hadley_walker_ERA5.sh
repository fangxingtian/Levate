
cd /work/bb1153/b381639/ERA5

cdo zonmean -sellonlatbox,120,270,-50,50 W_ERA5_monthly_1979-2021_timmean.nc OMEGA_Hadley_zonmean.nc
cdo zonmean -sellonlatbox,120,270,-50,50 U_ERA5_monthly_1979-2021_timmean.nc         U_Hadley_zonmean.nc
cdo zonmean -sellonlatbox,120,270,-50,50 V_ERA5_monthly_1979-2021_timmean.nc         V_Hadley_zonmean.nc
cdo zonmean -sellonlatbox,120,270,-50,50 Q_ERA5_monthly_1979-2021_timmean.nc         Q_Hadley_zonmean.nc


cdo zonmean -sellonlatbox,120,180,-50,50 W_ERA5_monthly_1979-2021_timmean.nc OMEGA_Hadley_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 U_ERA5_monthly_1979-2021_timmean.nc         U_Hadley_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 V_ERA5_monthly_1979-2021_timmean.nc         V_Hadley_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 Q_ERA5_monthly_1979-2021_timmean.nc         Q_Hadley_zonmean_w.nc

cdo zonmean -sellonlatbox,180,270,-50,50 W_ERA5_monthly_1979-2021_timmean.nc OMEGA_Hadley_zonmean_e.nc
cdo zonmean -sellonlatbox,180,270,-50,50 U_ERA5_monthly_1979-2021_timmean.nc         U_Hadley_zonmean_e.nc
cdo zonmean -sellonlatbox,180,270,-50,50 V_ERA5_monthly_1979-2021_timmean.nc         V_Hadley_zonmean_e.nc
cdo zonmean -sellonlatbox,180,270,-50,50 Q_ERA5_monthly_1979-2021_timmean.nc         Q_Hadley_zonmean_e.nc

cdo mermean -sellonlatbox,0,360,-20,20 W_ERA5_monthly_1979-2021_timmean.nc OMEGA_Walker_mermean.nc
cdo mermean -sellonlatbox,0,360,-20,20 U_ERA5_monthly_1979-2021_timmean.nc         U_Walker_mermean.nc
cdo mermean -sellonlatbox,0,360,-20,20 V_ERA5_monthly_1979-2021_timmean.nc         V_Walker_mermean.nc
cdo mermean -sellonlatbox,0,360,-20,20 Q_ERA5_monthly_1979-2021_timmean.nc         Q_Walker_mermean.nc



