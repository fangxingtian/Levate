
cd /work/bb1153/b381639/NorESM

cdo zonmean -sellonlatbox,120,-90,-50,50 OMEGA_150_timmean.nc OMEGA_walker_zonmean.nc
cdo zonmean -sellonlatbox,120,-90,-50,50 U_150_timmean.nc         U_walker_zonmean.nc
cdo zonmean -sellonlatbox,120,-90,-50,50 V_150_timmean.nc         V_walker_zonmean.nc
cdo zonmean -sellonlatbox,120,-90,-50,50 Q_150_timmean.nc         Q_walker_zonmean.nc


cdo zonmean -sellonlatbox,120,180,-50,50 OMEGA_150_timmean.nc OMEGA_walker_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 U_150_timmean.nc         U_walker_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 V_150_timmean.nc         V_walker_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 Q_150_timmean.nc         Q_walker_zonmean_w.nc

cdo zonmean -sellonlatbox,180,-90,-50,50 OMEGA_150_timmean.nc OMEGA_walker_zonmean_e.nc
cdo zonmean -sellonlatbox,180,-90,-50,50 U_150_timmean.nc         U_walker_zonmean_e.nc
cdo zonmean -sellonlatbox,180,-90,-50,50 V_150_timmean.nc         V_walker_zonmean_e.nc
cdo zonmean -sellonlatbox,180,-90,-50,50 Q_150_timmean.nc         Q_walker_zonmean_e.nc

exit
cdo mermean -sellonlatbox,-180,180,-20,20 OMEGA_150_timmean.nc OMEGA_walker_mermean.nc
cdo mermean -sellonlatbox,-180,180,-20,20 U_150_timmean.nc U_walker_mermean.nc
cdo mermean -sellonlatbox,-180,180,-20,20 V_150_timmean.nc V_walker_mermean.nc
cdo mermean -sellonlatbox,-180,180,-20,20 Q_150_timmean.nc Q_walker_mermean.nc



