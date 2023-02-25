
cd /work/bb1153/b381639/NorESM

#bias related to ERA5
# prepare ref
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/U_Hadley_zonmean_w.nc U_Hadley_zonmean_w_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/V_Hadley_zonmean_w.nc V_Hadley_zonmean_w_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/Q_Hadley_zonmean_w.nc Q_Hadley_zonmean_w_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/OMEGA_Hadley_zonmean_w.nc OMEGA_Hadley_zonmean_w_ref.nc

# pre N2

cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  U_Hadley_zonmean_w.nc U_Hadley_zonmean_w_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  V_Hadley_zonmean_w.nc V_Hadley_zonmean_w_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  Q_Hadley_zonmean_w.nc Q_Hadley_zonmean_w_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  OMEGA_Hadley_zonmean_w.nc OMEGA_Hadley_zonmean_w_vert.nc



#interpolate hor and bias
cdo sub -remapnn,U_Hadley_zonmean_w_ref.nc             U_Hadley_zonmean_w_vert.nc           U_Hadley_zonmean_w_ref.nc        U_Hadley_zonmean_w_bias.nc
cdo sub -remapnn,V_Hadley_zonmean_w_ref.nc             V_Hadley_zonmean_w_vert.nc           V_Hadley_zonmean_w_ref.nc        V_Hadley_zonmean_w_bias.nc
cdo sub -remapnn,Q_Hadley_zonmean_w_ref.nc             Q_Hadley_zonmean_w_vert.nc           Q_Hadley_zonmean_w_ref.nc        Q_Hadley_zonmean_w_bias.nc
cdo sub -remapnn,OMEGA_Hadley_zonmean_w_ref.nc     OMEGA_Hadley_zonmean_w_vert.nc       OMEGA_Hadley_zonmean_w_ref.nc    OMEGA_Hadley_zonmean_w_bias.nc



#bias related to ERA5
# prepare ref
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/U_Hadley_zonmean_e.nc U_Hadley_zonmean_e_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/V_Hadley_zonmean_e.nc V_Hadley_zonmean_e_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/Q_Hadley_zonmean_e.nc Q_Hadley_zonmean_e_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/OMEGA_Hadley_zonmean_e.nc OMEGA_Hadley_zonmean_e_ref.nc

# pre N2

cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  U_Hadley_zonmean_e.nc U_Hadley_zonmean_e_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  V_Hadley_zonmean_e.nc V_Hadley_zonmean_e_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  Q_Hadley_zonmean_e.nc Q_Hadley_zonmean_e_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  OMEGA_Hadley_zonmean_e.nc OMEGA_Hadley_zonmean_e_vert.nc



#interpolate hor and bias
cdo sub -remapnn,U_Hadley_zonmean_e_ref.nc             U_Hadley_zonmean_e_vert.nc           U_Hadley_zonmean_e_ref.nc        U_Hadley_zonmean_e_bias.nc
cdo sub -remapnn,V_Hadley_zonmean_e_ref.nc             V_Hadley_zonmean_e_vert.nc           V_Hadley_zonmean_e_ref.nc        V_Hadley_zonmean_e_bias.nc
cdo sub -remapnn,Q_Hadley_zonmean_e_ref.nc             Q_Hadley_zonmean_e_vert.nc           Q_Hadley_zonmean_e_ref.nc        Q_Hadley_zonmean_e_bias.nc
cdo sub -remapnn,OMEGA_Hadley_zonmean_e_ref.nc     OMEGA_Hadley_zonmean_e_vert.nc       OMEGA_Hadley_zonmean_e_ref.nc    OMEGA_Hadley_zonmean_e_bias.nc



exit
#bias related to ERA5
# prepare ref
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/U_Hadley_zonmean.nc U_Hadley_zonmean_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/V_Hadley_zonmean.nc V_Hadley_zonmean_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/Q_Hadley_zonmean.nc Q_Hadley_zonmean_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/OMEGA_Hadley_zonmean.nc OMEGA_Hadley_zonmean_ref.nc

# pre N2

cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  U_Hadley_zonmean.nc U_Hadley_zonmean_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  V_Hadley_zonmean.nc V_Hadley_zonmean_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  Q_Hadley_zonmean.nc Q_Hadley_zonmean_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  OMEGA_Hadley_zonmean.nc OMEGA_Hadley_zonmean_vert.nc



#interpolate hor and bias
cdo sub -remapnn,U_Hadley_zonmean_ref.nc             U_Hadley_zonmean_vert.nc           U_Hadley_zonmean_ref.nc        U_Hadley_zonmean_bias.nc
cdo sub -remapnn,V_Hadley_zonmean_ref.nc             V_Hadley_zonmean_vert.nc           V_Hadley_zonmean_ref.nc        V_Hadley_zonmean_bias.nc
cdo sub -remapnn,Q_Hadley_zonmean_ref.nc             Q_Hadley_zonmean_vert.nc           Q_Hadley_zonmean_ref.nc        Q_Hadley_zonmean_bias.nc
cdo sub -remapnn,OMEGA_Hadley_zonmean_ref.nc     OMEGA_Hadley_zonmean_vert.nc       OMEGA_Hadley_zonmean_ref.nc    OMEGA_Hadley_zonmean_bias.nc

#bias related to ERA5
# prepare ref
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/U_Walker_mermean.nc U_Walker_mermean_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/V_Walker_mermean.nc V_Walker_mermean_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/Q_Walker_mermean.nc Q_Walker_mermean_ref.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100 /work/bb1153/b381639/ERA5/OMEGA_Walker_mermean.nc OMEGA_Walker_mermean_ref.nc

# pre N2

cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  U_Walker_mermean.nc U_Walker_mermean_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  V_Walker_mermean.nc V_Walker_mermean_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  Q_Walker_mermean.nc Q_Walker_mermean_vert.nc
cdo intlevel,990,925,850,800,700,600,500,400,300,250,200,150,100  OMEGA_Walker_mermean.nc OMEGA_Walker_mermean_vert.nc



#interpolate hor and bias
cdo sub -remapnn,U_Walker_mermean_ref.nc             U_Walker_mermean_vert.nc           U_Walker_mermean_ref.nc        U_Walker_mermean_bias.nc
cdo sub -remapnn,V_Walker_mermean_ref.nc             V_Walker_mermean_vert.nc           V_Walker_mermean_ref.nc        V_Walker_mermean_bias.nc
cdo sub -remapnn,Q_Walker_mermean_ref.nc             Q_Walker_mermean_vert.nc           Q_Walker_mermean_ref.nc        Q_Walker_mermean_bias.nc
cdo sub -remapnn,OMEGA_Walker_mermean_ref.nc     OMEGA_Walker_mermean_vert.nc       OMEGA_Walker_mermean_ref.nc    OMEGA_Walker_mermean_bias.nc

exit

cdo zonmean -sellonlatbox,120,270,-50,50 OMEGA_150_timmean.nc OMEGA_Hadley_zonmean.nc
cdo zonmean -sellonlatbox,120,270,-50,50 U_150_timmean.nc         U_Hadley_zonmean.nc
cdo zonmean -sellonlatbox,120,270,-50,50 V_150_timmean.nc         V_Hadley_zonmean.nc
cdo zonmean -sellonlatbox,120,270,-50,50 Q_150_timmean.nc         Q_Hadley_zonmean.nc


cdo zonmean -sellonlatbox,120,180,-50,50 OMEGA_150_timmean.nc OMEGA_Hadley_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 U_150_timmean.nc         U_Hadley_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 V_150_timmean.nc         V_Hadley_zonmean_w.nc
cdo zonmean -sellonlatbox,120,180,-50,50 Q_150_timmean.nc         Q_Hadley_zonmean_w.nc

cdo zonmean -sellonlatbox,180,270,-50,50 OMEGA_150_timmean.nc OMEGA_Hadley_zonmean_e.nc
cdo zonmean -sellonlatbox,180,270,-50,50 U_150_timmean.nc         U_Hadley_zonmean_e.nc
cdo zonmean -sellonlatbox,180,270,-50,50 V_150_timmean.nc         V_Hadley_zonmean_e.nc
cdo zonmean -sellonlatbox,180,270,-50,50 Q_150_timmean.nc         Q_Hadley_zonmean_e.nc

cdo mermean -sellonlatbox,0,360,-20,20 OMEGA_150_timmean.nc OMEGA_Walker_mermean.nc
cdo mermean -sellonlatbox,0,360,-20,20 U_150_timmean.nc         U_Walker_mermean.nc
cdo mermean -sellonlatbox,0,360,-20,20 V_150_timmean.nc         V_Walker_mermean.nc
cdo mermean -sellonlatbox,0,360,-20,20 Q_150_timmean.nc         Q_Walker_mermean.nc



