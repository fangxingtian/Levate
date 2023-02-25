import numpy as np
from scipy import stats
import scipy
from scipy.stats import linregress
import netCDF4 as nc4
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import cartopy.crs as ccrs
import numpy.ma as ma
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

font = {'family' : 'calibri',
       'weight': 'bold',
       'size': 20}
plt.rc('font', **font)
plt.rc('axes',edgecolor='k',linewidth=3)

# Function to filter the data

def nan_gaussian_filter(field,sigma):
    from scipy.ndimage import gaussian_filter
    field = np.double(field)    
    # Take the original field and replace the NaNs with zeros.
    field0 = field.copy()
    field0[np.isnan(field)] = 0
    ff = gaussian_filter(field0, sigma=sigma)
    # Create the smoothed weight field.
    weight = 0*field.copy()+1
    weight[np.isnan(field)] = 0
    ww = gaussian_filter(weight, sigma=sigma)
    zz = ff/(ww*weight) # This rescale for the actual weights used in the filter and set to NaN where the field
                        # was originally NaN.
    return zz


def mesh(lat,lon):
    mesh_lat = np.empty([len(lat),len(lon)])
    mesh_lon = np.empty([len(lat),len(lon)])
    for i in range(len(lat)):
        for j in range(len(lon)):
            mesh_lat[i,j] = lat[i]
            mesh_lon[i,j] = lon[j]
    return mesh_lat, mesh_lon



# Load data for SeaFlux and ERA5 (SST, qair2m and wspd10m). Dimensions time x lat x lon

fil_era5 = Dataset('/Users/pabloff/Documents/PhD/Data/ERA5/Coare3.5_DJF/ERA5_wspd10m_sst_tair2m_qair2m_lhf_DJF_2008-2018_05N17N51W60W.nc')
fil_sf = Dataset('/Users/pabloff/Documents/PhD/Data/SeaFlux/Coare3.5_DJF/SeaFlux_wspd10m_sst_tair2m_qair2m_lhf_DJF_2008-2018_05N17N51W60W.nc')


lat_sf = fil_sf.variables['lat'][:]
lon_sf = fil_sf.variables['lon'][:]

lat_era5 = fil_era5.variables['lat'][:]
lon_era5 = fil_era5.variables['lon'][:]

qair2m_sf = fil_sf.variables['qair2m'][:]
wspd10m_sf = fil_sf.variables['wspd10m'][:]
sst_sf = fil_sf.variables['sst'][:]

qair2m_era5 = fil_era5.variables['qair2m'][:]
wspd10m_era5 = fil_era5.variables['wspd10m'][:]
sst_era5 = fil_era5.variables['sst'][:]
                          
                
qair2m_sf_smoothed = np.empty(qair2m_sf.shape)
wspd10m_sf_smoothed = np.empty(wspd10m_sf.shape)
sst_sf_smoothed = np.empty(sst_sf.shape)

qair2m_era5_smoothed = np.empty(qair2m_era5.shape)
wspd10m_era5_smoothed = np.empty(wspd10m_era5.shape)
sst_era5_smoothed = np.empty(sst_era5.shape)

# Compute smoothed and residual fields

for j in range(qair2m_sf.shape[0]):
    qair2m_sf_smoothed[j,:,:] = nan_gaussian_filter(qair2m_sf[j,:,:],6)
    wspd10m_sf_smoothed[j,:,:] = nan_gaussian_filter(wspd10m_sf[j,:,:],6)
    sst_sf_smoothed[j,:,:] = nan_gaussian_filter(sst_sf[j,:,:],6)
        
    qair2m_era5_smoothed[j,:,:] = nan_gaussian_filter(qair2m_era5[j,:,:],6)
    wspd10m_era5_smoothed[j,:,:] = nan_gaussian_filter(wspd10m_era5[j,:,:],6)
    sst_era5_smoothed[j,:,:] = nan_gaussian_filter(sst_era5[j,:,:],6)
        
        
    # Calculo los campos residuo 
    qair2m_sf_residual = qair2m_sf - qair2m_sf_smoothed
    wspd10m_sf_residual = wspd10m_sf - wspd10m_sf_smoothed
    sst_sf_residual = sst_sf - sst_sf_smoothed
    
    qair2m_era5_residual = qair2m_era5 - qair2m_era5_smoothed
    wspd10m_era5_residual = wspd10m_era5 - wspd10m_era5_smoothed
    sst_era5_residual = sst_era5 - sst_era5_smoothed

# Compute slopes for all the datasets (smoothed and residual fields)

m_u_sf = np.empty([5,len(lat_sf),len(lon_sf)])
m_q_sf = np.empty([5,len(lat_sf),len(lon_sf)])
m_u_era5 = np.empty([5,len(lat_era5),len(lon_era5)])
m_q_era5 = np.empty([5,len(lat_era5),len(lon_era5)])

for i in range(len(lat_sf)):
    for j in range(len(lon_sf)):
        u_stats_tot = wspd10m_sf_residual[:,i,j]
        sst_stats_tot = sst_sf_residual[:,i,j]
        q_stats_tot = qair2m_sf_residual[:,i,j]

        mask_q_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(q_stats_tot[:])
        mask_u_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(u_stats_tot[:])
        
    
        varx_q_tot = sst_stats_tot[mask_q_tot]
        vary_q_tot = q_stats_tot[mask_q_tot]

        varx_u_tot = sst_stats_tot[mask_u_tot]
        vary_u_tot = u_stats_tot[mask_u_tot]
   
    
        if ((varx_q_tot.shape[0])) == 0 or ((vary_q_tot.shape[0]) == 0):
            m_q_sf[:,i,j] = np.nan *  np.ones(5)
        
        else:
            m_q_sf[:,i,j] = scipy.stats.linregress(varx_q_tot,vary_q_tot)                   
            
        if ((varx_u_tot.shape[0])) == 0 or ((vary_u_tot.shape[0]) == 0):
                    
            m_u_sf[:,i,j] = np.nan * np.ones(5)
        
        else:
            m_u_sf[:,i,j] = scipy.stats.linregress(varx_u_tot,vary_u_tot)
                   

# Do the same for ERA5
for i in range(len(lat_era5)):
    for j in range(len(lon_era5)):
        u_stats_tot = wspd10m_era5_residual[:,i,j]
        sst_stats_tot = sst_era5_residual[:,i,j]
        q_stats_tot = qair2m_era5_residual[:,i,j]

        mask_q_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(q_stats_tot[:])
        mask_u_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(u_stats_tot[:])
        
    
        varx_q_tot = sst_stats_tot[mask_q_tot]
        vary_q_tot = q_stats_tot[mask_q_tot]

        varx_u_tot = sst_stats_tot[mask_u_tot]
        vary_u_tot = u_stats_tot[mask_u_tot]

    
        if ((varx_q_tot.shape[0])) == 0 or ((vary_q_tot.shape[0]) == 0):
            m_q_era5[:,i,j] = np.nan *  np.ones(5)
        
        else:
            m_q_era5[:,i,j] = scipy.stats.linregress(varx_q_tot,vary_q_tot)                   
            
        if ((varx_u_tot.shape[0])) == 0 or ((vary_u_tot.shape[0]) == 0):
                    
            m_u_era5[:,i,j] = np.nan * np.ones(5)
        
        else:
            m_u_era5[:,i,j] = scipy.stats.linregress(varx_u_tot,vary_u_tot)


# Same for the smoothed fields

m_u_s_sf = np.empty([5,len(lat_sf),len(lon_sf)])
m_q_s_sf = np.empty([5,len(lat_sf),len(lon_sf)])
m_u_s_era5 = np.empty([5,len(lat_era5),len(lon_era5)])
m_q_s_era5 = np.empty([5,len(lat_era5),len(lon_era5)])



for i in range(len(lat_sf)):
    for j in range(len(lon_sf)):
        u_stats_tot = wspd10m_sf_smoothed[:,i,j]
        sst_stats_tot = sst_sf_smoothed[:,i,j]
        q_stats_tot = qair2m_sf_smoothed[:,i,j]


        mask_q_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(q_stats_tot[:])
        mask_u_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(u_stats_tot[:])
        
    
        varx_q_tot = sst_stats_tot[mask_q_tot]
        vary_q_tot = q_stats_tot[mask_q_tot]

        varx_u_tot = sst_stats_tot[mask_u_tot]
        vary_u_tot = u_stats_tot[mask_u_tot]
   
    
        if ((varx_q_tot.shape[0])) == 0 or ((vary_q_tot.shape[0]) == 0):
            m_q_s_sf[:,i,j] = np.nan *  np.ones(5)
        
        else:
            m_q_s_sf[:,i,j] = scipy.stats.linregress(varx_q_tot,vary_q_tot)                   
            
        if ((varx_u_tot.shape[0])) == 0 or ((vary_u_tot.shape[0]) == 0):
                    
            m_u_s_sf[:,i,j] = np.nan * np.ones(5)
        
        else:
            m_u_s_sf[:,i,j] = scipy.stats.linregress(varx_u_tot,vary_u_tot)            
            
# Again for ERA5

for i in range(len(lat_era5)):
    for j in range(len(lon_era5)):
        u_stats_tot = wspd10m_era5_smoothed[:,i,j]
        sst_stats_tot = sst_era5_smoothed[:,i,j]
        q_stats_tot = qair2m_era5_smoothed[:,i,j]

        mask_q_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(q_stats_tot[:])
        mask_u_tot = ~np.isnan(sst_stats_tot[:]) & ~np.isnan(u_stats_tot[:])
            
        varx_q_tot = sst_stats_tot[mask_q_tot]
        vary_q_tot = q_stats_tot[mask_q_tot]

        varx_u_tot = sst_stats_tot[mask_u_tot]
        vary_u_tot = u_stats_tot[mask_u_tot]
   
    
        if ((varx_q_tot.shape[0])) == 0 or ((vary_q_tot.shape[0]) == 0):
            m_q_s_era5[:,i,j] = np.nan *  np.ones(5)
        
        else:
            m_q_s_era5[:,i,j] = scipy.stats.linregress(varx_q_tot,vary_q_tot)                   
            
        if ((varx_u_tot.shape[0])) == 0 or ((vary_u_tot.shape[0]) == 0):
                    
            m_u_s_era5[:,i,j] = np.nan * np.ones(5)
        
        else:
            m_u_s_era5[:,i,j] = scipy.stats.linregress(varx_u_tot,vary_u_tot)


# Plot the coefficients 

#######################################

# SeaFlux

#######################################

lat_central = lat_sf
lon_central = lon_sf
Lat_central, Lon_central = mesh(lat_sf,lon_sf)


figTS,axs = plt.subplots(2,2,figsize=(25,30), subplot_kw={'projection': ccrs.PlateCarree(180)})
lev_1 = np.arange(-1,1.2,0.2)
lev_2 = np.arange(-1,1.2,0.2)

        
plt.suptitle('SeaFlux' ,weight='bold')
        
cs_1 = axs[0,0].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(m_q_s_sf[0,:,:]),#,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='Reds',vmin = 0, vmax = 1.3)
        
        
LON_central = ma.masked_where(m_q_s_sf[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_q_s_sf[3,:,:]>0.01, (Lat_central))


hatch = axs[0,0].plot(np.transpose(LON_central+180),np.transpose(LAT_central),'.',color='black',markersize=5)
        
cs_2 = axs[0,1].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(m_q_sf[0,:,:]),#,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='bwr',vmin = -0.5, vmax = 0.5)
        
LON_central = ma.masked_where(m_q_sf[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_q_sf[3,:,:]>0.01, (Lat_central))

hatch = axs[0,1].plot(np.transpose(LON_central+180),np.transpose(LAT_central),'.',color='black',markersize=5)
        
cs_3 = axs[1,0].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(np.asarray(m_u_s_sf[0,:,:])), #,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='Blues_r',vmin = -1.3, vmax  =0)
        
LON_central = ma.masked_where(m_u_s_sf[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_u_s_sf[3,:,:]>0.01, (Lat_central))

hatch = axs[1,0].plot(np.transpose(LON_central)+180,np.transpose(LAT_central),'.',color='black',markersize=5)
        
cs_4 = axs[1,1].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(np.asarray(m_u_sf[0,:,:])), #,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='bwr',vmin = -0.5, vmax = 0.5)
        
LON_central = ma.masked_where(m_u_sf[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_u_sf[3,:,:]>0.01, (Lat_central))

hatch = axs[1,1].plot(np.transpose(LON_central)+180,np.transpose(LAT_central),'.',color='black',markersize=5)

plt.colorbar(cs_1,ax=axs[0,0],orientation='horizontal',label='g·kg$^{-1}$·°C$^{-1}$')
plt.colorbar(cs_2,ax=axs[0,1],orientation = 'horizontal',label='g·kg$^{-1}$·°C$^{-1}$')
plt.colorbar(cs_3,ax=axs[1,0],orientation='horizontal',label='m·s$^{-1}$·°C$^{-1}$')
plt.colorbar(cs_4,ax=axs[1,1],orientation='horizontal',label='m·s$^{-1}$·°C$^{-1}$')

axs[0,0].set_xlim(-60+180,-51.5+180)
axs[1,0].set_xlim(-60+180,-51.5+180)
axs[0,1].set_xlim(-60+180,-51.5+180)
axs[1,1].set_xlim(-60+180,-51.5+180)

axs[0,0].set_ylim(5,17)
axs[1,0].set_ylim(5,17)
axs[0,1].set_ylim(5,17)
axs[1,1].set_ylim(5,17)
        
        
axs[0,0].set_title('Smoothed field \n a)',weight='bold')
axs[0,1].set_title('Residual field \n b)',weight='bold')
axs[1,0].set_title(r'c)', weight='bold')
axs[1,1].set_title(r'd)',weight='bold')
        
axs[0,0].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
axs[0,1].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
axs[1,0].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
axs[1,1].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
        
cs = axs[0,0].coastlines(resolution='110m', linewidth=1)
cs = axs[0,1].coastlines(resolution='110m', linewidth=1)
cs = axs[1,0].coastlines(resolution='110m', linewidth=1)
cs = axs[1,1].coastlines(resolution='110m', linewidth=1)
        
gl = axs[0,0].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False

gl = axs[0,1].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
        
gl = axs[1,0].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
        
gl = axs[1,1].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
        
plt.savefig('/Users/pabloff/Desktop/Prueba_1.jpg')
   

#########################################
# Same for ERA5

lat_central = lat_era5
lon_central = lon_era5
Lat_central, Lon_central = mesh(lat_era5,lon_era5)

#########################################

figTS,axs = plt.subplots(2,2,figsize=(25,30), subplot_kw={'projection': ccrs.PlateCarree(180)})
lev_1 = np.arange(-1,1.2,0.2)
lev_2 = np.arange(-1,1.2,0.2)


plt.suptitle('ERA5' ,weight='bold')
        
cs_1 = axs[0,0].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(m_q_s_era5[0,:,:]),#,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='Reds',vmin = 0, vmax = 1.3)
        
        
LON_central = ma.masked_where(m_q_s_era5[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_q_s_era5[3,:,:]>0.01, (Lat_central))


hatch = axs[0,0].plot(np.transpose(LON_central+180),np.transpose(LAT_central),'.',color='black',markersize=5)
        
cs_2 = axs[0,1].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(m_q_era5[0,:,:]),#,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='bwr',vmin = -0.5, vmax = 0.5)
        
LON_central = ma.masked_where(m_q_era5[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_q_era5[3,:,:]>0.01, (Lat_central))

hatch = axs[0,1].plot(np.transpose(LON_central+180),np.transpose(LAT_central),'.',color='black',markersize=5)
        
cs_3 = axs[1,0].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(np.asarray(m_u_s_era5[0,:,:])), #,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='Blues_r',vmin = -1.3, vmax  =0)
        
LON_central = ma.masked_where(m_u_s_era5[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_u_s_era5[3,:,:]>0.01, (Lat_central))

hatch = axs[1,0].plot(np.transpose(LON_central)+180,np.transpose(LAT_central),'.',color='black',markersize=5)
        
cs_4 = axs[1,1].pcolormesh(np.asarray(lon_central),np.asarray(lat_central),(np.asarray(m_u_era5[0,:,:])), #,levels = lev_1,
               transform=ccrs.PlateCarree(),cmap='bwr',vmin = -0.5, vmax = 0.5)
        
LON_central = ma.masked_where(m_u_era5[3,:,:]>0.01, (Lon_central))
LAT_central = ma.masked_where(m_u_era5[3,:,:]>0.01, (Lat_central))

hatch = axs[1,1].plot(np.transpose(LON_central)+180,np.transpose(LAT_central),'.',color='black',markersize=5)

plt.colorbar(cs_1,ax=axs[0,0],orientation='horizontal',label='g·kg$^{-1}$·°C$^{-1}$')
plt.colorbar(cs_2,ax=axs[0,1],orientation = 'horizontal',label='g·kg$^{-1}$·°C$^{-1}$')
plt.colorbar(cs_3,ax=axs[1,0],orientation='horizontal',label='m·s$^{-1}$·°C$^{-1}$')
plt.colorbar(cs_4,ax=axs[1,1],orientation='horizontal',label='m·s$^{-1}$·°C$^{-1}$')

axs[0,0].set_xlim(-60+180,-51.5+180)
axs[1,0].set_xlim(-60+180,-51.5+180)
axs[0,1].set_xlim(-60+180,-51.5+180)
axs[1,1].set_xlim(-60+180,-51.5+180)

axs[0,0].set_ylim(5,17)
axs[1,0].set_ylim(5,17)
axs[0,1].set_ylim(5,17)
axs[1,1].set_ylim(5,17)
        
        
axs[0,0].set_title('Smoothed field \n a)',weight='bold')
axs[0,1].set_title('Residual field \n b)',weight='bold')
axs[1,0].set_title(r'c)', weight='bold')
axs[1,1].set_title(r'd)',weight='bold')
        
axs[0,0].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
axs[0,1].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
axs[1,0].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
axs[1,1].add_feature(cartopy.feature.LAND,facecolor='gray',zorder=100, edgecolor='k')
        
cs = axs[0,0].coastlines(resolution='110m', linewidth=1)
cs = axs[0,1].coastlines(resolution='110m', linewidth=1)
cs = axs[1,0].coastlines(resolution='110m', linewidth=1)
cs = axs[1,1].coastlines(resolution='110m', linewidth=1)
        
gl = axs[0,0].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False

gl = axs[0,1].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
        
gl = axs[1,0].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
        
gl = axs[1,1].gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
        
plt.savefig('/Users/pabloff/Desktop/Prueba_2.jpg')
   






